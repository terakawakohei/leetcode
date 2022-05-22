#first answer
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums) / 2):
            freq = nums[2 * i]
            val = nums[2 * i + 1]
            sublist = [val] * freq
            result.extend(sublist)
        return result
#second answer
class Solution
    def decomopressRLElist(self,nums:List[int])->List[int]:
        result=[]
        for i in range(0,len(nums),2):#range(start,stop,step)
            result+=[nums[i+1]]*nums[i]#リストを要素指定で初期化：list=[val]*num
        return result