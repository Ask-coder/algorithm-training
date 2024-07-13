def check_eq(num1: int, num2: int) -> bool:
    return num1 == num2

def check_gt(num1:int, num2: int) -> bool:
    return num1 < num2 

def check_ge(num1: int, num2: int) -> bool:
    return num1 <= num2

def check_lt(num1: int, num2: int) -> bool:
    return num1 > num2

def check_le(num1: int, num2: int) -> bool: 
    return num1 >= num2


def derminate_type_seq(arr, check):
    for i in range(1, len(arr)):
        if not check(arr[i - 1], arr[i]):
            return False            
    return True


def pass_seq(arr: list):
    checker = {
        check_eq: "CONSTANT", 
        check_ge: "WEAKLY ASCENDING", 
        check_le: "WEAKLY DESCENDING", 
    }
    
    for check in checker:
        if derminate_type_seq(arr, check):
            return checker[check]
    return "RANDOM"


if __name__ == '__main__':
    arr = []
    while tmp := int(input()):
        if tmp == -2 * 10 ** 9:
            break
        arr.append(tmp)

    if len(arr) == 0 or len(arr) == 1:
        print("RANDOM")
        exit(0)

    res = pass_seq(arr)
    if res == "WEAKLY ASCENDING":
        print("ASCENDING" if derminate_type_seq(arr, check_gt) else res)
    elif res == "WEAKLY DESCENDING":
        print("DESCENDING" if derminate_type_seq(arr, check_lt) else res)
    else:
        print(res)    
