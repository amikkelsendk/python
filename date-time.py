from datetime import datetime

datetime.now()
# datetime.datetime(2024, 10, 22, 10, 51, 59, 547619)

str( datetime.now() )
# '2024-10-22 10:53:35.168220'


# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# '2024-10-22 10:56:05'
