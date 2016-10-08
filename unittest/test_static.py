#!/Users/xinguimeng/.pyenv/shims/python
from tool import Tool
import unittest
#测试用例类
class ToolTestCase(unittest.TestCase):
    def runTest(self):
        tool = Tool()
        self.assertEqual(tool.getNum(),30)

#运行测试
if __name__ == "__main__":
    testCase = ToolTestCase()
    testCase.runTest()



