
def getIndex(num_list, target):
    index = num_list.index(target)
    return index

def getMax(num_list):
    
    num_max = max(num_list)
    return num_max


def getMin(num_list):

    num_min = min(num_list)
    return num_min

def countGT(num_list, target):
    count = 0
    for number in num_list:
        if number > target:
            count += 1
    return count
    
def sumList(num_list):

    num_sum = sum(num_list)
    return num_sum

def swapList(num_list):
    num_list.reverse()


number_list = [23,45,27,11,25,65,78]

print(getIndex(number_list, 25))
print(getMax(number_list))
print(getMin(number_list))
print(countGT(number_list,42))
print(sumList(number_list))
swapList(number_list)
print(number_list)