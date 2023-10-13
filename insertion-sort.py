nums = [99,100,88,4,9,19,15]
#[5,100,100]
#88,1

def insertion_sort(alist):
    for i in range(1, len(alist)):
        while i >0 and alist[i-1] >alist[i]:
            alist[i], alist[i-1] = alist[i-1], alist[i]
            i -= 1


#insertion_sort(nums)
print(nums)


def insertion_variant(alist):
    for i in range(1, len(alist)):
        current_number = alist[i]
        while i > 0 and alist[i-1] > current_number:
            alist[i] = alist[i-1]
            i -= 1
            alist[i] = current_number

insertion_variant(nums)            


print(nums)