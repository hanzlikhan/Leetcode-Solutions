class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int pivot = findpivot(nums, n);
        if (target >= nums[pivot] && target <= nums[n - 1]) {
            return binarySearch(nums, pivot, n - 1, target);
        } else {
            return binarySearch(nums, 0, pivot - 1, target);
        }
    }

    int findpivot(vector<int>& arr, int n) {
        int s = 0;
        int e = n - 1;
        while (s < e) {
            int mid = s + (e - s) / 2;
            if (arr[mid] > arr[e]) {
                s = mid + 1;
            } else {
                e = mid;
            }
        }
        return s;
    }

    int binarySearch(vector<int>& arr, int s, int e, int key) {
        while (s <= e) {
            int mid = s + (e - s) / 2;
            if (arr[mid] == key) {
                return mid;
            }
            if (key > arr[mid]) {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        return -1;
    }
};