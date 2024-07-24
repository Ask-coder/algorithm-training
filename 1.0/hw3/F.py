line1 = input()
line2 = input()

def solution(line1, line2):

    if len(line1) < 2 or len(line2) < 2:
        return 0
    
    g1 = [line1[i] + line1[i + 1] for i in range(len(line1) - 1)]
    g2 = {line2[i] + line2[i + 1] for i in range(len(line2) - 1)}

    cnt = 0
    for item in g1:
        if item in g2:
            cnt += 1
    
    return cnt


print(solution(line1, line2))