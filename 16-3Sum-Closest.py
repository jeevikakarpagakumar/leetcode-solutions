class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result= nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j=i+1
            k= len(nums)-1
            while j<k:
                sum= nums[i]+nums[k]+nums[j]
                if sum==target:
                    return sum
                if abs(sum-target)<abs(result-target):
                    result= sum
                if sum<target:
                    j+=1
                else:
                    k-=1
        return result
        