import unittest

from src.consumer import consumer
from src.producer1 import producer1
from src.producer2 import producer2
from src.producer3 import producer3
from src.producer4 import producer4
from src.producer5 import producer5
from src.producer6 import producer6


class TestMQ(unittest.TestCase):
    def test(self):
        producer1()
        producer2()
        producer3()
        producer5()
        producer6()
        producer4()
        consumer()


if __name__ == '__main__':
    unittest.main()
