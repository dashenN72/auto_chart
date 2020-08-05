# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 22:51
# @Author  : dashenN72
"""
demo for chat test
"""

from pyecharts import Bar
from pyecharts import Line
from pyecharts import Gauge
from pyecharts import Pie
from pyecharts import Funnel
# c导入柱状图-Bar
# 设置行名
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# 设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# 设置柱状图的主标题与副标题
bar = Bar("柱状图", "一年的降水量与蒸发量")
# 添加柱状图的数据及配置项
bar.add("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
bar.add("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])
# 生成本地文件（默认为.html文件）
bar.render()


# 折线图
cities = ["合肥", "芜湖", "南京", "北京", "天津", "马鞍山", "杭州", "扬州", "苏州", "亳州"]
data3 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0]
# data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8]
line = Line("气温变化折线图", '2018-4-16', width=1200, height=600)
line.add("最高气温", cities, data3, mark_point=['average'], is_datazoom_show=False, is_label_show=True)
# line.add("最低气温", cities, data2, mark_line=['average'], is_smooth=True)
# line.render('Line-High-Low.html')
line.render(path='折线图.gif')

# 仪表盘图
gu = Gauge("仪表盘图")
gu.add("指标", "达标", 85)
gu.render("Guage-eg.html")

# 导入饼图Pie
# 设置主标题与副标题，标题设置居中，设置宽度为900
pie = Pie("饼状图", "一年的降水量与蒸发量", title_pos='center', width=900)
# 加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示
pie.add("降水量", columns, data1, center=[25, 50], is_legend_show=True)
# 加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签
pie.add("蒸发量", columns, data2, center=[75, 50], is_legend_show=False, is_label_show=True)
# 保存图表
pie.render("pie.html")

# 漏斗图+图片
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add("商品", attr, value, is_label_show=True,
           label_pos="inside", label_text_color="#fff")
funnel.render(path='./漏斗图01.png')