---
description: Strong-hire 乾跑：用不變量驗證使用者解法（事件驅動、一般性正確性、含複雜度與抓 bug），並控制篇幅避免 token 膨脹
globs:
  - "**/*.py"
  - "**/*.md"
alwaysApply: false
---

# Strong-Hire Dry Run Protocol（僅在使用者要求乾跑/驗證解法時套用）

## 觸發條件
當使用者提供「題目 + 解法」並要求 dry run / correctness / complexity / 驗證正確性 / 找 bug 時，必須遵守本規則。
若使用者不是在要求乾跑或驗證解法，請不要強制使用此格式。

## 篇幅控制（省 token：強制）
- Representative Testcases：2–3 組為預設（除非使用者指定更多）。
- Event-driven Dry Run：
  - 每個 testcase 最多 **6 個事件**（必要時可到 8，但要有理由）。
  - 每個事件的 state_snapshot 最多 **5 個欄位**（只保留關鍵狀態）。
- 禁止輸出完整資料結構 dump：完整 heap、完整 dp 表、完整鄰接邊清單、完整 window 逐字追蹤。
  - 若需要，只能列「局部」：例如 heap top、被 relax 的那條邊、dp 的某一列/某幾格、window 的關鍵計數等。
- 禁止逐行逐迭代唸程式。只講轉折事件（turning points）。

---

## 輸出格式（固定順序；標題不可省略）
1) Spec Checkpoints
2) State Semantics
3) Invariants
4) Representative Testcases
5) Event-driven Dry Run
6) Correctness Argument
7) Complexity
8) Bugs / Fixes (if any)

---

## 1) Spec Checkpoints（2–5 點，可檢核）
- 用 2–5 點把題目轉成「可驗證條件」：
  - 功能正確（包含重複需求/計數/限制）
  - 最優性（最短/最小/最大）若題目要求
  - 無解與邊界輸入的行為（若適用）
- 不要只是重述題目句子；要能被反例推翻的那種條件。

---

## 2) State Semantics（列出核心狀態與語意）
列出核心變數/資料結構（通常 3–8 個即可），每個都要：
- meaning：它代表什麼（語意）
- updates：什麼情況會更新它（新增/移除/比較/回溯/鬆弛等）

---

## 3) Invariants（至少 1 個 main；可 0–2 個 aux）
- 必須至少提出 1 個 **Main invariant**（直接支撐 correctness）。
- 可選 0–2 個 **Aux invariants**（支撐最優/不漏/終止/攤提）。
- 每個 invariant 必須包含三段式（簡短即可）：
  - init：為何初始成立
  - preserve：每次更新後為何仍成立
  - use：何時/如何用它推出規格成立（或最優/完備/終止）

> Invariant 必須可檢核（能對上某個狀態），禁止空泛語句。

---

## 4) Representative Testcases（2–3 組，目的導向）
- 每個 testcase 必須標註 purpose：
  - normal_turning_point：能觸發核心轉折（例如第一次合法、第一次更新最優、第一次 finalize 等）
  - edge_case：邊界（空、單元素、極小、t>s 等）
  - risk_point：重複需求、權重、去重、分支/剪枝等常見出錯點
  - no_solution：明確無解（若題目允許）
- testcase 不求多；求能覆蓋「最容易出錯」與「核心轉折」。

---

## 5) Event-driven Dry Run（只追 turning points）
### Turning points 的通用定義（最重要）
只記錄會改變下列任一項的事件：
- validity/可行性（合法↔不合法、約束滿足↔不滿足）
- best/答案候選（更新最優解）
- 核心狀態類別切換（例如：節點被 finalize、顏色改變、dp cell 被確定、遞迴返回、剪枝觸發）
- 進度與終止（指標/層級/子問題規模確實前進）

### 每個事件必須包含（簡短、固定欄位）
- trigger：事件是什麼（例如：加入元素、移除元素、pop、relax 成功、dp 轉移、enter/return/prune）
- state_snapshot：只列必要欄位（<= 5 個）
- invariant_alignment：一句話說明不變量仍成立 / 或指出在此處即將被破壞
- answer_update（若有）：did_update + why_valid（為何此刻可更新）+ new_answer（可省略細節）

### Examples（僅為例子，不要求列舉全部）
- sliding window：valid 變化、答案更新、收縮停點
- graph：pop、relax 成功、狀態/顏色變更、union 成功/失敗
- DP：base、某格候選比較、依賴已就緒
- recursion/backtracking：enter/return、choose→recurse→unchoose(restore)、prune、record solution

---

## 6) Correctness Argument（一般性，用 invariants 串起來）
必須包含三段（每段 1–3 句即可）：
- Safety/Validity：為何過程不會違反規格（用 invariant）
- Optimality 或 Completeness：為何最優 / 不漏不重（視題型）
- Termination/Progress：為何會停（單調指標/子問題規模下降/有限狀態）

附註（必要時才提）：
- DP：state 定義 + 轉移完整性 + fill order +（口頭版）歸納
- Dijkstra：需聲明非負權前提，並說明 finalize 合理性

---

## 7) Complexity（time/space + why）
- Time：Big-O + 為什麼（用“總次數”角度，例如指標最多走 m 次、每條邊 relax 次數、每格 dp 計算成本）
- Space：Big-O + 主要來源（表格/圖/遞迴深度/哈希表）
- 若有攤提（amortized），用 1 句話說明攤提理由。

---

## 8) Bugs / Fixes（若有）
若發現違反 spec 或 invariant：
1) earliest_failure_point：最早失效點（指出具體語句/步驟）
2) minimal_counterexample：最小反例
3) minimal_fix：最小 diff 修正（prefer minimal）
4) why_fix_works：修正後 invariant 如何恢復並滿足 spec

若未發現問題：簡短列出「在以下假設下未發現問題」與假設清單。
