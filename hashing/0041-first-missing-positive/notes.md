---
difficulty: Hard
pattern: In-place Hashing
misclassified: N/A
guessed_pattern: External Hashing
time_min: 35
revisit: 9/12/2026
---

## Key signal I should have caught
Sometimes you can substitiute input array itself as the hash table. Especially, if the hash is boolean array or same size as the input

## Brute force
Approach + complexity: Iterate starting at 1 check if it's in array, then 2, 3, 4, etc. Return first number not in array TC: $O(N^2)$ SC: $O(1)$

## Optimized approach(es)

### 1. Negative Marking
**Complexity:** TC: $O(N)$ SC: $O(1)$
**Insight:** Have the sign of an element in array correspond to weather element i + 1 is in the input
### 2. Cycle Sort
**Complexity:** TC: $O(N)$ SC: $O(1)$
**Insight:** Place an element at it's correct index in the hash by swapping it with what's already at the index
### 3. Hash Set
**Complexity:** TC: $O(N)$ SC: $O(N)$
**Insight:** Hash all the elements in the array. Iterate starting from 1 all the way to N and return first number not in the set

## Mistakes made
Not trying to build off the brute force approach more. Brute force leads to solution 3 which then leads to 1&2. Weather I would come up with the trick in 1 or 2 cold is another story

## Time to solve
35 min with solution hint

## Revisit