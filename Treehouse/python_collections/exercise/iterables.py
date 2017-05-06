def combos(item1, item2):

    combos = []

    for index, item in enumerate(item1, start=0):
        combo = (item1[index], item2[index])
        combos.append(combo)

    return combos

print(combos([1,2,3], 'abc'))
