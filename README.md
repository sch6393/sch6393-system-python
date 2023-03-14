# sch6393-system-python
sch6393-system-python

<br>

# Server
* https://sch6393-system-sch6393.koyeb.app/

<br>

# Web Page
* https://sch6393-system.web.app/
* https://sch6393-system.firebaseapp.com/

<br>

# TimeZone
* Asia/Tokyo (GMT+9)

<br>

# Sample Test
* Directory
  ```
  ├ sch6393-system-UIP
  │  ├ ...
  │  ├ ApiKey
  │  │  └ sch6393-system.key  ← 1
  │  ├ Function
  │  ├ Log
  │  ├ Process
  │  │  ├ Process.py          ← 2
  │  │  └ Sample.py           ← 2
  │  ├ .gitignore
  │  ├ ...
  ```

1. [Download key file](#get-useruid-apikey) and put key file in `ApiKey` folder

1. Put `Process.py` file in `Process` folder, `Sample.py` file in json directory folder
    * [Process.py](./Process/Process.py)
    * [Sample.py](./Process/Sample.py)

1. Create sample task and write sample script in [Add Task](#add-task-script)
    ```JSON
    {
      "type": "py",
      "py": "C:\\Sample.py"
    }
    ```

<br>

# Parsing Script
```py
strtmp = json.dumps(array_json[0])
dicttmp = json.loads(strtmp)
str_script = dicttmp.get('script')
dict_script = json.loads(str_script)

print(dict_script.get('py'))
print(dict_script.get('no'))
```

<br>

# API
* Get Queue
  * Info
    |Name|Value|
    |-|-|
    |URL|`https://sch6393-system-sch6393.koyeb.app/api/queue/first`|
    |Method|POST|

  * Request Parameters
    |Name|Type|Description|
    |-|-|-|
    |userUid|String||
    |apikey|String||
    |factor|String|Client Classification|

  * Response
    ```JSON
    [
      {
        "seqqueue":"----------------------",
        "id":"----------------------------",
        "script":"{
                    "a": "a",
                    "b": "b",
                    "c": "c"
                  }"
      }
    ]
    ```

<br>

# Get userUid, apikey
* [Web Page](#Web-Page) ➞ About
  * Download key file
    ```
    userUid
    apikey
    factor
    ```
    >File name : `sch6393-system.key`

<br>

# Add Task Script
* [Web Page](#Web-Page) ➞ Task List ➞ Add Task

<br>

# Add iTask Script
* [Web Page](#Web-Page) ➞ iTask List ➞ Add iTask

<br>

```
# Group (Task)
* [Web Page](#Web-Page) ➞ Dash Board ➞ Task ➞ Add Task ➞ Group ON/OFF
* Execute in order by registered iTasks on group (Limit 5 iTasks)
  >Queues, Tasks are Displayed yellow by executed in group
```
>Suspend

<br>

# Crontab (Task)
```sh
# *       *     *    *      *
# Minutes Hours Days Months Week

# Example
# At minute 30 past hour 11 and 15 on every day-of-week from Monday through Friday
30 11,15 * * 1-5

# At minute 0 past hour 0 and 12 on day-of-month 1 in every 2nd month
0 0,12 1 */2 *
```
>https://crontab.guru/

<br>
