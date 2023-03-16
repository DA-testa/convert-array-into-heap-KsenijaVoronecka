# python3 build_heap.py
# Ksenija Voronecka RDCP0
import math

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    i = math.floor((len(data) - 2) / 2)

    def change_places(i, length):
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2

        smallestNumber = i

        if leftChild < length and data[leftChild] < data[i]:
            smallestNumber = leftChild
        
        if rightChild < length and data[rightChild] < data[smallestNumber]:
            smallestNumber = rightChild
        
        if smallestNumber != i:
            (data[i], data[smallestNumber]) = [data[smallestNumber], data[i]]
            swaps.append([i, smallestNumber])
            change_places(smallestNumber, length)
    
    while i >= 0:
        change_places(i, len(data))
        i -= 1

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    command = input()

    if "I" in command:
        print("Enter a number of elements: ")
        # input number of elements
        elements_count = int(input())
        # input values in one variable
        print("Enter values: ")
        data = input()

    elif "F" in command:
        # let user input file name to use, don't allow file names with letter a
        print("Enter the file name: ")
        fileName = input()

        if "a" in fileName:
            print("wrong file name")
            return
        
        filePath = "./tests/" + fileName
        with open(filePath, mode="r") as fail:
            # input number of elements
            elements_count = int(fail.readline())
            # input values in one variable
            data = fail.readline()

    else:
        print("error")
        return


    # input from keyboard
    data = list(map(int, data.split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == elements_count

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()