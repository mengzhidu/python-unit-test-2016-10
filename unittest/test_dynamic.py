#!/Users/xinguimeng/.pyenv/shims/python
from tool import Tool
import unittest
#测试用例类
class ToolTestCase(unittest.TestCase):
    def setUp(self):
        self.tool = Tool()
    def tearDown(self):
        self.tool = None
    def testInit(self):
        self.assertEqual(self.tool.getNum(),30)
    def testSet(self):
        setVal = 140
        self.assertRaises(ValueError,self.tool.setNum,setVal)
        #self.tool.setNum(setVal)
        #self.assertEqual(self.tool.getNum(),setVal)
    def testAdd(self):
        tmpVal = self.tool.getNum() + 1
        self.tool.addNum()
        self.assertEqual(self.tool.getNum(),tmpVal)
    def testSub(self):
        tmpVal = self.tool.getNum() - 1
        self.tool.subNum()
        self.assertEqual(self.tool.getNum(),tmpVal)

        

#开始测试
if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(ToolTestCase("testInit"))
    suite.addTest(ToolTestCase("testSet"))
    suite.addTest(ToolTestCase("testAdd"))
    suite.addTest(ToolTestCase("testSub"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
