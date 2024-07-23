class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Build a hashtable of counts - O(n),
            then sort the input array by frequency and order - O(nlogn) using std lib.
        Time complexity: O(n + nlogn) = O(nlogn)
        Space complexity: O(2n) = O(n)
        """

        # count number of frequencies
        count = dict()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # sort by frequency and order
        nums.sort(key=lambda x: (count[x], -x))
        return nums
