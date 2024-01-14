import ctypes

class mylist:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make__array(self.size)

    def __make__array(self,size):
        return (size*ctypes.py_object)()

    def __len__(self):
        return self.n
    
    def __str__(self):
        s = ""
        for i in range(self.n):
            s += str(self.A[i])
            s += ","
        
        s = "[" + s[0:-1] + "]"
        return s
    
    def __delitem__(self,index):

        for i in range(0,self.n-1):
            if(i >= index):
                a = i+1
            else:
                a = i

            self.A[i] = self.A[a]
        
        self.n -= 1

            
    
    def __getitem__(self,index):
        if( self.n <= index or index <= -(self.n)):
            return "IndexError - Index is out of range :( "
        return self.A[index]
    
    def append(self,ele):
        if(self.size == self.n):
            self.A = self.__resize(self.size)
        
        self.A[self.n] = ele
        self.n += 1

    def insert(self,index,val):
        if(index > self.n):
            index = self.n
        
        B = self.__make__array(self.n+1)
        b = -1
        for i in range(self.n+1):
            if(i == index):
                B[i] = val
            else:
                b+=1
                B[i] = self.A[b]
        
        self.A = B
        self.size += 1
        self.n += 1
        return None

    
    def pop(self,index = 0):
        if (self.n == 0):
            print("EmptyListError : No item in list to pop ")
            return 

        self.n -= 1

    def index(self,val):
        for i in range(0,self.n):
            if(self.A[i] == val):
                return i
        return f"ValueError : No value in the list matching \"{val}\""

    def remove(self,val):
        for i in range(self.n):
            if(self.A[i] == val):
                self.__delitem__(i)
                return
            
        return None

    def __resize(self,size):
    
        B = self.__make__array(size+2)
        self.size = size+2
        for i in range(self.n):
            B[i] = self.A[i]
        
        return B
            
        
l = mylist()
l.append(1)
l.append(2)
l.append(3)
l.insert(2,100)
print(l)
l.append(4)
l.insert(2,"HEy")
del l[5]
print(l)