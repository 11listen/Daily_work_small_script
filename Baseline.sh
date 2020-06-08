#!/bin/bash

#更改权限
#chmod +x Baseline.sh

#运行
#./Baseline.sh

#当前目录下会生成BaseLine.txt

echo -e "\033[31m Baseline \033[0m\n"

echo -e "\033[31m author:1isten \033[0m\n"

#查看IP
net=`ifconfig eth0 | grep 'inet' | awk -F " " 'NR==1{print $2}'`

ip=`echo -e "this server ip:$net\n"`

#查看服务器版本
version=`cat /etc/issue`

ServerVersion=`echo -e "this server is:$version"`
#身份鉴别

#查看用户
user=`cat /etc/passwd`

#查看密码复杂度
password=`cat /etc/login.defs`

#查看登录失败
LoginFailed=`cat /etc/pam.d/sshd`

#查看是否限制root
LimitRoot=`cat /etc/ssh/sshd_config`

#查看最后100条登录认证日志
log=`tail -n 100 /var/log/auth.log`

#查看开放端口
OpenPort=`netstat -antp | awk '{print $4}' | grep "0.0.0.0"`

#查看主机限制
LimitHost=`cat /etc/hosts.deny`

#查看防火墙规则
iptables=`iptables -L`

Time=`date`

printf "$Time\n\n" this time is: >> BaseLine.txt

printf "$ip\n\n" this server ip: >> BaseLine.txt

printf "$ServerVersion\n\n" this server ip: >> BaseLine.txt

printf "%s\n $user\n\n" "=======/etc/passwd======" >> BaseLine.txt

printf "%s\n $password\n\n" "=======/etc/login.defs======" >> BaseLine.txt

printf "%s\n $LoginFailed\n\n" "=======/etc/pam.d/sshd======" >> BaseLine.txt

printf "%s\n $LimitRoot\n\n" "=======/etc/ssh/sshd_config======" >> BaseLine.txt

printf "%s\n $log\n\n" "=======/var/log/auth.log=======" >> BaseLine.txt

printf "%s\n $OpenPort\n\n" "=======openport=======" >> BaseLine.txt

printf "%s\n $LimitHost\n\n" "=======/etc/hosts.deny=======" >> BaseLine.txt

printf "%s\n $iptables\n\n" "=======iptables=======" >> BaseLine.txt

echo -e "\033[31m Wait, the script is being generated \033[0m\n"

i=0
str=""
arry=("\\" "|" "/" "-")
while [ $i -le 100 ]
do
    let index=i%4
    printf "[%-100s] %d %c\r" "$str" "$i" "${arry[$index]}"
    sleep 0.1
    let i=i+1
    str+="#"
done
echo ""

echo -e "\n\033[31m the script is generated done \033[0m\n"