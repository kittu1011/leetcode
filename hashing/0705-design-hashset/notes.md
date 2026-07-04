---
difficulty: Easy
pattern: direct hash
misclassified: N/A
guessed_pattern: direct hash
time_min: 8 mins
revisit: 2026-07-17
---

## Key signal I should have caught
Interviewer probably wants to see me implement some form of hashing, not just go straight to the optimization as that is kind of chaining. In real interview I should clarify if they want the hash to dynamically resize or not (as constraints are small).

## Brute force
Approach + complexity:
Just use a regular list without hashing keys to indicies. Add, delete, contains will all do linear searches
O(n) for each of the operations
## Optimized approach(es)

### 1. Map each key to single array of $10^6$ + 1 elements
**Complexity:** TC: O(1) SC: O($10^6$)
**Insight:** This works because the key is constrained to [0, $10^6$]

### 2. Use Linked list
**Complexity:** TC: O(N/10000) SC: O(10000)
**Insight:** Use seprate chaining and key % 10000. Made underly array size $10^4$ as that's max possible elements that can be in the hash set

## Mistakes made
Didn't know how to properly use dummy node in appr. 2. Made a mistake by comparing curr.val instead of curr.next.val when loop condition was `while curr`

## Time to solve
8 mins cold for solution 1 hint needed for solution 2

## Revisit
2026-07-17 do approach 2 cold