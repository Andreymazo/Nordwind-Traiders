def dupl(da):  ##Ubiraem duplikati v new_prod_
    index = 0
    index2 = 0
    data_finish = []
    while index < len(da):
        # print(da[0][0])
        # print(index)
        while index < len(da) - 1 and da[index] == da[index + 1]:#[0][0]
            index += 1

        da[index2] = da[index]
        data_finish.append(da[index2])
        index2 += 1
        index += 1

    return data_finish
# print(dupl([[1,1,1,3],[1,1,1,3],[3,3,55,55]]))