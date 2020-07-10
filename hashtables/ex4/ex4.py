def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    pos = {}
    neg = {}
    result = []
    for num in a:
        if num > 0:
            pos[num] = True
        else:
            neg[num] = True
    for key in pos:
        if(neg.get(key*-1)):
            result.append(key)


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
