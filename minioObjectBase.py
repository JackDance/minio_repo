#!/usr/bin/python
# -*- coding: UTF-8 -*-


from minioConfig import minioClient
from minio.error import InvalidResponseError
import os
"""
Python操作文件
"""

class Object:

    # 从桶中下载一个对象txt、csv文件都可以
    def load_object(self):
        try:
            data = minioClient.get_object('data', 'version.txt') # 参数为bucket_name, object_name
            file_path = os.path.join(os.path.dirname(__file__), 'data', 'version.txt')
            with open(file_path, 'wb') as file_data:
                for d in data.stream(32 * 1024):
                    file_data.write(d)
            print("Sussess")
        except InvalidResponseError as err:
            print(err)

    # 下载一个对象的指定区间的字节数组
    def load_partial_object(self):
        try:
            data = minioClient.get_partial_object('testfiles', '123.txt', 2, 8)
            with open('./load_files/123_new.txt', 'wb') as file_data:
                for d in data:
                    file_data.write(d)
            print("Sussess")  # 部分出现乱码
        except InvalidResponseError as err:
            print(err)

    # 下载并将文件保存到本地
    # 主要用该函数实现下载（从minio下载到本地）
    def fget_object(self, bucket_name, file_path):
        try:
            print(minioClient.fget_object(bucket_name, os.path.split(file_path)[-1], file_path)) # bucket_name, object_name, file_path
            print("Success")
        except InvalidResponseError as err:
            print(err)

    # 拷贝对象存储服务上的源对象到一个新对象
    # 注：该API支持的最大文件大小是5GB
    # 可通过copy_conditions参数设置copy条件
    # 经测试copy复制28M的文件需要663ms; 1.8G的压缩包需要53s
    def get_copy_object(self):
        try:
            copy_result = minioClient.copy_object("pictures", "123.jpg",
                                                  "/testfiles/123.jpg"
                                                  )
            print(copy_result)
        except InvalidResponseError as err:
            print(err)

    # 添加一个新的对象到对象存储服务
    """
    单个对象的最大大小限制在5TB。put_object在对象大于5MiB时，自动使用multiple parts方式上传。
    这样，当上传失败时，客户端只需要上传未成功的部分即可（类似断点上传）。
    上传的对象使用MD5SUM签名进行完整性验证。
    """

    def upload_object(self, bucket_name, local_file_path):
        try:
            with open(local_file_path, 'rb') as file_data:
                file_stat = os.stat(local_file_path)
                # print("file_stat: ", file_stat)
                minioClient.put_object(bucket_name, os.path.split(local_file_path)[-1],
                                       file_data, file_stat.st_size) # bucket_name, object_name, data, length
            print("Sussess")
        except InvalidResponseError as err:
            print(err)

    # 通过文件上传到对象中
    # 主要用该函数实现上传（从本地上传到minio）
    def fput_object(self, bucket_name, local_file_path):
        try:
            print(minioClient.fput_object(bucket_name, os.path.split(local_file_path)[-1], local_file_path)) # bucket_name, object_name, file_path
            print("Sussess")
        except InvalidResponseError as err:
            print(err)

    # 获取对象的元数据
    def stat_object(self):
        try:
            print(minioClient.stat_object('pictures', '123.txt'))
        except InvalidResponseError as err:
            print(err)

    # 删除对象
    def remove_object(self):
        try:
            minioClient.remove_object('pictures', '234.jpg')
            print("Sussess")
        except InvalidResponseError as err:
            print(err)

    # 删除存储桶中的多个对象
    def remove_objects(self):
        try:
            objects_to_delete = ['123.txt', 'long_lat.csv']
            for del_err in minioClient.remove_objects('testfiles', objects_to_delete):
                print("Deletion Error: {}".format(del_err))
            print("Sussess")
        except InvalidResponseError as err:
            print(err)

    # 删除一个未完整上传的对象
    def remove_incomplete_upload(self):
        try:
            minioClient.remove_incomplete_upload('testfiles', '123.jpg')
            print("Sussess")
        except InvalidResponseError as err:
            print(err)


if __name__ == '__main__':
    bucket_name = 'data'
    local_file_path = '/home/jackdance/Downloads/paddlepaddle_gpu-2.3.0-cp37-cp37m-linux_x86_64.whl'
    # Object().fput_object(bucket_name, local_file_path)
    Object().fget_object(bucket_name, local_file_path)
