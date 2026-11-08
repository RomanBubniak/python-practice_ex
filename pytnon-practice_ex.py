numbers = [5, -10, 0, -3, 8, 1, -15, 1, 2, 311121221212]
quant = 0
quant1 = 0
for i in numbers:
    if i > 0:
        quant += 1
    elif i == 0:
        pass
    else:
        quant1 += 1
print(f"the number of positive numbers: {quant}")
print(f"the number of negative numbers: {quant1}")