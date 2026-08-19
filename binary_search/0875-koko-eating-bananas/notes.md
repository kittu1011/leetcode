---
difficulty: Medium
pattern: Binary Search
misclassified: No
guessed_pattern: Binary Search
time_min: 16
revisit: 10/3/2026
---

## Key signal I should have caught
**Invariant maintained throughout the loop:**

- The search space looks like: `F F F F T T T T` — infeasible speeds, then feasible speeds, split at the answer `k*`.
- Everything strictly **left of `l`** is proven `F` (infeasible).
- Everything strictly **right of `r`** is proven `T` (feasible).
- The unknown region is always `[l, r]`.

**Why `l` ends up at `k*`:**

- If `mid` is `F` → `l = mid + 1` (mid and everything below it is now proven `F`).
- If `mid` is `T` → `r = mid - 1` (mid *might* be `k*`, so `l` is never pushed past it).
- Each step shrinks `[l, r]` while preserving the invariant — `l` never crosses into `T` territory, `r` never crosses into `F` territory.
- Loop ends when `l > r`, i.e. the unknown region is empty.
- At that point: position `l - 1` is `F`, position `l` is `T` → `l` sits exactly on the first `T`, which is `k*`.

## Brute force
Approach + complexity: Test every possible `k` starting from $1$ return the first one
TC: $O(N*\max(piles))$ SC: $O(1)$

## Optimized approach(es)

### 1. Binary Search
**Complexity:** TC: $O(N\log \max(piles))$ SC: $O(1)$
**Insight:** Use binary search to find smallest feasible `k` in $[1,\max(piles)]$

## Mistakes made
No need to run `helper` function twice

## Time to solve
16 min cold

## Revisit
Solve it optimally first time cold. Remember why `l` will end up at the final answer
