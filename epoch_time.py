# https://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p

from datetime import datetime

round((datetime.now() - datetime.utcfromtimestamp(0)).total_seconds() * 1000.0)
# or
int(datetime.now().strftime("%s")) * 1000
