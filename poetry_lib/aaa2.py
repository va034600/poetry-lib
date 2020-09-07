from dateutil.relativedelta import *
from datetime import *


def bbb2():
    today = datetime.now()
    return today + relativedelta(months=+6)
