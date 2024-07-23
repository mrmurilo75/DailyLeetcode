class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Build a hashtable of counts - O(n), 
            then sort it into an array of pairs by frequency and order (on colisions) - O(nlogn) using std lib,
            lastly we build the resulting array O(n).
        Time complexity: O(2n + nlogn) = O(nlogn)
        Space complexity: O(3n) = O(n)
        """
        
        # count number of frequencies
        count = dict()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
        # sort colisions in decreasing order
        result = sorted(
            count.items(),
            key=(lambda x: (x[1], -x[0])),
        )
        
        # build solution
        build = []
        for x, y in result:
            build += [x]*y
            
        return build

