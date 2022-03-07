import matplotlib.pyplot as plt

values = [0, 1, 2, 3, 4, 5, 6]
squares = [0, 1, 4, 9, 16, 25, 36]
plt.plot(values, squares, linewidth=3)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=18)
plt.ylabel("Square of Value", fontsize=18)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()