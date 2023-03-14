import requests
import time

# import pdb
# pdb.set_trace()

from Function import Init
from Function import Log
from Global import Global
from Process import Process

# MAIN
if __name__ == '__main__':
    # 초기화
    if Init.init():
        print('Success to Init!')
        Log.writeLog('info', 'Success to Init!')
        # print(Global.g_userid)
        # print(Global.g_apikey)
        # print(Global.g_factor)

        try:
            while True:
                print('Requset Queue...')
                Log.writeLog('info', 'Requset Queue...')

                # Https Requests
                data = {'userUid': Global.g_userid, 'apikey': Global.g_apikey, 'factor': Global.g_factor}
                response = requests.post(Global.g_api_url, data=data)
                """
                response.request            # request 객체
                response.status_code        # 응답 코드
                response.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발생
                response.json()             # 응답 형식이 json일 경우 변환
                """
                # print(response.status_code)
                # print(response.content)
                print('Code : ' + str(response.status_code) + ' / Return : ' + str(response.content))
                Log.writeLog('info', 'Code : ' + str(response.status_code) + ' / Return : ' + str(response.content))

                if response.status_code == 204:
                    print('Wait...')
                    Log.writeLog('info', 'Wait...')
                    time.sleep(Global.g_time_sleep)
                elif response.status_code == 200:
                    # json 파싱
                    Process.exec(response.json())
                elif str(response.status_code).startswith('4'):
                    print('Fail to Authentication!')
                    Log.writeLog('error', 'Fail to Authentication!')
                    exit()
                else :
                    print('Fail to Http Request!')
                    Log.writeLog('error', 'Fail to Http Request!')
                    exit()

        except OSError:
            print('Error: Http Request Execption!')
            Log.writeLog('error', 'Http Request Execption!')
    else:
        print('Fail to Init!')
        Log.writeLog('error', 'Fail to Init!')

