import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

values = list(range(1, 101))
squares = [value**2 for value in values]

#plt.scatter(values, squares, c='red', edgecolor='none', s=30) # 实参s设置了绘制图形时使用的点的尺寸
# 使用颜色映射
# 将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。下面代码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色
plt.scatter(values, squares, c=squares, cmap=plt.cm.Blues, edgecolor='none', s=30) 

# 设置每个坐标轴的取值范围
plt.axis([0, 110, 0, 11000])
# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square of Value", fontsize=16)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14) 

plt.show()
#要让程序自动将图表保存到文件中，可将对plt.show()的调用替换为对plt.savefig()的调用
#plt.savefig('squares_plot.png')#, bbox_inches='tight') # 第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，可省略这个实参

"""
要了解pyplot中所有的颜色映射，请访问http://matplotlib.org/，单击Examples，向下滚动
到Color Examples，再单击colormaps_reference。
"""