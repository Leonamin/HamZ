def divideEqual(entireCount, targetCount):
    li = []
    startIndex = 0  

    for i in range(targetCount):
        endIndex = (i + 1) * entireCount // targetCount

        li.append((startIndex, endIndex))

        startIndex = endIndex + 1

    return li


if __name__ == "__main__":
    print(divideEqual(13, 10))
    print(divideEqual(31, 5))
    print(divideEqual(32, 5))
    print(divideEqual(33, 5))

