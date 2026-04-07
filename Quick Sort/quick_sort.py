class QuickSorting:
    def quickSorting(self,list_array,lower_index, upper_index):
        if len(list_array)<=1:
            return list_array
        pivot = list_array[(lower_index+upper_index)//2]
        low = lower_index
        high = upper_index
        while low<=high:
            while list_array[low]<pivot:
                low+=1
            while list_array[high]>pivot:
                high -=1
            if low<=high:
                list_array[low],list_array[high] = list_array[high],list_array[low]
                low +=1
                high -=1
        if lower_index < high:       
            self.quickSorting(list_array,lower_index,high)
        if low< upper_index:    
            self.quickSorting(list_array,low,upper_index)

    def sortAll(self,list_given):
        pollar = QuickSorting()
        pollar.quickSorting(list_given, 0, len(list_given)-1)  
        return list_given

list_shared = list(map(int,input().split()))
solutions = QuickSorting()
bella = solutions.sortAll(list_shared)
print(*bella)     


    
