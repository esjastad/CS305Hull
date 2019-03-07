#quicksort
def partition(array, begin, end):
    pivot = begin
    for i in range (begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin, end):   
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)	
	
#For sorting the x values in generated points
def sort(InputList):
	end = len(InputList)-1
	InputList = quicksort(InputList,0,end)