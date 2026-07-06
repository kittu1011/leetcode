---
difficulty: Medium
pattern: hash map sroting
misclassified: No
guessed_pattern: N/A
time_min: 13 mins
revisit: 9/2/2026
---

## Key signal I should have caught
N/A

## Brute force
Approach + complexity: Initialize results set as `[[strs[0]]]` then check if the remaining strs can fit in any of the result groups. If not create a new one
TC: $O(S \cdot N^2)$ where S is size of longest string. SC: O(1) excluding final result

## Optimized approach(es)

### 1.
**Complexity:** TC: $O(N \cdot S \log(S))$ SC: $O(N)$
**Insight:** Sorting an anagram will always map to one string. This can be used as a key in a hash map

## Mistakes made
N/A

## Time to solve
13 min cold

## Revisit