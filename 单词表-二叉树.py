class treenode:
    def __init__(self,val):
        self.val=val
        self.rightchild=None
        self.leftchild=None

class tree():
    def __init__(self):
        self.root=None

    def insert(self,val):
        new_node=treenode(val)
        if self.root is None:
            self.root=new_node
            return 0
        else:
            curr=self.root
        while True:
            if val<=curr.val:
                if curr.leftchild is None:
                    curr.leftchild=new_node
                    break
                else:
                    curr=curr.leftchild
            else:
                if curr.rightchild is None:
                    curr.rightchild = new_node
                    break
                else:
                    curr = curr.rightchild
        return 0



def Traveltree(tree,dist):
    if(tree.leftchild):
        dist=Traveltree(tree.leftchild,dist)
    if(tree.rightchild):
        dist=Traveltree(tree.rightchild,dist)
    key=tree.val
    dist.append(key)
    return dist


def com(str1,str2):

    count = 0
    temp = ''
    # 始终保持str1为两字符串中的长串
    # temp用于占位,可以设置为任意字符
    if len(str1) < len(str2):
        str1, str2 = str2, str1
        temp = '-'
    if len(str1) > len(str2):
        temp = '-'
    # 避免短字符串索引越界
    str2 = str2 + '-'
    # 循环遍历长字符串
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count += 1
        else:
            # 重新拼接字符串
            str2 = str2[:i] + temp + str2[i:]
    # 判断两字符串是否为近似串,返回值为布尔类型
    if len(str1) == count + 1:
        return 1
    else:
        return 0



def find(str,dist):
    res=[]
    compare=[]
    l=len(str)
    flag=0
    for key in dist:
        if(len(key)<=l+1 and len(key)>=l-1):
            compare.append(key)
    for j in compare:
        if(com(j,str)==1):
            res.append(j)
    return res


def main():
    i=0
    dist=[]
    str=input()
    while(str!='#'):
        dist.append(str)
        str = input()
    inp=[]
    str=input()
    while(str!='#'):
        inp.append(str)
        str = input()
        pxtree=tree()
    for i in dist:
        pxtree.insert(i)
    res=[]
    res=Traveltree(pxtree.root,res)
    for i in res :
        print(i,end=' ')
    print()
    for st in inp:
        print(st,end='')
        if(st not in dist):
            print(':',end=' ')
            fl=find(st,dist)
            for i in fl:
                print(i,end=' ')
            print()
        else:
            print(' is correct')

if __name__=="__main__":
    main()