class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0

        for i, height in enumerate(heights + [0]):
            start = i

            while stack and stack[-1][1] > height:
                start_index, old_height = stack.pop()
                area = old_height * (i - start_index)
                largest = max(largest, area)
                start = start_index

            stack.append((start, height))

        return largest
        