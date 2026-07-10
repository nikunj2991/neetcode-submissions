class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        if not strs:
            return result

        """
            map = {
                key = []
            }
        """
        map = {}

        for str in strs:
            sortedStr = "".join(sorted(str))
            
            if sortedStr in map: # is anagram
                map[sortedStr].append(str)
            else: # first of its kind
                map[sortedStr] = [str]
            
        for key in map.keys():
            result.append(map[key])
        
        return result





