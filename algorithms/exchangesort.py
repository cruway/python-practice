def exchangesort(inputData):
    for i in range(len(inputData)):
        for j in range(i + 1, len(inputData)):
            if inputData[i] < inputData[j]:
                inputData[i], inputData[j] = inputData[j], inputData[i]
    print(inputData)


S = [-1, 10, 7, 11, 5, 13, 8]
print(S)
exchangesort(S)