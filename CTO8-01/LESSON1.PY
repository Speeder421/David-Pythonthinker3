# def is_ascending(item):
#     for i in range(len(item)-1):
#         if item[i]>=item[i+1]:
#             return False
#     return True
# list=[1,2,3,4,5]
# is_ascending(list)
# print(is_ascending(list))

def bubble_sort(numbers):
    # for j in range(len(numbers)):
        for i in range(len(numbers)-1):
            if numbers[i]>numbers[i+1]:
                item=numbers[i+1]
                numbers[i+1]=numbers[i]
                numbers[i]=item
        return numbers
bubble_sort(list)
list=[9,6,3,25,21,8,23,1,17,14]
print(list)