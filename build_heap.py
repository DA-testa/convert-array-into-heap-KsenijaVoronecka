# python3 build_heap.py
import math

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    def changePlaces (data, i):
        print("yes")

        leftChild = 2*i+1
        if leftChild < len(data):
            if data[leftChild] < data[i]:
                (data[leftChild], data[i]) = [data[i], data[leftChild]]
                print("parent = ", i)
                print("2 = ", data)
                return swaps.append([i, leftChild]), changePlaces(data, i)

        rightChild = 2*i+2
        if rightChild < len(data):
            if data[rightChild] < data[i]:
                (data[rightChild], data[i]) = [data[i], data[rightChild]]
                print("parent = ", i)
                print("1 = ", data)
                return swaps.append([i, rightChild]), changePlaces(data, i)

        # leftChild = 2*i+1
        # if leftChild < len(data):
        #     if data[leftChild] < data[i]:
        #         (data[leftChild], data[i]) = [data[i], data[leftChild]]
        #         print("parent = ", i)
        #         print("2 = ", data)
        #         return swaps.append([i, leftChild]), changePlaces(data, i)

        if i != 0:
            parent = math.floor((i-1)/2)
            if data[parent] > data[i]:
                (data[i], data[parent]) = [data[parent], data[i]]
                print("parent = ", parent)
                print("3 = ", data)
                return swaps.append([parent, i]), changePlaces(data, parent)
        
        if i == len(data)-1:
            return
        
        changePlaces(data, i+1)


    # k = 0
    # for i in reversed(range(0, len(data))):
    #     print("i=", i)
    #     # swaps[k] = swaps.extend (changePlaces(data, i))
    #     changePlaces(data, i)
    #     # k+=1
    changePlaces(data, len(data)-1)
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
        
        filePath = "./test/" + fileName
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
