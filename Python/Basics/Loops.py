# Range
# range(5) # [0,1,2,3,4]
# range(n) # 0,1,2,n-1;

# nums = range(5);

# print(nums)


# while Loops

# counter = 1;

# while counter <=5:
#     print("Himanshu")
#     counter +=1
# print("End of Code")


# For Loops

# nums = range(5)

# for i in nums:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)


# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)

# for i in range(2, 11,2):
#     print(i)


# for i in range(1,31):
#     # if(i == 21):
#     #     break
#     if(i == 21):
#         continue
#     if( i % 3 == 0):
#         print(i)


# for i in range(1,20):
#     if i % 2 !=0:
#         print(i)


# num = 57

# for i in range(1,11):
#     print(num * i)


# for i in range(1,50):
#    if(i == 15):
#       continue
#    if i % 3 == 0:
#       print(i)


a = int(input("Enter Number a : "))
b = int(input("Enter Number a : "))

for i in range(1, 1001):
    if i % a ==0  and i % b == 0:
        print(i)
        break