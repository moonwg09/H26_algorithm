
A = [5, 7, 23, 14, 9]

def partition(A, left, right):
    # 가장 왼쪽 원소를 피벗으로 설정
    pivot = A[left]
    low = left + 1
    high = right

    while True:
        # 피벗보다 큰 값을 찾을 때까지 low 이동
        while low <= high and A[low] <= pivot:
            low += 1
        
        # 피벗보다 작은 값을 찾을 때까지 high 이동
        while low <= high and A[high] >= pivot:
            high -= 1

        # 두 인덱스가 엇갈리지 않았다면 두 원소 교환
        if low <= high:
            A[low], A[high] = A[high], A[low]
        else:
            # 엇갈렸다면 루프 종료
            break

    # 피벗을 적절한 위치(high)로 옮김
    A[left], A[high] = A[high], A[left]
    return high # 새로운 피벗의 위치 반환

def quick_sort(A, left, right):
    if left < right:
        # 피벗을 기준으로 리스트를 쪼개고 피벗의 위치를 받음
        pivot_index = partition(A, left, right)
        
        # 피벗을 제외한 왼쪽과 오른쪽 부분을 각각 재귀적으로 정렬
        quick_sort(A, left, pivot_index - 1)
        quick_sort(A, pivot_index + 1, right)


quick_sort(A, 0, len(A) - 1)
print(A) 