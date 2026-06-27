# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=l1
        n2=l2
        sum=0
        number1=0
        number2=0
        power1=0
        power2=0
        while n1 is not None or n2 is not None:
            if n1 is not None:
                number1=number1+ n1.val*(10**power1)
                n1=n1.next
            if n2 is not None: 
                number2=number2+ n2.val*(10**power2)
                n2=n2.next
            power1+=1
            power2+=1

        print(number1)
        print(number2)
        sum=number1+number2
        total=sum
        node=ListNode(sum%10)
        answer=node
        sum=sum//10
        while sum!=0:
            node.next=ListNode(sum%10)
            sum=sum//10
            node=node.next
        return answer




        