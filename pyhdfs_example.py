#encoding=utf8
import pyhdfs
'''
in docker serve 192...4

out docker ser 192.168.28.195 like jupyter serve maybe
'''
#fs=pyhdfs.HdfsClient(hosts='172.18.0.4,50070') 
#fs=pyhdfs.HdfsClient(hosts='192.168.28.195,50070')

fs=pyhdfs.HdfsClient(hosts='192.168.28.195')

print(fs.listdir("/"))
print(fs.get_active_namenode())
print(fs.get_home_directory())


# fs=Client("192.168.28.183:50070")
# print(dir(fs))
# # print(fs.status('/'))
print(fs.listdir("/user"))

# 从本地上传文件至集群
print('from local upload files')
fs.copy_from_local( "/home/amis/Documents/tsl/hadoop_example/wordcounts.txt",'/user/wordcounts2.txt')

#/home/amis/Documents/tsl/hadoop_example
# 从本地上传文件至集群之后，集群的目录
print("After copy_from_local")
print(fs.listdir("/user"))

