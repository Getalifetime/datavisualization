from logging import PercentStyle
import pygal
"""
使用Python可视化包Pygal来生成可缩放的矢量图形文件(.svg)
对于需要在尺寸不同的屏幕上显示的图表，这很有用，因为它们将自动缩放，以适合观看者的屏幕。
如果你打算以在线方式使用图表，请考虑使用Pygal来生成它们，这样它们在任何设备上显示时都会很美观。
"""

from die import Die

# 创建一个D6骰子
die1 = Die()
die2 = Die()


# 投掷骰子，将结果存储在一个列表中
roll_times = 1000
results1 = []
results2 = []
add_results = []
for roll_num in range(roll_times):
    result1 = die1.roll()
    result2 = die2.roll()
    results1.append(result1)
    results2.append(result2)
    add_results.append(result1 + result2)

# 分析结果
frequencies1 = []
frequencies2 = []
for value in range(1, die1.num_sides+1):
    frequency1 = results1.count(value)
    frequency2 = results2.count(value)
    frequencies1.append(frequency1)
    frequencies2.append(frequency2)

sum_frequencies = []
percents = []
x_labels = []
for value in range(2, 13):
    x_labels.append(str(value))
    sum_frequency = add_results.count(value)
    sum_frequencies.append(sum_frequency)
    percents.append(sum_frequency / roll_times * 100)

# 对结果进行可视化
hist1 = pygal.Bar()
hist1.title = "Results of rolling two D6 1000 times."
hist1.x_labels = ['1', '2', '3', '4', '5', '6']
hist1.x_title = "Result"
hist1.y_title = "Frequency of Result"

hist1.add('D6-1', frequencies1)
hist1.add('D6-2', frequencies2)    
hist1.render_to_file('die_roll_bar.svg')

pie_chart = pygal.Pie()
pie_chart.title = 'Sum results of rolling two D6 1000 times. (in %)'
for i in range(11):
    pie_chart.add(x_labels[i], percents[i])

pie_chart.render_to_file('die_roll_pie.svg')


hist2 = pygal.Bar()
hist2.title = "Sum results of rolling two D6 1000 times."
hist2.x_labels = x_labels
hist2.x_title = "Result"
hist2.y_title = "Frequency of Result"

hist2.add('D6 + D6', sum_frequencies)    
hist2.render_to_file('die_add_bar.svg')

