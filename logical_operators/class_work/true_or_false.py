# Define the truth of logical expressions:
# 2 <= 2 and 3 > 3 or 15 > 2
# 2 <= 2 and (3 > 3 or 15 > 2)
# 2 * x >= 2 and x <= 7 and (y < 0 or y > 5)
# (2 * x >= 2 and x <= 7 and y < 0) or y > 5


print((2 <= 2 and 3 > 3 or 15 > 2) == True)
print((2 <= 2 and (3 > 3 or 15 > 2)) == True)
x, y = 1, 0
print((2 * x >= 2 and x <= 7 and (y < 0 or y > 5)) == False)
print(((2 * x >= 2 and x <= 7 and y < 0) or (y > 5)) == False)
