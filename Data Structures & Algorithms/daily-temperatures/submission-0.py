class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        helper_stack = []
        for i, n in enumerate(temperatures):
            while helper_stack and n > helper_stack[-1][1]:
                temp = helper_stack.pop()
                result[temp[0]] = i - temp[0]
            helper_stack.append([i, n])

        return result
        