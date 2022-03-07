import csv
from datetime import datetime

from matplotlib import pyplot as plt

#filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f) # 创建一个与该文件相关联的阅读器（reader）对象
    header_row = next(reader) # 函数next()，调用它并将阅读器对象传递给它时，它将返回文件中的下一行。只调用了next()一次，因此得到的是文件的第一行
    """
    for index, column_header in enumerate(header_row): # enumerate()获取每个元素的索引及其值
        print(index, column_header)
    """

    # 获取最高气温
    dates, highs, lows = [], [], []
    for row in reader: # 阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            # print(current_date)
            high_temp = int(row[1])
            low_temp = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high_temp)           
            lows.append(low_temp)
    #print(dates)
    #print(highs)


    # 绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.6) # Alpha值为0表示完全透明，1（默认设置）表示完全不透明。
    plt.plot(dates, lows, c='blue', alpha=0.6)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

    # 设置图形格式
    plt.title('Daily high and low temperatures, 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # 绘制斜的日期标签，以免它们彼此重叠
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

"""
    模块datetime中设置日期和时间格式的实参
    实 参       含 义
    %A          星期的名称，如Monday 
    %B          月份名，如January 
    %m          用数字表示的月份（01~12）
    %d          用数字表示月份中的一天（01~31）
    %Y          四位的年份，如2015 
    %y          两位的年份，如15 
    %H          24小时制的小时数（00~23）
    %I          12小时制的小时数（01~12）
    %p          am或pm 
    %M          分钟数（00~59）
    %S          秒数（00~61）
"""