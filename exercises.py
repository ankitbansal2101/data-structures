#hourglass problem #2d array
def hourglassSum(arr):
    sumlist=[]
    for i in range(0,4):
        for j in range(0,4):
            sum1=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            
            sumlist.append(sum1)
    print(max(sumlist))  
    return max(sumlist)  
        
hourglassSum([[9,8,7,6,5,6],[9,8,7,6,5,6],[9,8,7,6,5,6],[9,8,7,6,5,6],[9,8,7,6,5,6],[9,8,7,6,5,6]])





