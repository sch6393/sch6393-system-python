# Process (Example)
import json
import subprocess

from Function import Log

def exec(array_json):
    # print('exec')
    # print(array_json)
    # print(type(array_json))
    '''
    [{'seqqueue': '0000', 'id': '----------------------------', 'script': '{\n  "py": "C:\\\\Test.py",\n  "no": "5"\n}'}]
    <class 'list'>
    '''
    # print(array_json[0])
    # print(type(array_json[0]))
    '''
    {'seqqueue': '0000', 'id': '----------------------------', 'script': '{\n  "py": "C:\\\\Test.py",\n  "no": "5"\n}'}
    <class 'dict'>
    '''
    strtmp = json.dumps(array_json[0])
    # print(strtmp)
    # print(type(strtmp))
    '''
    {"seqqueue": "0000", "id": "----------------------------", "script": "{\n  \"py\": \"C:\\\\Test.py\",\n  \"no\": \"5\"\n}"}
    <class 'str'>
    '''
    dicttmp = json.loads(strtmp)
    # print(dicttmp)
    # print(type(dicttmp))
    '''
    {'seqqueue': '0000', 'id': '----------------------------', 'script': '{\n  "py": "C:\\\\Test.py",\n  "no": "5"\n}'}
    <class 'dict'>
    '''
    # str_script = dicttmp['script']
    str_script = dicttmp.get('script')
    # print(str_script)
    # print(type(str_script))
    '''
    {
        "py": "C:\\Sample.py",
        "no": "5"
    }
    <class 'str'>
    '''

    dict_script = json.loads(str_script)
    # print(dict_script.get('py'))
    file_parameter = dict_script.get('py') + ' ' + dict_script.get('no') + ' 3'
    # print(file_parameter)

    try:
        print('Error: Process Start! : ' + str(dicttmp.get('seqqueue')))
        Log.writeLog('info', 'Process Start! : ' + str(dicttmp.get('seqqueue')))

        # Execute the file
        subprocess.call(file_parameter, shell = True)

    except OSError:
        print('Error: Process Fail! (exec)')
        Log.writeLog('error', 'Process Fail! (exec)')
