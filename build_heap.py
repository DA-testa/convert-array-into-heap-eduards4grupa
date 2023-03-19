# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n=len(data)
    for i in range (n//2,-1,-1):
        minHeapify(array, size, k)
    return swaps

def minHeapify(data, i, n):
    n=len(data)
    samllest = i
    leftChild = 2*k + 1
    rightChild = 2*k + 2
  
    if leftChild < n and data[leftChild] < data[smallest]:
        smallest = leftChild
    if rightChild < n and data[rightChild]<data[smallest]:
       smallest = rightChild
    if smallest != i:
        swaps.append((i, smallest))
        data[i], data[smallest]=data[smallest], data[i]
        minHeapify(data, i ,n)
  

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
        with open ('./tests/',filename,"r") as f:
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
