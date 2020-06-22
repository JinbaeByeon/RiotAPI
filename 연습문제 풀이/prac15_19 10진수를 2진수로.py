def decimalToBinary(value):
    if value == 0:
        return ""
    else:
        return decimalToBinary(value//2) + str(value%2)

print(decimalToBinary(38))
