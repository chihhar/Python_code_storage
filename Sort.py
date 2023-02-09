import numpy as np
import time
import pdb
def bubble_sort(sort_list):
    #昇順にソート。隣接値の入れ替え
    for i in range(len(sort_list)-1):
        change_flag=0
        for j in range(len(sort_list)-1-i):#最悪で右から順に決定.
            if sort_list[j]>sort_list[j+1]:
                sort_list[j], sort_list[j+1]=sort_list[j+1],sort_list[j]
                change_flag=1
        if change_flag==0:
            break
    return sort_list
def quick_sort(sort_list):
    return sort_list

def merge(left_list, right_list):
    sorted_list=[]
    left_ind=0
    right_ind=0
    while left_ind < len(left_list) and right_ind < len(right_list):
        if left_list[left_ind]<right_list[right_ind]:
            sorted_list.append(left_list[left_ind])
            left_ind+=1
        else:
            sorted_list.append(right_list[right_ind])
            right_ind+=1
    if left_list:
        sorted_list.extend(left_list[left_ind:])
    if right_list:
        sorted_list.extend(right_list[right_ind:])
    return sorted_list
def merge_sort(sort_list):
    if len(sort_list)<=1:
        return sort_list
    mid = len(sort_list)//2
    left, right= sort_list[:mid],sort_list[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)
    
def sort_check(sorted_list):
    return all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list)-1))
    
def main():
    sort_list=np.arange(1000)
    np.random.seed(42)
    np.random.shuffle(sort_list)
    print(f"need_sort_list:{sort_list}\n")
    
    #bubble_sort start
    start_time=time.time()
    bubble_sort_result=bubble_sort(sort_list.copy())
    time_end=time.time()
    sort_check(bubble_sort_result)
    print(f"bubble_sort:sort_check={sort_check(bubble_sort_result)}\n"
          f"sort_time:{time_end-start_time}\n")
    
    #merge_sort start
    start_time=time.time()
    merge_sort_result=merge_sort(sort_list.copy())
    time_end=time.time()
    print(f"merge_sort:check={sort_check(merge_sort_result)}\n"
          f"sort_time:{time_end-start_time}\n")
    
    #quick_sort start
    start_time=time.time()
    quick_sort_result=quick_sort(sort_list.copy())
    time_end=time.time()
    print(f"quick_sort:check={sort_check(quick_sort_result)}\n"
          f"sort_time:{time_end-start_time}\n")
if __name__ == '__main__':
    main()