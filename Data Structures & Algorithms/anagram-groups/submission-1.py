class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        hashmap = {}

        for word in strs:
            key = ''.join(sorted(word))

            hashmap.setdefault(key, []).append(word)

        return list(hashmap.values())