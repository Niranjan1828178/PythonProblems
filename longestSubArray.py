# longest subarray with maximum bitwise AND operation
# Examples
# Input: nums = [1,2,3,3,2,2]
# Output: 2
# Explanation:
# The maximum possible bitwise AND of a subarray is 3.
# The longest subarray with that value is [3,3], so we return 2.

def longestSubarray(nums):
        a,c,k=max(nums),[0],0
        for i in range(nums.index(a),len(nums)):
            if a==nums[i]:
                c[k]+=1
            else:
                k+=1
                c.append(0)
        
        return max(c)

nums=list(map(int,input('enter elements of array seprated with comma: ').split(',')))

print('length of longest subarray with maximum bitwise AND operation:',longestSubarray(nums))