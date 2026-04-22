class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outer_map = {}
        for string in strs:
            count_map = {}
            for char in string:
                if char not in count_map:
                    count_map[char] = 1
                else:
                    count_map[char] += 1
            key = tuple(sorted(count_map.items()))
            if key not in outer_map:
                outer_map[key] = []
            outer_map[key].append(string)
        return list(outer_map.values())

            

        