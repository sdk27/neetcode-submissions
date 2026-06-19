
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.head=None
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied={}
        node=head
        if head is None:
            return None
        while node!=None:
            copied[node]=Node(node.val)
            node=node.next
        for key,value in copied.items():
            if key.random!=None:
                value.random=copied[key.random] 
            
        values=list(copied.values())
        for i in range(len(values)-1):
            values[i].next=values[i+1]
        return copied[head]


        
        
        
    

        
        
        
                
       
            

        

            
            


        