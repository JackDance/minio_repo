## 一、介绍
实现对象存储系统minio的创建，连接，存储桶的创建删除，文件的上传，下载等功能

## 二、minio的安装和启动
下载安装包：
```
sudo wget https://dl.min.io/server/minio/release/linux-amd64/minio
```
赋予访问权限
```
chmod +xminio
```
启动minio
```
./minio server /path/to/your/data/save/path
```
启动成功后，根据控制台的输出提示，访问提示的链接，输入提示的账号密码即可。

## 三、minio的连接，存储桶的创建，删除，文件的上传和下载
这里使用python代码的方式实现。详见该仓库code，各个文件的解释如下：
```
minioConig.py # 连接Minio文件存储服务器
minioBucketBase.py # Python操作存储桶
minioObjectBase.py # Python操作文件
```
