'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from math import inf
def sliding_window_max(nums, k):
    buffer = nums[:k]
    result = [0] * (len(nums)-k+1)

    for idx in range(len(result)):
        if idx!=0:
            buffer.pop(0)
            buffer.append(nums[idx+k-1])
        max = -inf
        for num in buffer:
            if num > max:
                max = num
        result[idx] = max
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
