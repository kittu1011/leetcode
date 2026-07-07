---
difficulty: Easy
pattern: Pointers
misclassified:
guessed_pattern:
time_min: 7
revisit: 9/3/2026
---

## Key signal I should have caught
In recurisve appr 2. head.next.next will hold the tail of the reverse linked list

## Brute force
Approach + complexity: iterate through linked list, store values in array and create a new linked list by iterating through the array backwards
TC: $O(N)$ SC: $O(N)$

## Optimized approach(es)

### 1. Iteration
**Complexity:** $O(N)$ SC: $O(1)$
**Insight:** Initialize prev to None and manipulate pointers
### 1. Recursion
**Complexity:** $O(N)$ SC: $O(N)$
**Insight:** head.next.next will hold tail of the newly reversed list

## Mistakes made
In recursive approach I tried to have the function return the tail of the linked list, which just overcomplicated the syntax

## Time to solve
7 min cold for appr. 1 
5 min for appr. 2 with hint 
## Revisit