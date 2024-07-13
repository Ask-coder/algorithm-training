


if __name__ == '__main__':
    arr = list(map(int, input().split()))

    def cnt_gt(arr):
        cnt = 0
        if len(arr) < 3:
            return cnt
        
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                cnt += 1
        return cnt
    
    print(cnt_gt(arr))

