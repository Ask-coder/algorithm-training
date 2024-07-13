#! /usr/bin/env python3
# -*- codign: utf-8 -*-


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    x_ = k + 1
    # x_ = 257
    # x_ = 10
    p = 10 ** 9 + 7
    h_s = [0] * (n + 1)
    h_r = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1

    for i in range(1, n + 1):
        h_s[i] = (h_s[i - 1] * x_ + s[i - 1]) % p
        h_r[i] = (h_r[i - 1] * x_ + s[-i]) % p
        x[i] = (x[i - 1] * x_) % p

    ans = []
    for i in range(n // 2 + 1):
        # l = min(i , n - i)
        a, b = i, n - i

        h1 = (h_s[a + i] + h_r[b] * x[i]) % p
        h2 = (h_r[b + i] + h_s[a] * x[i]) % p
        if h1 == h2:
            ans.append(b)


    print(' ' .join(map(str, ans[::-1])))
