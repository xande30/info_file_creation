import os
from os import path
from colorama import Fore
import time


way = "file.txt"

print(Fore.MAGENTA,os.listdir('.'))
print(Fore.MAGENTA,path.getsize('file.txt'))


file_creation_time = path.getctime(way)
file_creation_timem = path.getmtime(way)

print(Fore.MAGENTA, file_creation_time)
convert_sec_to_time_stamp = time.ctime(file_creation_time)
convert_sec_to_time_stamp_m = time.ctime(file_creation_timem)

print(Fore.MAGENTA,f"The file located at the path {way} \
was created at {convert_sec_to_time_stamp} and was "
      f"last modified at {convert_sec_to_time_stamp_m}")
