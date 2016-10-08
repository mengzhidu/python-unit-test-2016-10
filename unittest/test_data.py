#!/Users/xinguimeng/.pyenv/shims/python
from data import Data
import unittest
from  unittest.mock import MagicMock
#测试用例类
class DataTestCase(unittest.TestCase):
    def setUp(self):
        self.data = Data()
    def tearDown(self):
        self.data = None
    def testCalled(self):
        self.data.getFromCache = MagicMock()
        self.data.getData(3)
        self.data.getFromCache.assert_called_once_with(3,9)
    def testCaller(self):
        self.data.getFromCache = MagicMock()
        self.data.getFromCache.return_value = 20
        tmpVal = self.data.getData(4)        
        self.assertEqual(tmpVal,23)

#开始测试
if __name__ == "__main__":
    unittest.main()
