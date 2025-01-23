def divide(rawValues):
    if len(rawValues) > 1:
        mid = int(len(rawValues) / 2)  # 두개로 나눈거
        left = rawValues[:mid]
        right = rawValues[mid:]

        dividedLeft = divide(left)
        dividedRight = divide(right)

        return merge(dividedLeft, dividedRight)
    else:
        return rawValues


def merge(left, right):
    merged = []

    leftIdx = 0
    rightIdx = 0

    leftLen = len(left)
    rightLen = len(right)

    while leftIdx < leftLen and rightIdx < rightLen:
        if (left[leftIdx] < right[rightIdx]):
            merged.append(left[leftIdx])
            leftIdx += 1
        else:
            merged.append(right[rightIdx])
            rightIdx += 1

    # 한쪽 포인터에서 이미 정렬된 상태에서 남은 값들을 추가
    merged.extend(left[leftIdx:])
    merged.extend(right[rightIdx:])

    return merged


def mergeSort(rawValues):
    divided = divide(rawValues)
    print(divided)


if __name__ == "__main__":
    rawValues = [21, 10, 12, 20, 25, 13, 15, 22, 6,]

    print(rawValues)
    mergeSort(rawValues)
