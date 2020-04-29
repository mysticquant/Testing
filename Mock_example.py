from unittest.mock import Mock
from datetime import datetime
import requests


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


mock = Mock()
print(mock)
print(mock.some_attribute)
print(mock.do_something())
# Patch the json library
json = Mock()
print(json.dumps())
print(json.loads('{"k": "v"}').get('k'))
json.loads.assert_called_once()
json.loads.assert_called()
json.loads.assert_called_once_with('{"k": "v"}')
# Will fail
#json.loads.assert_not_called()





def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() <= 4


# Save a couple of test days
tuesday = datetime(year=2019, month=1, day=1)
saturday = datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()

# Mock .today() to return Tuesday
datetime.today.return_value = tuesday

assert is_weekday()

# Mock .today() to return Saturday
datetime.today.return_value = saturday

# Will fail
#assert is_weekday()


