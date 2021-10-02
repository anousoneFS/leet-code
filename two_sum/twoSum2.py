def twoSum(inp, tar):
    for i in range(len(inp)):
        for id, j in enumerate(inp):
            if id > i:
                if inp[i] + j == tar:
                    return [i, id]


if __name__ == "__main__":
    print(twoSum([3, 3, 4, 5], 8))
