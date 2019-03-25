'''
#1、Two sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                    break

solution=Solution()
print(solution.twoSum([3,2,4],6))
'''
'''
#2、Add two numbers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r=[]
        n=[]
        if len(l1)==len(l2):
            print('nothing will be changed')
        elif len(l1)>len(l2):
            for i in range(len(l2),len(l1)):
                l2.append(0)
        else:
            for i in range(len(l1),len(l2)):
                l1.append(0)
        for i in range(0, len(l1)):
            m=l1[i]+l2[i]
            r.append(m)     #Obtain the r just by addition without other operation

        for i in range(0,len(r)-1):
            if r[i]>=10:
                r[i]%=10  #if the element is greater than 10, changing the element to its module by 10
                r[i+1]+=1   #And let the element in next position plus 1
        print(r)
        if r[-1]>=10:       #Check the last element in r
            r[-1]%=10
            r.append(1)
        return r

solu=Solution()
print(solu.addTwoNumbers([9],[9]))
print(solu.addTwoNumbers([2,5,6],[3,5,3]))
'''
'''
#3. Longest Substring Without Repeating Characters
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=[]
        count=[]
        #s.strip('')
        if s=='':
            print(0)
        else:
            for i in range(0,len(s)):
                if s[i] in a:  #判断字符是否在a中出现过
                    count.append(len(a))  #记录此时a中最长不带重复字符的个数，并把它存到count列表中
                    #a.clear()   #清空a，以便继续使用
                    del a[:a.index(s[i])+1]  #依次删掉a中字符从0-a中第一个等于s[i]的元素
                    #print(a)
                    a.append(s[i]) #将s[i]补充进a，以免漏掉元素
                    #print(a)
                else:
                    a.append(s[i])
                    #print(a)
            #print(count)
            if a[-1] == s[-1]:
                count.append(len(a))
            #print(count)
            print(max(count))  # 打印count中最大的数，即最长不带重复字符的个数
solu=Solution()
solu.lengthOfLongestSubstring('pwwkew')
'''
#4、Median of Two Sorted Arrays
'''
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        New_array=nums1+nums2 #组成新的列表
        print(New_array)
        New_array.sort()
        count=len(New_array)
        if count%2==0:
            median=(New_array[int(count/2)]+New_array[int(count/2-1)])/2
        else:
            median=New_array[int((count-1)/2)]
        print(median)
solu=Solution()
solu.findMedianSortedArrays([1,2],[3,4,5,6])

