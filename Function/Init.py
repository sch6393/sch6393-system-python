# 초기화
import os

from . import Log         # 로그
from Global import Global # Global

def init():
    checkFolder()
    return checkApiKey()


# 초기 폴더 체크
def checkFolder():
    try:
        print ('info: checkFolder!')
        Log.writeLog('info', 'checkFolder!')

        # 없다면 생성
        if not os.path.exists(Global.g_directory_apikey):
            os.makedirs(Global.g_directory_apikey)
            Log.writeLog(Global.g_directory_apikey)

        if not os.path.exists(Global.g_directory_log):
            os.makedirs(Global.g_directory_log)
            Log.writeLog(Global.g_directory_apikey)

        if not os.path.exists(Global.g_directory_process):
            os.makedirs(Global.g_directory_process)
            Log.writeLog(Global.g_directory_apikey)

    except OSError:
        print ('Error: checkFolder!')
        Log.writeLog('error', 'checkFolder!')


# 키파일 체크
def checkApiKey():
    try:
        print ('info: checkApiKey!')
        Log.writeLog('info', 'checkApiKey!')

        # 없다면 에러
        if not os.path.isfile(Global.g_file_apikey):
            return False
        # 있다면 파일 읽기
        else:
            file = open(Global.g_file_apikey, 'r')
            i = 0
            while True:
                line = file.readline()
                # print(i)
                # print(line)

                if i == 0:
                    Global.g_userid = line.strip()

                if i == 1:
                    Global.g_apikey = line.strip()

                if i == 2:
                    Global.g_factor = line.strip()

                if not line:
                    break

                i = i + 1
            file.close()
            return True

    except OSError:
        print ('Error: checkApiKey!')
        Log.writeLog('error', 'checkApiKey!')
