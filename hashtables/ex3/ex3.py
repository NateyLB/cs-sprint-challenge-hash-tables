def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    for index,arr in enumerate(arrays):
        locals()["dict{}".format(index)] ={}
        for value in arr:
            locals()["dict{}".format(index)][value] = True

    # for index in range(len(arrays)):
    #     print(locals()["dict{}".format(index)])
    results =[]
    for key in locals()["dict{}".format(0)]:
        if len(arrays) < 3:
            if locals()["dict{}".format(1)].get(key):
                results.append(key)
        else:
            if locals()["dict{}".format(1)].get(key) and locals()["dict{}".format(2)].get(key):
                results.append(key)


    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
