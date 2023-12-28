import subprocess

# Define the command you want to run
# cmd = 'dir'
# cmd = 'dir /B /A-D ' #/B for name only , /A-D only for files not directories...~
cmd = 'dir /B /A-D '+'C:\\Users\\Admin\\Documents\\Atmosphere\\2250\\2250'
try:
    data = subprocess.run(cmd,shell=True,capture_output=True,text=True)

    #convetred into form of list
    data = data.stdout.splitlines()
    print(data)
    # print(type(data))
except Exception as e:
    print(f'{e}')


'''
Below code is to automate the convertion if the gps file to csv file.
'''
import re

pattern_gps = r"(?i).gps$"
# pattern_sli = r"(?i).sli$"
for item in data:
    match_gps = re.search(pattern_gps,item)
    # match_sli = re.search(pattern_sli,item)
    if match_gps:
        # print(item)
        item = str(item)
        # fname ='C:\\Users\\Admin\\Documents\\Atmostsphere\\Converted\\'+item+'.csv'
        cmd_gps_to_csv = f'cd "C:\\Users\\Admin\\Documents\\Atmosphere\\2250\\2250" && parseismr all {item} Parselsmr_{item[:-4]}.csv'

        try:
            subprocess.run(cmd_gps_to_csv,shell=True)
        except ExceptionGroup as e:
            print(f'Command execution error : {e}')

        print(cmd_gps_to_csv)
'''
're' is python module which is used for regex accomplicement 
synx -> r'flags'
(?i) -> is for ignore case-sensitivity
xyz$ -> for matching extention 
'''