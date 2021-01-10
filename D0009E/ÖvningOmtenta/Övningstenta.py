# UPG1 A)NEJ B)two C)[1,1,7] D)14,1 TOTALT:8P

#  UPG2 TOTAL 12P
# def min(lst):
#     e=lst[0]
#     i=0
#     while i<len(lst):
#         if lst[i]<e:
#           e=lst[i]
#         i=i+1
#     return e
# print(min([3,2,3,1,5]))

# UPG3 TOTALT:12P
# l1=[10,4,5]
# l2=[3,[1,2],5]
# l3=[10,4,5]
# def insert(lst1, lst2, p):     
#     if p>0:         
#         lst1[p:p] = lst2     
#     else:        
#         lst1 = lst2     
#     return lst1 
# l1 = [3,4,5] 
# l2 = insert(l1, [1,2], 1) 
# l1[0] = 10 
# l3 = insert(l2, [7,8], 0)
# print(l1,l2,l3)

# UPG4 TOTALT: 17P
# def findRev(s1,s2,n):
#     s =""
#     for c in s2:  
#         s = c+s
#     if s in s1:
#         print(s1.index(s))
#     else:
#         print(n)
# findRev("Fin sensommardag", "mos", 40) 

# UPG5 TOTALT: 19P
# def loadInt(fname):
#   try:
#       f=open(fname,"r")
#   except FileNorFoundError
#   try:
#       v=int(f.readline())
#   except ValueError:
#       raise exception
#   f.close()
#   return v
# 
# def example():
#   fname = input("Filnamn:")
#   try:
#       print(loadInt(fname))
#   except ValueError:
#       print("ReadError")
# 
# 

# UPG6 TOTALT: 21P
# class circle:
#     def __init__(self,r,x,y):
#         self.center = Point(x,y)
#         self.radie = r
#     def moveTo(self, x,y)
#         self.center = Point(x,y)
#         moved = True
#         return self.center

#     def isMoved(self)
#         return moved
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def getXY(self)
#         return (x,y) 

# UPG7 TOTALT:23P
# def sumPart(l1,l2):
#     if len(l1) == 0:
#         return 0
#     else:
#         if l1[0] in l2:
#             return sumPart(l1[1:],l2)
#         elif l1[0] not in l2:
#             return l1[0] + sumPart(l1[1:],l2)


# print(sumPart([4,6,2,9,8],[4,9]))
# def isfib(l):
#     if len(l)<2:
#         return False
#     i = 2
#     while i < len(l):
#         if l[i-2]+l[i-1] != l[i]:
#             return False
#         print(i)
#         i = i +1
#     return True

# print(isfib([1,1,2,3,5,8,13,21]))

# def delete(s):
#     newS=""
#     flag = False
#     for i in s:
#         if i =="t" and flag == False:
#             flag = True
#             newS=newS+"t"
#         elif i =="t" and flag == True:
#             flag = False
#             newS = newS + "T"
#         else: 
#             newS=newS+i
#     return newS

# print(delete("iterationstentamen"))
def lisexp2(lst):
    i=0
    while i <len(lst):
        if lst[i]!=2*lst[i+1]:
            return False
        lisexp2(lst[1:])
    return True
print(lisexp2([16,8,4,2,1]))