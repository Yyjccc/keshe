import math
MAXSIZE = 101

#定义打印真值表的函数
def calling(s, j):

    a = []
    while s!=0:
        if(s%2==1):
            a.append(1)
        else:
            a.append(0)
        s=s//2
    for i in a:
        print(i, end=" ")
    print()

#主函数
if __name__ == "__main__":
    str = input()
    j=0
    a=[]
    for i in range(0, len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            a.append(str[i])
            j += 1
            print(str[i], end="")
            if i+1<=len(str):
                print(" ", end="")

        if str[i] == '-':
            print(str[i], str[i + 1], sep="", end="")
            if i <=len(str) :
                print(" ", end="")
        elif str[i] == '<':
            print(str[i], str[i + 1], str[i + 2], sep="", end="")
            i += 1
            if i <=len(str):
                print(" ", end="")
        elif str[i] == '|' or str[i] == '^' or str[i] == '!' or str[i] == '(' or str[i] == ')':
            print(str[i], end="")
            if i + 1<len(str):
                print(" ", end="")
    print()
    for i in sorted(a):
        print(i,end=' ')
    print()
    sum = math.pow(2, j) - 1
    while sum >= 0:
        calling(sum, j)
        sum -= 1

