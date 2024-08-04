def binary_to_decimal(decimal):
    if decimal == 0:
        return 0
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def main():
    decimal = int(input("Enter the Decimal Number"))
    result = binary_to_decimal(decimal)
    print(f"Binary Equivalent of {decimal} is {result}")

main()
