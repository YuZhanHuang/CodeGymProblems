## Sliding Window Overview

### 為什麼會需要 Sliding Window？

在 array / string 上，所有 **連續子序列**（subarray/substring）的數量是：

* 對每個結尾 `i`，令 `E_i = 所有以 i 結尾的 subarray`
* 則 `|E_i| = i + 1`
* 所以總數量為 `Σ(i+1) = n(n+1)/2`

因此，很多「要在連續區間上找某種答案」的題目，若直接枚舉所有 subarray，時間通常是 **O(n²)**。

Sliding Window 的目的：
**在連續區間上做查找/最優化/計數時，用兩個指標維持一個區間，讓每個元素最多被加入/移除一次，從 O(n²) 降到 O(n)（攤銷）。**

### 什麼時候用 Sliding Window？

只要題目關鍵字像這些就要想到它：

* 「subarray / substring」
* 「連續」
* 「最長 / 最短」
* 「滿足條件的區間」
* 「計數：有多少個區間符合條件」
* 常見條件：不重複、總和 <= / >=、至多 K 個不同元素、最多 K 次替換、等等


### Sliding Window 的核心操作

用 `(left, right)` 表示目前的 window `[left, right]`：

* `right` 往右擴張：把新元素納入 window，更新狀態（hash map / counter / sum / max...）
* 若 window 不符合條件：移動 `left` 收縮，並同步更新狀態
* 在過程中更新答案（最長/最短/計數/最大值…）

關鍵：**left 的移動條件要非常嚴謹**，並確保「狀態維護」與「邊界移動」一致。


## 常見程式碼模板

### 固定長度 window（size = w）

常見題：sliding window maximum、固定長度平均值、固定長度的某種統計

```python
from typing import List

def fixed_window(nums: List[int], w: int) -> int:
    n = len(nums)
    if w >= n:
        # 視題意：整段當一個 window
        w = n

    # init: 建立第一個 window 的狀態
    window_state = 0
    for i in range(w):
        window_state += nums[i]

    ans = window_state

    # slide: 每次右邊加一個、左邊減一個
    for right in range(w, n):
        left = right - w
        window_state += nums[right]
        window_state -= nums[left]
        ans = max(ans, window_state)  # 視題意更新
    return ans
```


### 可變長度 window：求「最長」(Longest)

常見題：Longest Substring Without Repeating Characters、最多 K 個不同字元、最多替換 K 次…

```python
from collections import defaultdict

def longest_window(s: str) -> int:
    count = defaultdict(int)   # window 狀態（視題意換成 set / dict / sum...）
    left = 0
    ans = 0

    for right, ch in enumerate(s):
        count[ch] += 1

        # 當 window 不合法時就收縮
        while count[ch] > 1:   # 範例：不允許重複
            count[s[left]] -= 1
            left += 1

        # window 合法時更新答案
        ans = max(ans, right - left + 1)

    return ans
```

---

### 可變長度 window：求「最短」(Shortest)

常見題：Minimum Size Subarray Sum、最短覆蓋子字串…

```python
def shortest_window(nums: List[int], target: int) -> int:
    left = 0
    window_sum = 0
    ans = float('inf')

    for right, x in enumerate(nums):
        window_sum += x

        # 只要符合條件就盡量縮小（找最短）
        while window_sum >= target:
            ans = min(ans, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if ans == float('inf') else ans
```

