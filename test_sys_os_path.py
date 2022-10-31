

import sys
import os
# BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)


import pprint



pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pardir)
#  ['/mnt/A/bin/app',
#  '/usr/local/python3/lib/python38.zip',
#  '/usr/local/python3/lib/python3.8',
#  '/usr/local/python3/lib/python3.8/lib-dynload',
#  '/usr/local/python3/lib/python3.8/site-packages']
pprint.pprint(sys.path)


#
###################### 对于引入上一级目录的解决对策################
# pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(pardir)
###################### 对于引入上一级目录的解决对策################
# pprint.pprint(sys.path) ------>  from binservice.config.info import s_info  ---> ok
# ['/mnt/A/bin/app',
#  '/usr/local/python3/lib/python38.zip',
#  '/usr/local/python3/lib/python3.8',
#  '/usr/local/python3/lib/python3.8/lib-dynload',
#  '/usr/local/python3/lib/python3.8/site-packages',
#  '/mnt/A/bin']

# sys.path.append(os.path.abspath(os.path.join(__file__,"/../..","/")))
# pprint.pprint(sys.path)
#



# sys.path.append(__dir__)

# os.path.dirname、os.path.abspath和sys.path.append
# 上一级，上上级都可以引入了。算是比较彻底的解决了。记得增加__init__.py
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(__dir__,"../..")))

pprint.pprint(sys.path)

from service.config.info import s_info


print(s_info)
# ['/mnt/A/bin/app',
#  '/usr/local/python3/lib/python38.zip',
#  '/usr/local/python3/lib/python3.8',
#  '/usr/local/python3/lib/python3.8/lib-dynload',
#  '/usr/local/python3/lib/python3.8/site-packages',
#  '/mnt/A/bin']
# ['/mnt/A/bin/app',
#  '/usr/local/python3/lib/python38.zip',
#  '/usr/local/python3/lib/python3.8',
#  '/usr/local/python3/lib/python3.8/lib-dynload',
#  '/usr/local/python3/lib/python3.8/site-packages',
#  '/mnt/A/bin',
#  '/mnt/A']
# asdfadfafdasfa

# /mnt/A
# ├── bin
# │   ├── app
# │   │   ├── __init__.py
# │   │   └── test_path.py
# │   ├── binservice
# │   │   └── config
# │   │       ├── info.py
# │   │       ├── __init__.py
# │   │       └── __pycache__
# │   │           ├── info.cpython-37.pyc
# │   │           ├── info.cpython-38.pyc
# │   │           ├── __init__.cpython-37.pyc
# │   │           └── __init__.cpython-38.pyc
# │   ├── __init__.py
# │   └── __pycache__
# │       └── __init__.cpython-37.pyc
# ├── __init__.py
# └── service
#     ├── config
#     │   ├── info.py
#     │   ├── __init__.py
#     │   └── __pycache__
#     │       ├── info.cpython-37.pyc
#     │       ├── info.cpython-38.pyc
#     │       ├── __init__.cpython-37.pyc
#     │       └── __init__.cpython-38.pyc
#     ├── __init__.py
#     └── __pycache__
#         ├── __init__.cpython-37.pyc
#         └── __init__.cpython-38.pyc