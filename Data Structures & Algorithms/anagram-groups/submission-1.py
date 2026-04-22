class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(string)

        return list(groups.values())

            

        