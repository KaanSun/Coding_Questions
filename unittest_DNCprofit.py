import unittest
from Hard_int_questions.stockProfitDNC import MaxPriceDNC

class TestMaxPriceDNC(unittest.TestCase):
    def test_basic_case(self):
        stockList = [100, 180, 260, 310, 40, 535, 695]
        startindex = 0
        endindex = len(stockList) - 1
        self.assertEqual(MaxPriceDNC(stockList, startindex, endindex), (4, 6))

    def test_no_profit(self):
        stockList = [100, 90, 80, 70, 60]
        startindex = 0
        endindex = len(stockList) - 1
        self.assertEqual(MaxPriceDNC(stockList, startindex, endindex), (0, 0))

    def test_single_day(self):
        stockList = [100]
        startindex = 0
        endindex = len(stockList) - 1
        self.assertEqual(MaxPriceDNC(stockList, startindex, endindex), (0, 0))

    def test_two_days_profit(self):
        stockList = [100, 200]
        startindex = 0
        endindex = len(stockList) - 1
        self.assertEqual(MaxPriceDNC(stockList, startindex, endindex), (0, 1))

    def test_two_days_no_profit(self):
        stockList = [200, 100]
        startindex = 0
        endindex = len(stockList) - 1
        self.assertEqual(MaxPriceDNC(stockList, startindex, endindex), (0, 0))

if __name__ == '__main__':
    unittest.main()