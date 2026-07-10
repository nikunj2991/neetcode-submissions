class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        sum = 0
        for operation in operations:
            match operation:
                case "+":
                    top = len(score) - 1
                    val = score[top] + score[top - 1]
                    score.append(val)
                    sum += val
                case "C":
                    val = score.pop()
                    sum -= val
                case "D":
                    top = len(score) - 1
                    val = 2 * score[top]
                    score.append(val)
                    sum += val
                case _:
                    val = int(operation)
                    score.append(val)
                    sum += val

        return sum