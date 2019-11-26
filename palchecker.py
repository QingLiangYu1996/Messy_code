#回文词判定
from Dequeop import Deque

def palchecker(aString):
    d=Deque()
    for str in aString:
        d.addFront(str)
    while d.size()>1:
        if d.removeFront() != d.removeRear():
            return False
    return True
str='上海自来水来自海上'
print (palchecker(str))

