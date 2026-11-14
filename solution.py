def min_coins_to_add(a: list[int]) -> int:
    a.sort()
    largest = a[-1]

    total = 0
    i = 0
    while i < len(a)-1:
        total += largest - a[i]
        i += 1

    return total