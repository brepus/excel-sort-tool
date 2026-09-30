import pandas as pd

# 读取 Excel
file_path = r"D:\pythontest\source.xlsx"  # 根据实际文件名改
df = pd.read_excel(file_path)

# 确保 C、D 列是 datetime 类型
df["进入时间"] = pd.to_datetime(df["进入时间"])
df["出时间"] = pd.to_datetime(df["出时间"])

# 计算时间差（D - C），单位：秒
df["时间差"] = (df["出时间"] - df["进入时间"]).dt.total_seconds()

# 按时间差倒序排列
df_sorted = df.sort_values(by="时间差", ascending=False)

# 输出到新文件
df_sorted.to_excel(r"D:\pythontest\source_sorted.xlsx", index=False)

print("处理完成！")