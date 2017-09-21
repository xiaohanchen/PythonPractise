# -*- coding: utf-8 -*-

# I V X   L  C   D    M
# 1 5 10 50 100 500 1000

#RULE:
# 1. Repeating a numeral up to **three** times represents addition of the number, Only I, X, C, and M can be repeated; V, L, and D cannot be
# 2. Write from large num to small num
# MAX: 3888
# example: M(CM)(XL)(IV)

# look ahead solution
# IV 4 IX 9 XL 40 XC 90 CM 900     each could exist only once!

def romanToInt_LookAhead(romanStr):
    sum = 0
    skipNext = False
    for idx, char in enumerate(romanStr):
        if skipNext:
            skipNext = False
            continue

        if char == 'I':
            if idx < len(romanStr)-1:
                if romanStr[idx+1] == 'V':
                    sum += 5 - 1
                    skipNext = True   #下一个item in loop 跳过
                else:
                    sum += 1
            else:
                sum += 1
        elif char == 'V':
            sum += 5
    return sum


# Method2: reverse iterate!!!
def romanToInt_BestSolution(romanStr):
    print(romanStr.index("IV"))



    return

# Method3: count every Symbol and add its value to the sum, and minus the extra part of special cases.********



s = "IX"
print romanToInt_LookAhead("I")
print romanToInt_LookAhead("IV")
print romanToInt_LookAhead("IVI")
print romanToInt_LookAhead("IVV")
print romanToInt_LookAhead("IVVI")
print romanToInt_LookAhead("IVIV")


romanToInt_BestSolution("XXXXXIV")
# ints = [8, 23, 45, 12, 78]
# for idx, val in enumerate(ints):
#     print(idx, val)




