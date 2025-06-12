class a:
    def __init__(self,a):
        self.a = a

    
    def __eq__(self, o):
        return self.a - o.a
    
obj1 = a(1)
obj2 = a(2)


print(obj2 == obj1)