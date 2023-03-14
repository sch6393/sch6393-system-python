# 로그
import os
from datetime import datetime

# 오늘 날짜 로그 파일
file_log_today = os.getcwd() + '\Log\\' + datetime.today().strftime('%Y%m%d') + '.log'

def writeLog(type, msg):
    # 로그 쓰기 전 파일 체크
    checkLogFile()
    # print(msg)
    
    # Append
    f = open(file_log_today,'a')
    f.write('[' + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + '] (' + type + ')	' + msg)
    f.write('\n')
    f.close()


# 오늘 날짜 로그 파일이 있는지 확인
def checkLogFile():
    # 없다면 생성
    if not os.path.isfile(file_log_today):
        print('No File! : ' + file_log_today)
        f = open(file_log_today, 'w')
        f.close()
        return False
    else:
        return True
