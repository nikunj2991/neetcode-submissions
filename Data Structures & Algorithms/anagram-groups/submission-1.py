class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return result

        """
            map = {
                key = []
            }
        """
        map = defaultdict(list)

        for str in strs:
            # sortedStr = "".join(sorted(str))

            key = [0] * 26
            for char in str:
                key[ord(char) - ord('a')] += 1
            
            map[tuple(key)].append(str)
            
            """
            if sortedStr in map: # is anagram
                map[sortedStr].append(str)
            else: # first of its kind
                map[sortedStr] = [str]
            """
        
        return list(map.values())





