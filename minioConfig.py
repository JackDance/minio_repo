from minio import Minio

"""
连接Minio文件存储服务器
"""
# 使用endpoint， access key和secret key来初始化minioClient对象
minioClient = Minio('192.168.3.25:9000', # 端口号应为9000
                    access_key='minioadmin',
                    secret_key='minioadmin',
                     secure=False,
                    )