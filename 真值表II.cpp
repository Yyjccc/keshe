#include <bits/stdc++.h>
#define MAXSIZE 201
using namespace std;

int re(int aa,int bb,char ch)
{
    if(ch=='|')
    {
        if(aa==0&&bb==0)
            return 0;
        else return 1;
    }
    else if(ch=='^')
    {
        if(aa==1&&bb==1)
            return 1;
        else return 0;
    }
    else if(ch=='-')
    {
        if(aa==1&&bb==1)
            return 1;
        else if(aa==1&&bb==0)
            return 0;
        else return 1;
    }
    else if(ch=='<')
    {
        if(aa==1&&bb==1)
            return 1;
        else if(aa==0&&bb==0)
            return 1;
        else
            return 0;
    }
    return 0;
}

void cal(int sum,int j,char b[],char alg[])
{
    int i;
    int a[11]= {0};
    int flag=0;
    while(sum/2)
    {
        a[flag]=sum%2;
        flag++;
        sum/=2;
    }
    a[flag]=sum;
    flag++;
    for(i=j-1; i>=0; i--)
    {
        printf("%d ",a[i]);
    }
    stack<int> opnd;
    stack<char> optr;
    sort(alg,alg+j);
    for(i=0; i<strlen(b);)
    {
        if(b[i]>='a'&&b[i]<='z')
        {
            for(int jj=0; jj<j; jj++)
            {
                if(b[i]==alg[jj])
                {
                    opnd.push(a[j-jj-1]);
                }
            }
            i++;
            continue;
        }
        if((optr.empty()==true)&&(!(b[i]>='a'&&b[i]<='z')))
        {
            optr.push(b[i]);
            if(b[i]=='|'||b[i]=='-')
            {
                i+=2;
            }
            else if(b[i]=='^'||b[i]=='!'||b[i]=='('||b[i]==')')
            {
                i++;
            }
            else if(b[i]=='<')i+=3;
            continue;
        }
        if(opnd.empty()==true&&b[i]=='!')
        {
            optr.push(b[i]);
            i++;
            continue;
        }
        int pan,x,y;
        if((optr.top()=='(')&&(b[i]==')'))
        {
            pan=0;
        }
        else if(b[i]==')')pan=1;
        else if(optr.top()=='(')pan=-1;
        else if(b[i]=='(')pan=-1;
        else
        {
            if(b[i]=='!')x=5;
            else if(b[i]=='^')x=4;
            else if(b[i]=='|')x=3;
            else if(b[i]=='-')x=2;
            else x=1;
            if(optr.top()=='!')y=5;
            else if(optr.top()=='^')y=4;
            else if(optr.top()=='|')y=3;
            else if(optr.top()=='-')y=2;
            else y=1;
            if(x-y>0)pan=-1;
            else pan=1;
        }
        switch(pan)
        {
        case -1:
        {
            optr.push(b[i]);
            break;
        }
        case 0:
        {

            optr.pop();
            break;
        }
        case 1:
        {
            char ch;
            ch=optr.top();
            optr.pop();
            if(ch=='!')
            {
                int aa=opnd.top();
                aa=!aa;
                opnd.top()=aa;
                break;
            }
            else
            {
                int aa,bb;
                bb=opnd.top();
                opnd.pop();
                aa=opnd.top();
                opnd.pop();
                opnd.push(re(aa,bb,ch));
                break;
            }
        }
        }
        if(pan==1)continue;
        if((b[i]=='|')||(b[i]=='-'))
        {
            i+=2;
        }
        else if((b[i]=='^')||(b[i]=='!')||(b[i]=='(')||(b[i]==')'))
        {
            i++;
        }
        else
        {
            i+=3;
        }
    }
    while(optr.empty()!=true)
    {
        char ch;
        ch=optr.top();
        optr.pop();
        if(ch=='!')
        {
            int aa;
            aa=opnd.top();
            aa=!aa;
            opnd.top()=aa;
        }
        else
        {
            int bb,aa;
            bb=opnd.top();
            opnd.pop();
            aa=opnd.top();
            opnd.pop();
            opnd.push(re(aa,bb,ch));
        }
    }
    printf("%d",opnd.top());
    printf("\n");
}

int main()
{
    char str[MAXSIZE];
    int i,j,k;
    while(gets(str))
    {
        int a[260]= {0};
        char alg[260];
        char b[200];
        j=k=0;
        for(i=0; str[i]!='\0'; i++)
        {
            if(str[i]!=' ')
            {
                b[k]=str[i];
                k++;
            }
            if(str[i]>='a'&&str[i]<='z')
            {
                int b=str[i];
                if(a[b-97]==0)
                {
                    a[b-97]=1;
                    alg[j]=str[i];
                    j++;
                }
            }

        }
        b[k]='\0';
        for(i=0; i<=25; i++)
        {
            if(a[i]==1)
            {
                printf("%c ",i+97);
            }
        }
        cout<<str<<endl;
        int sum=pow(2,j)-1;
        while(sum>=0)
        {
            cal(sum,j,b,alg);
            sum--;
        }
    }
    return 0;
}