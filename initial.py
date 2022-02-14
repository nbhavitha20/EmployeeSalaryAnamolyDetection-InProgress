import pandas as pd
import pandas_profiling as pp
from timeit import timeit
df = pd.read_excel('EmpList.xlsx')

#print(df.info())

profile = pp.ProfileReport(df)

profile.to_file("profileOutput.html")


