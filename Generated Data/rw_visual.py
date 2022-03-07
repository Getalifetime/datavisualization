import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(10000)
    rw.fill_walk()

    # 函数figure()用于指定图表的宽度、高度、分辨率和背景色。
    # 你需要给形参figsize指定一个元组，向matplotlib指出绘图窗口的尺寸，单位为英寸。
    # Python假定屏幕分辨率为80像素/英寸。如果你知道自己的系统的分辨率，可使用形参dpi向figure()传递该分辨率，以有效地利用可用的屏幕空间，
    plt.figure(dpi=128, figsize=(10, 6)) 

    # 隐藏坐标轴。需放在scatter之前，否则不能正确画图
    current_axes = plt.axes()
    current_axes.get_xaxis().set_visible(False)
    current_axes.get_yaxis().set_visible(False)

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
        edgecolor='none', s=2)

    # plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=50) 
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
        s=50)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running != 'y':
        break