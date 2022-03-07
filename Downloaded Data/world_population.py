import json

from pygal.style import RotateStyle

from pygal_maps_world.maps import World
from pygal_maps_world.i18n import COUNTRIES

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

"""
Pygal中的地图制作工具要求数据为特
定的格式：用国别码表示国家，以及用数字表示人口数量。处理地理政治数据时，经常需要用到几个标准化国别码集。
population_data.json中包含的是三个字母的国别码，但Pygal使用两个字母的国别码。
"""
def get_country_code(country_name):
    '根据国家名称获取两字母的国家码'
    """
    for country_code in sorted(COUNTRIES.keys()):
        print(country_code, COUNTRIES[country_code])
    """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


# 制作各国2010年人口数量的字典，键值为国家码
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": "+ str(population))
            cc_populations[code] = population
        else:
            print('ERROR - ' + country_name) 


# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items(): 
    if pop < 10000000: 
        cc_pops_1[cc] = pop 
    elif pop < 1000000000: 
        cc_pops_2[cc] = pop 
    else: 
        cc_pops_3[cc] = pop 
# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3)) 


"""
创建RotateStyle这个类的实例时，需要提供一个实参——十六进制的RGB颜色；Pygal将根据指定的颜色为每组选择颜色。
十六进制格式的RGB颜色是一个以井号（#）打头的字符串，后面跟着6个字符，
其中前两个字符表示红色分量，接下来的两个表示绿色分量，最后两个表示蓝色分量。
每个分量的取值范围为00（没有相应的颜色）~FF（包含最多的相应颜色）。
这里使用的颜色值（#336699）混合了少量的红色（33）、多一些的绿色（66）和更多一些的蓝色（99），
它为RotateStyle提供了一种淡蓝色基色
在线搜索hex color chooser（十六进制颜色选择器），可找到让你能够尝试选择不同的颜色并显示其RGB值的工具。
"""
wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
#wm = World()
wm.title = 'World Population in 2010, by Country'
#wm.add('2010', cc_populations) 
wm.add('0-10m', cc_pops_1) 
wm.add('10m-1bn', cc_pops_2) 
wm.add('>1bn', cc_pops_3) 
wm.render_to_file('world_population.svg') 



