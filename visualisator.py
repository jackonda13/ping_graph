import matplotlib.pyplot as plt


def get_data(filename):
    with open(filename, "r") as logfile:
        result = {}
        for i in logfile.readlines():
            ip = i.split(',')[1].strip()
            time_ping = [i.split(',')[0], i.split(',')[2].split('\n')[0].strip()]
            result[ip] = result.setdefault(ip, []) + [time_ping]
        return result


def y_graph(log, ip):
    y_ = []
    for i in log[ip]:
        y_.append(i[1])
    return y_


def x_graph(log, ip):
    x_ = []
    for i in log[ip]:
        x_.append(i[0])
    return x_


filename_ = 'log.log'

ip_inp = input('Введите IP-адрес для построения графика: ')
y = y_graph(get_data(filename_), ip_inp)
x = x_graph(get_data(filename_), ip_inp)

plt.plot(x, y)
plt.xticks(rotation=75)
plt.show()
