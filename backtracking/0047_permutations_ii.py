# Original Sub-Optimal Solution using map
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        freq_map = dict(Counter(nums))

        def permute(i):
            if i == len(nums):
                result.append(path.copy())
                return
            for key in freq_map.items():
                print(key)
                if freq_map[key] == 0: # no more instances of key to use
                    continue
                freq_map[key] -= 1
                path.append(key)
                permute(i + 1)
                path.pop()
                freq_map[key] += 1

        permute(0)
        return result
# Optimal Solution
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        used = [False] * len(nums)

        def permute(i):
            if i == len(nums):
                result.append(path.copy())
                return
            for j in range(len(nums)):
                if used[j]:
                    continue
                # if nums[j] == nums[j-1] and not used[j-1] then nums[j-1] was already used before in a previous loop
                if j > 0 and nums[j] == nums[j-1] and not used[j-1]:
                    continue
                used[j] = True
                path.append(nums[j])
                permute(i + 1)
                path.pop()
                used[j] = False
        
        permute(0)
        return result
