"""
Задача №2
Дана двовимірна матриця розміром 𝑛×𝑚, що складається з 0 і 1.
Знайти площу найбільшого прямокутника, який складається тільки з 1.
Автор: Мотовилець Марія 31І групa
"""
matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

if not matrix:
    max_area = 0
else:
    max_area = 0
    heights = [0] * len(matrix[0])

    for row in matrix:
        for i in range(len(row)):
            if row[i] == 0:
                heights[i] = 0
            else:
                heights[i] += row[i]

        stack = []
        curr_max_area = 0
        idx = 0

        while idx < len(heights):
            if not stack or heights[idx] >= heights[stack[-1]]:
                stack.append(idx)
                idx += 1
            else:
                top = stack.pop()
                area = (heights[top] * 
                        ((idx - stack[-1] - 1) if stack else idx))
                curr_max_area = max(curr_max_area, area)

        while stack:
            top = stack.pop()
            area = (heights[top] * 
                    ((idx - stack[-1] - 1) if stack else idx))
            curr_max_area = max(curr_max_area, area)

        max_area = max(max_area, curr_max_area)
print("Максимальна площа прямокутника з одиниць:", max_area)
