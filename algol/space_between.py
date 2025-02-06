def spaceBetween(
    numbers: list[int],
    count: int,
) -> list[int]:
    result: list[int] = []
    numbersLen = len(numbers)
    for i in range(count):
        index = round((i) * (numbersLen - 1) / (count - 1))
        result.append(numbers[index])
    return result



if __name__ == "__main__":
    numbers = list(range(1, 33))
    print(numbers)
    print(spaceBetween(numbers, 5))
    pass
