import sys
'''
sys module is imported inorder to take command line argument which will use to take path for others machine.
'''

import subprocess
'''
subprocess imported to run command line commands.
'''
cmd = 'dir /B /A-D '+ str(sys.argv[1])
# print(sys.argv[1])
try:
    data = subprocess.run(cmd,shell=True,capture_output=True,text=True)

    data = data.stdout.splitlines()
except Exception as e:
    print(f'{e}')


'''
Below code is to automate the convertion if the gps file to csv file.
'''
import re

pattern_gps = r"(?i).gps$"
for item in data:
    match_gps = re.search(pattern_gps,item)
    if match_gps:
        item = str(item)
        cmd_gps_to_csv = f'cd "{sys.argv[1]}" && parseismr all {item} Parselsmr_{item[:-4]}.csv'

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