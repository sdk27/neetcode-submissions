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
        multiplier1=1
        multiplier2=1
        while n1 is not None or n2 is not None:
            if n1 is not None:
                number1=number1+ n1.val* multiplier1 
                multiplier1=multiplier1*10
                n1=n1.next
            if n2 is not None: 
                number2=number2+ n2.val* multiplier2
                multiplier2=multiplier2*10
                n2=n2.next
            

        print(number1)
        print(number2)
        sum=number1+number2
        node=ListNode(sum%10)
        answer=node
        sum=sum//10
        while sum!=0:
            node.next=ListNode(sum%10)
            sum=sum//10
            node=node.next
        return answer




        