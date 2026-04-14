def insertionSort(given_list):
    for i in range(1,len(given_list)):
        key = given_list[i]
        j=i-1
        while j>=0 and key<given_list[j]:
            given_list[j+1]=given_list[j]
            j-=1
        given_list[j+1]=key
    return given_list

list_given=list(map(int,input().split()))
print(insertionSort(list_given))        
