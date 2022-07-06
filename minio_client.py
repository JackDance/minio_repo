from minio import Minio
from minio.error import InvalidResponseError
import os
"""
python连接服务器并上传文件
"""

# 使用endpoint， access key和secret key来初始化minioClient对象
minioClient = Minio('192.168.3.25:9000', # 端口号应为9000
                    access_key='minioadmin',
                    secret_key='minioadmin',
                     secure=False,
                    )


file_path = r'/home/jackdance/Downloads/version.txt' # 需是文件，不能是文件夹
file_name = file_path.split('/')[-1]
try:
    minioClient.fput_object('jack', 'version.txt', file_path)
    print('success')
except InvalidResponseError as e:
    print(e)