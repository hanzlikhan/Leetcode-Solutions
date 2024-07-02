class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = self.findpivot(nums, n)
        if target >= nums[pivot] and target <= nums[n - 1]:
            return self.binarySearch(nums, pivot, n - 1, target)
        else:
            return self.binarySearch(nums, 0, pivot - 1, target)

    def findpivot(self, arr: List[int], n: int) -> int:
        s, e = 0, n - 1
        while s < e:
            mid = s + (e - s) // 2
            if arr[mid] > arr[e]:
                s = mid + 1
            else:
                e = mid
        return s

    def binarySearch(self, arr: List[int], s: int, e: int, key: int) -> int:
        while s <= e:
            mid = s + (e - s) // 2
            if arr[mid] == key:
                return mid
            if key > arr[mid]:
                s = mid + 1
            else:
                e = mid - 1
        return -1

# Example usage
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0
# solution = Solution()
# result = solution.search(nums, target)
# print(result)  # Output: 4
