def maximumValueSum(nums, k, edges):
        s=sum(nums)
        # for i in range(5):
        #     tem=nums[:]
        #     tem[0]=2
        #     tem[2]=2
        #     print(nums, tem)
        #     tem=[]
        print('nums: ',nums,'sum: ',s)
        for i,j in edges:
            print('i: ',i,'j: ',j)
            tem=nums[:]
            tsum=0
            tem[i]=tem[i]^k
            tem[j]=tem[j]^k
            print('stsrt tem:',tem)
            for i in tem:
                tsum+=i
            print('tsum: ',tsum,'sum: ', s)
            if tsum>s:
                s=tsum
            tem=[]
        return s

print(maximumValueSum([24,78,1,97,44],6,[[0,2],[1,2],[4,2],[3,4]]))