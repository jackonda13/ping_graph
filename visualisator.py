import matplotlib.pyplot as plt
import numpy as np


def get_data(filename):
    with open(filename, "r") as logfile:
        result = {}
        for i in logfile.readlines():
            ip = i.split(',')[1].strip()
            time_ping = [i.split(',')[0], i.split(',')[2].split('\n')[0].strip()]
            result[ip] = result.setdefault(ip, []) + [time_ping]
        return result


y = np.arange(get_data())


print(get_data('log.log'))
