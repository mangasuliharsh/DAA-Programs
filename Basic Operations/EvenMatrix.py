def even(matrix):
    for row in matrix:
        for num in row:
            if (num % 2 == 0):
                print(num)

def main():
    matrix = [[1,2,3,4,5,6],
             [7,8,9,10,11,12]]
    even(matrix)

main()
