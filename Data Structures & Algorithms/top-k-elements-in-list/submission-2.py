from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        most = count.most_common(k)

        res = []

        for num, freq in most:
            res.append(num)

        return res