def sort(mas):

    if len(mas) < 2:
        return mas[:]

    else:
        middle = int(len(mas)/2)
        left = sort(mas[:middle])
        right = sort(mas[middle:])
        return merge(left, right)

def merge(left, right):

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

a = [int(i) for i in input().split()]
n = 0
a = sort(a)

print(a)
