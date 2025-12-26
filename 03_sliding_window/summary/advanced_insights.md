# Sliding Window 進階洞見 (Advanced Insights)

> 這份文檔總結了從實際題目中提煉出的深層技巧與思維模式，補充 `sliding_window_overview.md` 中的基礎模板。

---

## 目錄 (Content Table)

1. [預處理 + Sliding Window：不是所有題目都能直接滑](#1-預處理--sliding-window不是所有題目都能直接滑)
2. [單調隊列 (Monotonic Deque)：O(1) 查詢窗口極值](#2-單調隊列-monotonic-dequeo1-查詢窗口極值)
3. [Rolling Hash：高效比較窗口內容](#3-rolling-hash高效比較窗口內容)
4. [窗口收縮：while vs if 的選擇](#4-窗口收縮while-vs-if-的選擇)
5. [狀態追蹤：避免重覆計算](#5-狀態追蹤避免重覆計算)
6. [窗口大小限制 vs 窗口條件限制](#6-窗口大小限制-vs-窗口條件限制)
7. [固定窗口的兩種實現方式](#7-固定窗口的兩種實現方式)
8. [綜合技巧：何時使用哪種方法？](#8-綜合技巧何時使用哪種方法)
9. [常見陷阱與調試技巧](#9-常見陷阱與調試技巧)
10. [總結：Sliding Window 的思維模式](#10-總結sliding-window-的思維模式)
11. [參考題目清單](#參考題目清單)

---

## 1. 預處理 + Sliding Window：不是所有題目都能直接滑

### 洞見
**有些題目需要先對數據進行預處理（排序、編碼等），才能有效使用滑動窗口。**

### 典型案例

#### FrequencyoftheMostFrequentElement
```python
def max_frequency(nums, k):
    nums.sort()  # 必須先排序！
    start = 0
    window_sum = 0
    
    for end in range(len(nums)):
        window_sum += nums[end]
        # 計算把窗口內所有元素變成 nums[end] 需要的操作數
        required_ops = nums[end] * (end - start + 1) - window_sum
        
        while required_ops > k:
            window_sum -= nums[start]
            start += 1
            required_ops = nums[end] * (end - start + 1) - window_sum
    
    return end - start + 1
```

**為什麽要排序？**
- 排序後，窗口內的目標值一定是 `nums[end]`（最大值）
- 可以用數學公式 `target × len - sum` 快速計算操作數
- 如果不排序，無法確定窗口內應該把所有元素變成哪個值

**關鍵公式：**
```
把窗口 [start..end] 的所有元素變成 nums[end] 需要的操作數：
required_ops = nums[end] × (end - start + 1) - window_sum
```

### 何時需要預處理？

| 預處理類型 | 使用時機 | 典型題目 |
|----------|---------|---------|
| **排序** | 需要窗口內的"相對順序"而非"原始順序" | Frequency of Most Frequent Element |
| **編碼/Hash** | 需要快速比較窗口內容，但內容很長 | Repeated DNA Sequence (Rolling Hash) |
| **前綴和** | 需要快速計算任意區間的和 | 某些 subarray sum 變體 |

---

## 2. 單調隊列 (Monotonic Deque)：O(1) 查詢窗口極值

### 洞見
**當需要在滑動窗口中快速查詢最大/最小值時，使用單調隊列可以在 O(1) 時間內完成。**

### 典型案例：FindMaximuminSlidingWindow

```python
from collections import deque

def find_max_sliding_window(nums, w):
    dq = deque()  # 存儲索引
    result = []
    
    for i in range(len(nums)):
        # 1. 移除過期的索引（超出窗口範圍）
        if dq and dq[0] < i - w + 1:
            dq.popleft()
        
        # 2. 維護單調遞減：移除所有比當前元素小的元素
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        # 3. 加入當前索引
        dq.append(i)
        
        # 4. 窗口形成後，隊首就是最大值
        if i >= w - 1:
            result.append(nums[dq[0]])
    
    return result
```

### 單調隊列的性質

**不變式 (Invariant)：** `nums[dq[0]] ≥ nums[dq[1]] ≥ ... ≥ nums[dq[-1]]`

**為什麽有效？**
- 隊首永遠是窗口內的最大值
- 如果新元素比隊尾大，隊尾元素永遠不可能成為最大值 → 可以安全移除
- 每個元素最多入隊一次、出隊一次 → 總時間 O(n)

### 單調隊列 vs 普通窗口

| 方法 | 時間覆雜度 | 適用場景 |
|-----|-----------|---------|
| **樸素遍歷** | O(n × w) | 每次窗口滑動都重新計算 max/min |
| **Heap** | O(n log w) | 需要頻繁插入刪除，但不保證刪除的是堆頂 |
| **單調隊列** | O(n) | 固定窗口內的最大/最小值查詢 |

---

## 3. Rolling Hash：高效比較窗口內容

### 洞見
**當需要比較大量固定長度的子字符串時，Rolling Hash 可以將每次窗口滑動的更新從 O(k) 降到 O(1)。**

### 典型案例：RepeatedDNASequence

```python
def findRepeatedDnaSequences(s, k):
    to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
    encoded_sequence = [to_int[c] for c in s]
    
    a = 4  # 基數（因為有 4 種字符）
    h = 0  # 當前哈希值
    a_k = a ** k  # 預計算 a^k
    
    # 計算第一個窗口的哈希
    for i in range(k):
        h = h * a + encoded_sequence[i]
    
    seen_hashes = {h}
    output = set()
    
    # Rolling Hash：O(1) 更新
    for end in range(k, len(s)):
        start = end - k + 1
        # 移除最左邊的字符，加入新字符
        h = h * a - encoded_sequence[start - 1] * a_k + encoded_sequence[end]
        
        if h in seen_hashes:
            output.add(s[start : start + k])
        else:
            seen_hashes.add(h)
    
    return list(output)
```

### Rolling Hash 公式

假設窗口是 `s[i..i+k-1]`，滑動到 `s[i+1..i+k]`：

```
old_hash = s[i] × a^(k-1) + s[i+1] × a^(k-2) + ... + s[i+k-1] × a^0

new_hash = old_hash × a - s[i] × a^k + s[i+k]
         = (old_hash - s[i] × a^(k-1)) × a + s[i+k]
```

**注意：** 為了避免浮點誤差和溢出，通常會取模一個大質數。

### Rolling Hash vs 直接比較

| 方法 | 每次窗口更新 | 總時間覆雜度 |
|-----|------------|-------------|
| **直接字符串比較** | O(k) | O(n × k) |
| **Rolling Hash** | O(1) | O(n) |

---

## 4. 窗口收縮：while vs if 的選擇

### 洞見
**收縮窗口時用 `while` 還是 `if`，取決於題目要求和優化目標。**

### 規則總結

| 使用 `while` | 使用 `if` |
|-------------|----------|
| 需要找**最短**窗口 | 需要找**最長**窗口 |
| 必須保證窗口**完全合法** | 允許窗口**暫時不合法** |
| 例：Minimum Size Subarray Sum | 例：Longest Repeating Character Replacement |

### 案例對比

#### Case 1：MinimumSizeSubarraySum（最短 → 用 while）

```python
def min_sub_array_len(target, nums):
    left = 0
    window_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        # 必須用 while：要把窗口收縮到最小
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0
```

**為什麽用 `while`？** 因為要找最短，所以當 `window_sum >= target` 時，要盡可能收縮左邊界。

#### Case 2：LongestRepeatingCharacterReplacement（最長 → 用 if）

```python
def longest_repeating_character_replacement(s, k):
    start = 0
    most_freq_chr = 0
    chr_dict = {}
    length_of_max_substring = 0
    
    for end in range(len(s)):
        chr_dict[s[end]] = chr_dict.get(s[end], 0) + 1
        most_freq_chr = max(most_freq_chr, chr_dict[s[end]])
        
        curr_win_len = end - start + 1
        
        # 只用 if：不需要完全收縮
        if curr_win_len - most_freq_chr > k:
            chr_dict[s[start]] -= 1
            start += 1
        
        # 這里的窗口長度只會增加或不變，不會減少
        length_of_max_substring = max(end - start + 1, length_of_max_substring)
    
    return length_of_max_substring
```

**為什麽用 `if`？**
- 我們只需要找最長的合法窗口
- 窗口不合法時，只需移動一步 `left`，讓窗口長度不增加
- `most_freq_chr` 不需要更新（即使它在窗口收縮後不再準確），因為只有當窗口變得更長時，我們才需要更新答案

**反直覺的優化：** `most_freq_chr` 可以是"歷史最大值"，不需要實時更新，因為如果當前窗口的頻率沒有超過歷史最大值，那麽它不可能產生更長的答案。

---

## 5. 狀態追蹤：避免重覆計算

### 洞見
**用額外的變量追蹤窗口狀態，避免每次都重新計算是否滿足條件。**

### 典型案例：MinimumWindowSubstring

```python
def min_window(s, t):
    req_dict = {}  # t 中每個字符的需求數量
    for char in t:
        req_dict[char] = req_dict.get(char, 0) + 1
    
    cur_win = {}  # 當前窗口中每個字符的數量
    required = len(req_dict.keys())  # 需要滿足的字符種類數
    current = 0  # 當前已滿足的字符種類數
    
    left = 0
    res_len = float('inf')
    res = [-1, -1]
    
    for right in range(len(s)):
        if s[right] in req_dict:
            cur_win[s[right]] = cur_win.get(s[right], 0) + 1
            
            # 狀態追蹤：只在"剛好滿足"時更新 current
            if cur_win[s[right]] == req_dict[s[right]]:
                current += 1
        
        # 只有當完全滿足條件時才嘗試收縮
        while current == required:
            # 更新答案
            if right - left + 1 < res_len:
                res = [left, right]
                res_len = right - left + 1
            
            # 收縮左邊界
            if s[left] in req_dict:
                cur_win[s[left]] -= 1
                # 狀態追蹤：只在"不再滿足"時更新 current
                if cur_win[s[left]] < req_dict[s[left]]:
                    current -= 1
            
            left += 1
    
    left, right = res
    return s[left:right + 1] if res_len != float('inf') else ""
```

### 狀態追蹤的優勢

**樸素做法：** 每次都檢查窗口是否滿足條件
```python
def is_valid_window():
    for char in req_dict:
        if cur_win.get(char, 0) < req_dict[char]:
            return False
    return True
```
時間覆雜度：O(|t|) 每次檢查

**優化做法：** 維護 `current` 變量
```python
# current == required 時窗口合法
# 只在"邊界變化"時更新 current
```
時間覆雜度：O(1) 檢查

---

## 6. 窗口大小限制 vs 窗口條件限制

### 洞見
**Sliding Window 有兩種約束方式：限制窗口大小 vs 限制窗口條件。**

### 類型 1：窗口大小限制

**特征：** 窗口大小不能超過某個值 `k`

#### 案例：ContainsDuplicateII

```python
def contains_nearby_duplicate(nums, k):
    seen = set()
    
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        
        seen.add(nums[i])
        
        # 限制窗口大小：最多保留 k 個元素
        if len(seen) > k:
            seen.remove(nums[i - k])
    
    return False
```

**關鍵：** 窗口大小 `len(seen) <= k`，一旦超過就移除最左邊的元素。

### 類型 2：窗口條件限制

**特征：** 窗口必須滿足某種條件（如：最多 2 種水果、最多 k 次替換等）

#### 案例：FruitIntoBaskets

```python
def total_fruit(fruits):
    basket = {}
    left = 0
    max_collected = 0
    
    for right, f in enumerate(fruits):
        basket[f] = basket.get(f, 0) + 1
        
        # 限制窗口條件：最多 2 種水果
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        
        max_collected = max(max_collected, right - left + 1)
    
    return max_collected
```

**關鍵：** 窗口條件是 `len(basket) <= 2`，不是窗口大小。

### 對比總結

| 限制類型 | 檢查方式 | 移除策略 |
|---------|---------|---------|
| **大小限制** | `len(window) > k` | 移除 `nums[i - k]` |
| **條件限制** | `condition(window)` | 移除 `nums[left]`，`left += 1` |

---

## 7. 固定窗口的兩種實現方式

### 洞見
**固定大小的窗口有兩種常見實現方式，各有優缺點。**

### 方式 1：先建立窗口，再滑動

```python
def fixed_window_v1(nums, k):
    # 先建立第一個窗口
    window_sum = sum(nums[:k])
    result = window_sum
    
    # 然後滑動：每次加一個、減一個
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        result = max(result, window_sum)
    
    return result
```

**優點：** 代碼清晰，邏輯分明  
**缺點：** 需要特殊處理第一個窗口

### 方式 2：統一處理，用計數器判斷

```python
def fixed_window_v2(nums, k):
    window_sum = 0
    result = float('-inf')
    
    for i in range(len(nums)):
        window_sum += nums[i]
        
        # 窗口還未形成
        if i < k - 1:
            continue
        
        # 窗口已形成，更新答案
        result = max(result, window_sum)
        
        # 移除最左邊的元素
        window_sum -= nums[i - k + 1]
    
    return result
```

**優點：** 統一處理，不需要特殊情況  
**缺點：** 每次都要判斷 `i < k - 1`

### 方式 3：ContainsDuplicateII 的巧妙做法

```python
def contains_nearby_duplicate(nums, k):
    seen = set()
    
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        
        seen.add(nums[i])
        
        # 當窗口大小超過 k 時，移除最左邊的元素
        if len(seen) > k:
            seen.remove(nums[i - k])
    
    return False
```

**巧妙之處：** 用 `len(seen) > k` 自動控制窗口大小，不需要顯式的 `left` 指針。

---

## 8. 綜合技巧：何時使用哪種方法？

### 決策樹

```
是否需要在窗口內查詢極值（max/min）？
├─ 是 → 使用單調隊列 (Monotonic Deque)
│   └─ 例：Sliding Window Maximum
└─ 否 → 繼續判斷
    │
    窗口大小是否固定？
    ├─ 是 → 固定窗口模板
    │   ├─ 需要比較窗口內容？→ Rolling Hash
    │   │   └─ 例：Repeated DNA Sequences
    │   └─ 需要統計/求和？→ 簡單滑動
    │       └─ 例：Maximum Average Subarray I
    └─ 否 → 可變窗口模板
        │
        需要預處理嗎？
        ├─ 是 → 先排序/編碼，再滑動
        │   └─ 例：Frequency of Most Frequent Element
        └─ 否 → 直接滑動
            │
            目標是什麽？
            ├─ 找最長 → 用 if 收縮（窗口只增不減）
            │   └─ 例：Longest Repeating Character Replacement
            ├─ 找最短 → 用 while 收縮（盡可能小）
            │   └─ 例：Minimum Size Subarray Sum
            └─ 覆雜條件 → 用狀態追蹤
                └─ 例：Minimum Window Substring
```

---

## 9. 常見陷阱與調試技巧

### 陷阱 1：窗口索引的一致性

**錯誤示例：**
```python
for right in range(n):
    window.add(nums[right])
    
    while not is_valid():
        window.remove(nums[left])  # left 沒有初始化！
        left += 1
```

**正確做法：** 永遠記得初始化 `left = 0`

### 陷阱 2：過早更新答案

```python
# 錯誤：在窗口不合法時就更新
for right in range(n):
    window.add(nums[right])
    ans = max(ans, right - left + 1)  # ❌ 窗口可能不合法
    
    while not is_valid():
        window.remove(nums[left])
        left += 1

# 正確：在窗口合法後才更新
for right in range(n):
    window.add(nums[right])
    
    while not is_valid():
        window.remove(nums[left])
        left += 1
    
    ans = max(ans, right - left + 1)  # ✓ 窗口保證合法
```

### 陷阱 3：忘記更新狀態

```python
# 錯誤：移除元素時忘記更新狀態
while len(basket) > 2:
    left += 1  # ❌ 沒有從 basket 中移除

# 正確：同步更新窗口狀態
while len(basket) > 2:
    basket[fruits[left]] -= 1
    if basket[fruits[left]] == 0:
        del basket[fruits[left]]
    left += 1
```

### 調試技巧

**加入調試輸出：**
```python
for right in range(n):
    # ... 窗口操作 ...
    
    print(f"[{left}, {right}] window = {window}, valid = {is_valid()}")
    
    while not is_valid():
        # ... 收縮窗口 ...
```

**檢查不變式 (Invariants)：**
- 窗口狀態是否與實際窗口內容一致？
- 窗口是否總是合法的（或在收縮後變合法）？
- `left` 是否總是 <= `right + 1`？

---

## 10. 總結：Sliding Window 的思維模式

### 核心思想

> **用兩個指針維護一個"合法窗口"，通過增量更新狀態，避免重覆計算。**

### 三個關鍵問題

1. **窗口狀態是什麽？**
   - Sum, Count, Hash, Set, Max, Min...

2. **窗口何時合法？**
   - 大小限制、條件限制、目標達成...

3. **如何高效更新狀態？**
   - 增量更新、Rolling Hash、單調隊列、狀態追蹤...

### 從 O(n²) 到 O(n) 的本質

**樸素枚舉：**
```python
for i in range(n):
    for j in range(i, n):
        if condition(nums[i:j+1]):
            ans = update(ans, nums[i:j+1])
```
時間：O(n²)，每次都重新計算 `condition` 和 `update`

**Sliding Window：**
```python
left = 0
state = init_state()

for right in range(n):
    state.add(nums[right])  # 增量更新
    
    while not state.is_valid():
        state.remove(nums[left])
        left += 1
    
    ans = update(ans, state)
```
時間：O(n)，每個元素最多被加入/移除一次

---

## 參考題目清單

| 題目 | 類型 | 核心技巧 |
|-----|-----|---------|
| Contains Duplicate II | 固定窗口 | Set 控制窗口大小 |
| Maximum Average Subarray I | 固定窗口 | 簡單滑動求和 |
| Sliding Window Maximum | 固定窗口 | 單調隊列 |
| Repeated DNA Sequences | 固定窗口 | Rolling Hash |
| Longest Substring Without Repeating Characters | 可變窗口（最長） | HashMap + while 收縮 |
| Longest Repeating Character Replacement | 可變窗口（最長） | if 收縮 + 歷史最大頻率 |
| Fruit Into Baskets | 可變窗口（最長） | 最多 K 種元素模板 |
| Minimum Size Subarray Sum | 可變窗口（最短） | while 收縮到最小 |
| Minimum Window Substring | 可變窗口（最短） | 狀態追蹤 |
| Frequency of Most Frequent Element | 可變窗口（最長） | 預處理排序 |
| Diet Plan Performance | 固定窗口 | 滑動計數 |

---

**下一步建議：**
- 重點掌握"單調隊列"和"Rolling Hash"，這兩個是最難但最強大的技巧
- 理解"最長用 if，最短用 while"的本質原因
- 練習識別何時需要預處理（排序/編碼）
- 熟練使用狀態追蹤變量，避免重覆計算

