
class MergeSort:
    def mergeSort(self, user_provided_list):
        if len(user_provided_list)<=1:
            return user_provided_list
        mid_value = len(user_provided_list)//2
        left_list = user_provided_list[:mid_value]
        right_list = user_provided_list[mid_value:]

        new_left_list = self.mergeSort(left_list)
        new_right_list = self.mergeSort(right_list)

        return self.sorting_values(new_left_list,new_right_list)
    
    def sorting_values(self, list_a, list_b):
        i = 0 
        j = 0
        new_list =[]
        while i < len(list_a) and j < len(list_b):
            if list_a[i]<list_b[j]:
                new_list.append(list_a[i])
                i +=1
            else:
                new_list.append(list_b[j])
                j +=1
        new_list.extend(list_a[i:])  
        new_list.extend(list_b[j:])  
        return new_list

class_variables = MergeSort()
list_hola =  list(map(int, input().split())) 
sorted_list = class_variables.mergeSort(list_hola)
print(*sorted_list)



