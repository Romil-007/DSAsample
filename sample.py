
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

    
class Linkedlist:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
    def head_insert(self,val):
        new = Node(val)
        new.next = self.head
        self.head = new
        self.n += 1
    
    def append(self,val):    
        new = Node(val)

        if(self.n == 0):
            self.head = new
            self.head.next = None
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next =  new

        self.n += 1

    def clear(self):
        self.__init__()

    def insert(self,search,val):
        curr = self.head
        if(self.head == None):
            print("Empty linked list Error")
            return
        
        while curr.data != search:
            curr = curr.next
            if(curr.next == None):
                if(curr.data != search):
                    print(f"ERROR NO DATA FOUND FOR ELEMENT {search} :(")
                    return
                else:
                    break


        new = Node(val)
        new.next = curr.next
        curr.next = new

        self.n += 1
        
        


    def __str__(self):
        s = ""
        curr = self.head
        if(curr == None):
            s += "Emty Linked list as of now"
            return s
        while curr!=None:
            s+=str(curr.data) + " -> "
            curr = curr.next
        
        
        return s[:-3]

a = Linkedlist()
a.head_insert(10)
a.head_insert(20)
a.head_insert(30)
a.append(0)
a.append(0)
a.insert(0,100)
print((a))
