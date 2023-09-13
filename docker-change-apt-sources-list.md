
### 方式1
```docker
RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN  apt-get clean
```


### 方式2

sources.list
```shell
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free
deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free
deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free
deb http://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free

# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb http://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
deb http://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
deb http://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
deb http://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free
# deb-src http://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free
```


```docker
COPY ./sources.list /etc/apt/sources.list

RUN cat /etc/apt/sources.list
RUN rm -Rf /var/lib/apt/lists/*
RUN apt-get update
```
