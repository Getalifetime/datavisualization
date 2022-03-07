import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 这个调用返回GitHub当前托管了多少个Python项目，还有有关最受欢迎的Python仓库的信息。
# 第一部分（https://api.github.com/）将请求发送到GitHub网站中响应API调用的部分；
# 接下来的一部分（search/repositories）让API搜索GitHub上的所有仓库。

# repositories后面的问号指出我们要传递一个实参。q表示查询，而等号让我们能够开始指定查询（q=）。
# 通过使用language:python，我们指出只想获取主要语言为Python的仓库的信息。
# 最后一部分（&sort=stars）指定将项目按其获得的星级进行排序。
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# 执行API调用，返回json格式的信息
r = requests.get(url)
print('Status code: ', r.status_code)

# 将API响应存储到一个变量中
response_dict = r.json()

# print(response_dict.keys())
# print("total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
# print("Repositories returned:", len(repo_dicts)) 

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in repo_dict.keys():#sorted(repo_dict.keys()):
#     print(key)
# print("\nSelected information about each repository:")

names, plot_dicts_list = [], []
for repo_dict in repo_dicts:
    # print('\nName:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count']) 
    # print('Repository:', repo_dict['html_url'])
    # print('Created:', repo_dict['created_at']) 
    # print('Updated:', repo_dict['updated_at']) 
    # print('Description:', repo_dict['description'])

    # 自定义工具提示
    plot_dict = {
        'value': repo_dict['stargazers_count'], # Pygal根据与键'value'相关联的数字来确定条形的高度，并使用与'label'相关联的字符串给条形创建工具提示。
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'], # Pygal根据与键'xlink'相关联的URL将每个条形都转换为活跃的链接。
    }

    names.append(repo_dict['name'])
    plot_dicts_list.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24 # 图表标题字体大小
my_style.label_font_size = 14 # 副标签字体大小。在这个图表中，副标签是x轴上的项目名以及y轴上的大部分数字
my_style.major_label_font_size = 18 # 主标签字体大小。主标签是y轴上为5000整数倍的刻度

my_config = pygal.Config()
my_config.style = my_style
my_config.x_label_rotation = 45 #让标签绕x轴旋转45度
my_config.show_legend = False # 隐藏图例
my_config.truncate_label = 15 # 将较长的项目名缩短为15个字符
my_config.show_y_guides = False # 隐藏图表中的水平线
my_config.width = 1000 # 自定义图表宽度, 让图表更充分地利用浏览器中的可用空间


# chart = pygal.Bar(sytle=my_style, x_label_rotation=45, show_legend=False) 
chart = pygal.Bar(my_config)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts_list)
chart.render_to_file('Most Starred Python Repos.svg')