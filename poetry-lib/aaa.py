from dateutil.relativedelta import *
from datetime import *


def bbb():
    today = datetime.now()
    return today + relativedelta(months=+6)
