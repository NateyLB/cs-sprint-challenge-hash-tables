def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weights_index = {}
    for index,weight in enumerate(weights):
        weights_index[weight] = index

    # print(weights_index)
    def choose_indices(weights):
        

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
    print(choose_sets(weights, 2))
    return None

if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9] 
    get_indices_of_item_weights(weights, len(weights), 4)