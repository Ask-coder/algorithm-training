
def clean_number(number: str) -> str:
    res = number.strip().replace('+', '').replace('-', '').replace('(','').replace(')', '')
    if len(res) == 7:
        res = '8495' + res
    
    return res[1:]
    

if __name__ == '__main__':
    add_number = clean_number(input())
    number_1 = clean_number(input())
    number_2 = clean_number(input())
    number_3 = clean_number(input())

    for item in [number_1, number_2, number_3]:
        print('YES' if add_number == item else 'NO')
