A = [5, 7, 23, 14, 9]
new_list = [0] * len(A)

def merge(A, left, mid, right):
    pL = left
    pR = mid + 1
    pNew = left

    #두 영역을 비교하며 new_list에 채우기
    while pL <= mid and pR <= right: 
        if A[pL] <= A[pR]:
            new_list[pNew] = A[pL]
            pL += 1
        else:
            new_list[pNew] = A[pR]
            pR += 1
        pNew += 1
    
    #왼쪽 영역이 남은 경우 처리
    while pL <= mid:
        new_list[pNew] = A[pL]
        pL += 1
        pNew += 1
        
    #오른쪽 영역이 남은 경우 처리
    while pR <= right:
        new_list[pNew] = A[pR]
        pR += 1
        pNew += 1

    #정렬된 구간을 원본 배열 A에 덮어쓰기
    for i in range(left, right + 1):
        A[i] = new_list[i]

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

merge_sort(A, 0, len(A) - 1)
print(A)