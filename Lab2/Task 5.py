matrix = [
    [2, 1, 5],
    [9, 2, 4],
    [7, 3 ,6]
       ]

max_value = matrix[0][0]
min_value = matrix[0][0]

for i in range(len(matrix)):  
     for j in range(len(matrix[i])):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_pos = (i, j)
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_pos = (i, j)

print(f"Максимальне значення: {max_value}, позиція: рядок {max_pos[0] + 1}, стовпець {max_pos[1] + 1}",
    f"\nМінімальне значення: {min_value}, позиція: рядок {min_pos[0] + 1}, стовпець {min_pos[1] + 1}")
