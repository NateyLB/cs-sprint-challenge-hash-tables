def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weights_index = {}
    for index,weight in enumerate(weights):
        weights_index[weight] = index

    # print(weights_index)
    # def choose_indices(weights):
        

    def choose_sets(mylist,length):
        mylen = len(mylist)

        if length == 1:
            return [[i] for i in mylist]
        if length > mylen:
            return []

        ToRet = []
        for k in range(mylen): 
            if mylen - k + 1> length :
                for j in choose_sets(mylist[k+1:],length-1):
                    New = [mylist[k]]
                    New.extend(j)
                    ToRet.append(New)
        return ToRet
    permutations = choose_sets(weights, 2)
    results = []
    for values in permutations:
        if values[0] + values[1] == limit:
            if values[0] > values[1]:
                greater = values[0]
                lesser = values[1]
            else:
                greater = values[1]
                lesser = values[0]
            result1 = weights_index.get(greater)
            result2 = weights_index.get(lesser)
            print(f"[{result1}, {result2}]")
            results.append([result1, result2])
    return results

if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9] 
    print(get_indices_of_item_weights(weights, len(weights), 4))