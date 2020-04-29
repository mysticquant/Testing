import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    @patch("my_calendar.requests")
    def test_get_holidays_timeout(self,mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

    # Can also patch an inidividual object method
    @patch.object(requests,get,side_effect=Timeout)
    def test_get_holidays_timeout_2(self,mock_requests):
        with self.assertRaises(Timeout):
            get_holidays()


if __name__=="__main__":
    unittest.main()

