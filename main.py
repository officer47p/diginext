import math

# First question: Repeat given string n times and return repeated 'a's


def repeat_string(string, count) -> int:
    multiplier = math.ceil(count / len(string))
    result: str = (string * multiplier)[:count]
    return result.count('a')


print(f"The number of repeated 'a' characters is {repeat_string('abcac', 10)}")

# Second question: Refactor given string based on alphabetic order (between 'a's and 'b's) and return the numbers of characters that need to be removed


def cleanup(string) -> int:
    string = string.lower()
    expect_a = string[0] == 'a'
    removal_count = 0

    for char in string:
        if expect_a:
            if char == 'b':
                removal_count += 1
            else:
                expect_a = not expect_a
        else:
            if char == 'a':
                removal_count += 1
            else:
                expect_a = not expect_a

    return removal_count


print(
    f"Minimum number of characters that need to be removed is {cleanup('AAABBB')}")


# Third question: Quick sort algorithm that returns the number of required swaps
count = 0


def quick_sort(arr, low, high):
    global count  # I know, bad practice, but didn't have time to refactor :)
    if (low >= high):
        return
    p = arr[(low + high) // 2]       # pivot, any arr[] except arr[high]
    i = low - 1
    j = high + 1
    while (1):
        while (1):               # while(arr[++i] < p)
            i += 1
            if (arr[i] >= p):
                break
        while (1):               # while(arr[--j] < p)
            j -= 1
            if (arr[j] <= p):
                break
        if (i >= j):
            break
        arr[i], arr[j] = arr[j], arr[i]
        count += 1
    quick_sort(arr, low, j)
    quick_sort(arr, j+1, high)

    return count


li = [7, 1, 3, 2, 4, 5, 6]
print(
    f"The number of minimum swaps required is {quick_sort(li, 0, len(li) - 1)}")
