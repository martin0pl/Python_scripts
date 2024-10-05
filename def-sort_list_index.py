def sort_list_index(l:list,index:int) -> list:
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j][index] > l[j+1][index] :
                l[j], l[j+1] = l[j+1], l[j]
    return(l)
