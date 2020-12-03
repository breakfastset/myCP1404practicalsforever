numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])          # 3
print(numbers[-1])         # 2
print(numbers[3])          # 1
numbers[:-1]        # [3, 1, 4, 1, 5, 9]
numbers[3:4]        # [1]
5 in numbers        # True
7 in numbers        # False
"3" in numbers      # False   "3" is not 3   string "3" is not integer 3
numbers + [6, 5, 3] # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]