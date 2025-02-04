def divideEqual(entireCount, targetCount):
    li = []
    startIndex = 0  

    for i in range(targetCount):
        endIndex = (i + 1) * entireCount // targetCount

        li.append((startIndex, endIndex))

        startIndex = endIndex

    return li


if __name__ == "__main__":
    print(divideEqual(93, 30))
