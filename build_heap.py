# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n=len(data)
    for i in range (n//2,-1,-1):
        minHeapify(data, i, n,swaps)
    return swaps

def minHeapify(data, i, n,swaps):
    n=len(data)
    maz = i
    leftChild = 2*i + 1
    rightChild = 2*i + 2
  
    if leftChild < n and data[leftChild] < data[maz]:
        maz = leftChild
    if rightChild < n and data[rightChild]<data[maz]:
        maz = rightChild
    if maz != i:
        swaps.append((i, maz))
        data[i], data[maz]=data[maz], data[i]
        minHeapify(data, i ,n,swaps)
  

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    iof = input()
    
    if "I" in iof:
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    if "F" in iof:
        filename=input()
        with open (f"tests/{filename}") as f:
            n=int(f.readline()) 
            data = list(map(int, input().split()))
        
    # checks if lenght of data is the same as the said lenght
   

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
