class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = list(students)
        
        res = n

        for sandwich in sandwiches:
            count = 0
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
