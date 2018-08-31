#股票相关
import pandas as pd
import tushare as ts
df = ts.get_industry_classified()

print(df)
