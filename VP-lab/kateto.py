# list_1 = [-2,3,36,28,9,0,-28]

# result = 0
# for x in list_1:
#     if abs(x) % 6 == 4:
#         if result > x:
#            result = x
# if result:
#     print(list_1.index(result))
    
    
    
# for num in list_1 :
#     print(list_1.index(num))
    
# print("------------")

# for i in range(len(list_1)):
#     print(i)
    
    
# list_2=[3,4,5,6,7,8,9]
# for i in range(len(list_2)-1,-1,-1):
#     if i % 2 == 0:
#         list_2.remove(list_2[i])
        
# print(list_2)
        
        
# list_3 = [0,1,2,3,4,5,6]




list1=[0,5,4,7,-22,4,58,-9,3,1]

for i in range(len(list1)-1,-1,-1):
    if i %2 != 1:
        if list1[i] > 0:
            list1.remove(list1[i])
print(list1)

