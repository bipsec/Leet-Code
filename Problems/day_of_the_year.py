import datetime
from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")
        return datetime(int(year), int(month), int(day)).timetuple().tm_yday


s = Solution()
print(s.dayOfYear(date="2019-01-09"))
print(s.dayOfYear(date="2019-02-10"))
