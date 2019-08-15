class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        circle_times = length//2
        for circle_time in range(circle_times):
            times = length - circle_time * 2
            for i in range(times-1):
                tmp = matrix[circle_time][i+circle_time]
                matrix[circle_time][i + circle_time] = matrix[times-i-1 + circle_time][circle_time]
                matrix[times - i - 1 + circle_time][circle_time] = matrix[times-1 +circle_time][times - i - 1+circle_time]
                matrix[times - 1 + circle_time][times - i - 1 + circle_time] = matrix[circle_time+i][times-1+circle_time]
                matrix[circle_time + i][times - 1 + circle_time] = tmp
        return matrix



matrix =[
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13,3, 6, 7],
        [15,14,12,16]]

for i in Solution().rotate(matrix):
    print i
