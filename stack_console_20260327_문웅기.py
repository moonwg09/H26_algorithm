
def f_push(N):
    stack_list.append(N)
    return list

def f_pop():
    pop_num = stack_list.pop()
    return pop_num

def f_peek():
    peak_num = stack_list[-1]
    return peak_num


def isEmpty(list):
    if len(list) == 0:
        return 0
    if len(list) > 0:
        return 1

def isFull(list):
    if len(list) == 5:
        return 0
    if len(list) < 5:
        return 1

print("------------[ 정수형 스택 연산 실습 (용량 5)]")
print("===========================================")
print("  1.Push     2.Pop    3.Peek     0.Exit")
print("===========================================")

stack_list = []



while True:

    num = int(input("> 메뉴 선택 : "))

    if num == 1:
        is_full = isFull(stack_list)
        if is_full == 0:
            print(">Stack이 차 있어서 더 이상 추가할 수 없습니다")
            print(f"> 현재 스택 상태 {stack_list}")
            
        else:
            N = int(input("> 데이터 입력 : "))
            f_push(N)
            print(f"> 현재 스택 상태 {stack_list}")

    elif num == 2:
        is_empty = isEmpty(stack_list)
        if is_empty == 0:
            print("> Stack이 비어 있습니다")
            print(f"> 현재 스택 상태 {stack_list}")
            
        else:
            pop_num = f_pop()
            print(f"> 가져온 데이터 {pop_num}")
            print(f"> 현재 스택 상태 {stack_list}")

    elif num == 3:
        if isEmpty(stack_list) == 0: 
            print("> Stack이 비어 있어 Peek할 데이터가 없습니다.")
        else:
            peek_num = f_peek()
            print(f"> 가져올 데이터 {peek_num}")
            print(f"> 현재 스택 상태 {stack_list}")
    
    elif num == 0:
        print("--------[정수형 스택 연산 실습 종료]----")
        break




    