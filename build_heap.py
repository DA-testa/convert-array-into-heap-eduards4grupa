# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n=len(data)
    for i in range (n//2,-1,-1):
        minHeapify(array, size, k)
    return swaps

def minHeapify(array, size, k):
    n=len(data)
    set k as smallest
    leftChild = 2*k + 1
    rightChild = 2*k + 2
  
    if leftChild < n and array[leftChild] < array[smallest]:
        set leftChildIndex as smallest
    if rightChild < n and array[rightChild]<array[smallest]:
        set rightChildIndex as smallest
        
  

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    iof = input()
    
    if iof = "I":
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    if iof = "F":
        filename=input()
        with open ('./tests/'filename,"r") as f:
            read=int(f.read()) 
            data = list(map(int, input().split()))
        
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

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
