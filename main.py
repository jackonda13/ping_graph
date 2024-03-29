from datetime import datetime
from ping3 import ping
from time import sleep


logfile = 'log.log'
state = True
ip = '100.41.9.9'


def log(text, filename):
    with open(filename, 'a+') as log_file:
        log_file.write(f'{text} \n')


while state:
    time_now = datetime.now()
    response = ping(ip, unit='ms')
    if isinstance(response, float):
        log(f'{time_now.strftime("%d.%m.%y %H:%M:%S")}, {ip}, {"%.2f" % response}', logfile)
    else:
        log(f'{time_now.strftime("%d.%m.%y %H:%M:%S")}, {ip}, None', logfile)
    sleep(1)
