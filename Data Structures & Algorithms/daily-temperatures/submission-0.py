class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        stack = []

        for today in range(len(temperatures)):
            while stack and temperatures[today] > temperatures[stack[-1]]:
                waiting_day = stack.pop()
                answer[waiting_day] = today - waiting_day

            stack.append(today)

        return answer
        