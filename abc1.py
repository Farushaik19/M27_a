##from collections import deque
##q=deque()
##q.append('t')
##q.append('a')
##q.append('l')
##q.append('e')
##q.append('n')
##q.append('t')
##q.popleft()
##print(q)

##class Value:
##    def __init__(self,a,b):
##        self.a=a
##        self.__b=b
##    def update_value(self,c):
##        if c<200 and c>0:
##            self.__b*=c
##        def show_value(self):
##            print("he value is ",self.__b)
##obj1=Value(5,20)
##print(obj1.__b)
##class Test:
##     def method1(self):
##         print("method1")
##     def method2(self):
##         self.method1()
##         print("method2")
##Test().method2()

##import queue
##q=queue.Queue()
##q.put("anil")
##q.put("sunil")
##q.put("Adil")
##q.put("haneef")
##list1=[]
##for i in range(q.qsize()):
##    t=q.get()
##    if t=="adil":
##        print("move away from queue")
##        break
####print(t)


##from multiprocessing import Queue
##que=Queue()
##que.put('led')
##que.put('iphone')
##que.put('Ac')
##print(que.get())
##print(que.get())
##print(que.get())
##

##a=[10,20,30,40,50,60]
##for i in range(1,6):
##    a[i-1]=a[i]
##for i in range(0,6):
##    print(a[i],end=" ")
##
##class Fav:
##    def__init__(self):
##        self.title=None
##obj=Fav()
##obj.title="pyhton programming"
##obj1=fav()
##obj1.title="learn python the hard way"
##obj.title="laerning pyhton"
##print("favouriye is",obj.title)
##print("second favourite is",obj1.title)


##s=input()
##a=input()
##str=""
##for i in s:
##    if i in a:                ###printing the similar substring in both the strings
##        str=str+i
##if len(str)==0:
##    print("-1")
##else:
##    print(str)
##        

##s1,s2=input().split()
##if len(s1)<=len(s2):
##    n=len(S1)                  ###printing two strings side by side with 
##else:                             equal no of chracters from both the srings 
##    n=len(s2)
##print(s1[:n:],end="")
##print(s2[:n:])
