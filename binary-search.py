def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


element = [int(x) for x in input("Enter the sorted array elements separated by spaces: ").split()]
guess = int(input("Enter the target value to search: "))
res = binary_search(element, guess)

if res != -1:
    print(f"Element {guess} is present at index {res}.")
else:
    print(f"Element {guess} is not present in the array")
