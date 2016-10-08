#!/Users/xinguimeng/.pyenv/shims/python
#即将被测试的类
class Data:
    def getData(self,id):
        tmp = self.getFromCache(id,id*id)
        return tmp + 3
    def getFromCache(self,id,expire):
        return id + expire
