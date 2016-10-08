#!/Users/xinguimeng/.pyenv/shims/python
#即将被测试的类
class Tool:
    def __init__(self,num = 30):
        self._num = num
    def getNum(self):
        return self._num
    def setNum(self,num):
        if num < 0 or num > 120:
            raise ValueError("非法数据")
        self._num = num
    def addNum(self):
        self._num += 1
    def subNum(self):
        self._num -= 1
