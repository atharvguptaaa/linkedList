class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get_length(self):
        count =0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
            return
        itr=self.head
       
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)
        
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("invalid input")
    
        if index==0:
            node=Node(data,self.head)
            self.head=node
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data, itr.next)
                itr.next=node
                break
            count+=1
            itr=itr.next

    def remove_at(self, index):
            if index<0 or index>=self.get_length():
                raise Exception("invalid index")
            
            if index==0:
                self.head=self.head.next
                return
            
            count=0
            itr=self.head
            while itr:
                if count==index-1:
                    itr.next=itr.next.next
                    break
                count+=1
                itr=itr.next

    def insert_values(self,values):
        self.head=None
        for i in values:
            self.insert_at_end(i)

    def remove_by_val(self,value):
        itr=self.head 
        count=0
        while itr:
            if value==itr.data:
                self.remove_at(count)
                return
             
            count+=1
            itr=itr.next 

        raise Exception("invalid value")          
    

    def insert_after_value(self, afterval, value):
        itr=self.head
        count=0
        while itr:
            if afterval==itr.data:
                node=Node(value, itr.next)
                itr.next=node
                return
            count+=1
            itr=itr.next
        
        raise Exception("invalid value")

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(60)
    ll.insert_at_end(7)
    ll.insert_at(0,3)
    ll.insert_at(4,30)
    ll.remove_at(3)
    #ll.insert_values([1,2,3,4,5,6,7])
    #ll.remove_by_val(6)
    #ll.insert_after_value(60,65)

    print(ll.get_length())
    ll.print()