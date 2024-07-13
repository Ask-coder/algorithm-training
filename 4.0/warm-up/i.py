#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def psp(sequence):
    stack = []
    for item in data:
        if item in ("(", "[", "{"):
            stack.append(item)
        elif item in (")", "]", "}"):
            if stack and d[item] == stack[-1]:
                stack.pop()
            else:
                return "no"
    return "yes" if not stack else "no"


if __name__ == "__main__":
    d = {
        "]": "[",
        ")": "(",
        "}": "{",
    }
    data = input()
    print(psp(data))

