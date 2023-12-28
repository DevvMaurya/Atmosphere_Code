import pandas as pd
import re
import subprocess as sb
import sys

cmd = 'dir /B /A-D ' + str(sys.argv[1])
# print(sys.argv[1])
try:
    data = sb.run(cmd,shell=True,capture_output=True,text=True)
    data = data.stdout.splitlines()
except Exception as e:
    print(f'{e}')

csv_files = []
patr_csv = r'(?i).csv$'
for item in data:
    match_csv = re.search(pattern=patr_csv,string=item)
    if match_csv:
        print(item)
        csv_files.append(pd.read_csv(f'{sys.argv[1]}\{str(item)}'))
# print(len(csv_files))
merge_csv = pd.concat(csv_files,ignore_index=True)
merge_csv.to_csv(f'{str(sys.argv[1])[:-5]}sample.csv',index=False)

# data_csvs= [
#     pd.read_csv('C:\\Users\\Admin\\Documents\\Atmosphere\\2250\\2250\\Parselsmr_2250_0_00_SVM05030012.csv'),
#     pd.read_csv('C:\\Users\\Admin\\Documents\\Atmosphere\\2250\\2250\\Parselsmr_2250_0_01_SVM05030012.csv')
# ]