import rstr
import pandas as pd

# 正则表达式 [0-9]{14} 表示匹配14位数字
exam_number_regex = r'[0-9]{14}'
id_number_regex = r'[0-9]{18}'

# 生成100个14位数字的考号和18位数字的身份证号
data = {
    "考号": [rstr.xeger(exam_number_regex) for _ in range(100)],
    "身份证号": [rstr.xeger(id_number_regex) for _ in range(100)],
    "所在地市":[]
}

# 将数据放入DataFrame
df = pd.DataFrame(data)

# 导出为Excel文件
df.to_excel("random_data.xlsx", index=False)

print("随机数据已导出到 random_data.xlsx")
