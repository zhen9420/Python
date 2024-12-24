import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 100

fig, ax = plt.subplots(figsize=(5, 4))  # 设置图表大小

ax.axis('tight')
ax.axis('off')

# 创建表格数据
table_data = [
    ['总人数', 1],
    ['满分值', 1],
    ['最大值',1],
    ['最小值',1],
    ['平均值', 1],
    ['标准差', 1],
    ['差异系数', 1],
    ['难度', 1],
    ['alpha系数', 1],
    ['标准误差', 1],
    ['中位数', 1],
    ['众数', '1,2'],
    ['偏度', 1],
    ['峰度', 1]
]

# 创建表格
table = ax.table(cellText=table_data, colLabels=None, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)

plt.title('总分分析表',x=0.5,y=0.89)

plt.show()
