#利用栈进行进制转换
from stackop import Stack

#num=TempNum
#s=Stack()

#while num>0:
#    s.push(num%2)
#    num//=2
#result=''
#for i in range(s.size()):
#    result+=str(s.pop())
#
#print ('{:0}的二进制为{:1}'.format(TempNum,result))


def NumConversion(num,b:'0<int<=16'=2):
    if b<0 or b>16:
        return None
    strlist='0123456789ABCDEF'
    s=Stack()
    result=''
    while num>0:
        s.push(num%b)
        num//=b
    while s.size() > 0:
        result+=strlist[s.pop()]
    
    return result
    
TempNum1=eval(input('请输入一个十进制整数:'))
TempNum2=eval(input('请输入要转换的进制（2~16）:'))
print (NumConversion(TempNum1,TempNum2))
