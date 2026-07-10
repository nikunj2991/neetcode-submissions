class Solution:
    def countStudents(self, q: List[int], sandwiches: List[int]) -> int:


        
        res = len(q)

        for sandwich in sandwiches:
            count = 0
            n = len(q)
            while count < n and q[0] != sandwich:
                curr = q.pop(0)
                q.append(curr)
                count += 1
            
            if q[0] == sandwich:
                q.pop(0)
                res -= 1
            else:  
                break
        
        return res
