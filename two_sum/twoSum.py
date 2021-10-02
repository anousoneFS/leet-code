class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for id, j in enumerate(nums[i + 1 :]):
                if nums[i] + j == target:
                    return [i, id + i + 1]
        return None


if __name__ == "__main__":
    ob = Solution()
    print(ob.twoSum([4, 3, 4, 7], 11))
