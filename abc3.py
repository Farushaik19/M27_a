##str=input()
##k=""
##j=""
##for i in str:
##    if i not in k:
##        k+=i
##    else:
##        j+=i
##for l in j:
##    if l in k:
##        k=k.replace(l,"")
##    else:
##        pass
##print(k)

##str=input()
##k=""
##if len(str)==26:
##    for i in str:
##        if i not in k:
##            k+=i
##        else:
##            print("no")
##        if len(k)==26:
##            print("yes")
##else:
##    print("no")


##list=[1,2,3,4,5,6,7,8]
##print(list.pop())

##from collections import deque
##q=deque()
##q.append('t')
##q.append('a')
##q.append('l')
##q.append('e')
##q.append('n')
##q.append('t')
##print(q.popleft())
##print(q.popleft())
##print(q.popleft())
##print(q)

##class Phone:
##    def __init__(self):
##        pass
##    def searchitems(self,items,key):
##        for i in range(0,len(items)):
##            if items[i]==key:
##                return i
##list=['iphone','samsung','vivo','realme']
##key='vivo'
##objref=Phone()
##res=objref.searchitems(list,key)
##if(res==None):
##    print('Not Found')
##else:
##    print('found')
##
##class emp:
##    def __init__(self):
##        self.__num=100
##    def show(self):
##        print("parent:",self.__nun)
##class child(emp):
##    def __init__(self):
##        self.__var=10
##    def show(Self):
##        self.show()
##        print("child:",self.__var)

##a=[12,25,63,48,71,10]
##max=a[0]
##for i in range(1,len(a)):
##    if a[i]>max:
##        max-a[i]
##        m=i
##print(m)

list("p#q#r#s".split('#'))
print(list)
