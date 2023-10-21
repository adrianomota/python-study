def print_list(lst):
    idx = 0
    while idx < len(lst):
        print(lst[idx])
        idx += 1

    print("Done!")

def list_numbers(n):
    idx = 0
    new_list = []
    while idx <= n:
        if idx % 2 == 0:
            new_list.append(idx)
        idx += 1
    return new_list

def square_list(nums):
    idx = 0
    while idx < len(nums):
        nums[idx] = nums[idx] * nums[idx]
        idx += 1
    return nums


# input => flavors = ["vanilla", "strawberry", "chocolate", "mint", "banana", "rubber"]
def list_flavors(flavors):
    for flavor in flavors:
        print(flavor)

