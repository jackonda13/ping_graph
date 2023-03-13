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

def y_graph(log):
    y_ = []
    for i in log['10.41.9.9']:
        y_.append(i[1])
    return y_


def x_graph(log):
    x_ = []
    for i in log['10.41.9.9']:
        x_.append(i[0])
    return x_

filename_ = 'log.log'
# y = np.arange(y_graph(get_data(filename_)))
# x = np.arange(x_graph(get_data(filename_)))

y = y_graph(get_data(filename_))
x = x_graph(get_data(filename_))

plt.plot(x, y)
plt.xticks(rotation=90)
plt.show()

print(x_graph(get_data('log.log')))
