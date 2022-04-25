# 好币量化托管者使用方法：

# 第一步、部署托管者

## 购买服务器

自己选择一个linux服务器，对服务器的配置要求不高，1G内存、1核心、2M带宽配置即可，但是要稳定，安装centOS7以上，推荐centOS7.6 64位

服务商 www.henghost.com , www.jingdouyun.cn ,阿里云、百度智能云、腾讯云、华为云等等都可以。

## linux系统的使用

使用服务商自带的VNC连接服务器即可，操作简单。

## 一、关闭防火墙

（1）systemctl  status firewalld.service查看防火墙的状态；

（3）systemctl  stop firewalld.service关闭防火墙；

（6）systemctl  disable firewalld.service开机禁用防火墙；

（7）systemctl  is-enabled firewalld.service查看防火墙是否开机启动；

## 二、打开3621端口

各个服务器提供商安全组，默认打开的端口不尽相同。
默认端口全开服务商 www.henghost.com , www.jingdouyun.cn ，可以参考使用

## 三、下载托管者

安装 wget

yum -y install wget

wget https://github.com/OkbiQuant/OKTVbot/releases/download/v1.0.3/oktvbot_v1


打开托管者权限

chmod 777 oktvbot_v1

## 四、挂起运行 
### nohup ./oktvbot_v1 &

有提示，回车就可以

查看进程是不是启动了用下面的命令

netstat -ntlp | grep 3621

此命令会让托管者一直在线，无论有没有关终端。

# 即可

检测托管者是否在线的方法
浏览器输入 x.x.x.x:3621   (您的IP+端口)
提示 ：I am online
说明托管者已经在线了。

联系UP主，把托管者的IP发给UP主，第一版本麻烦点，下个版本，就可以自己提交到网站了

# 第二步、TV信号格式设置

## 使用方法

## 专注于tradingview信号对接交易
用tradingview发送的消息体格式：

一 用 alert()函数消息格式：

{exchange":"binance","symbol":"BTCUSDT","side":"sell","amount":"0.01","robot_number":"100340","user_security_code": "xxxxxx"}

二 用函数的参数做警报的commet参数：（反斜杆是转义字符）

{\\"exchange\\":\\"binance\\",\\"symbol\\":\\"BTCUSDT\\",\\"side\\":\\"buy\\",\\"amount\\":\\"0.15\\",\\"robot_number\\":\\"544578\\",\\"user_security_code\\": \\"edrdgfdgfdfg\\"}

三、添加报警信号

tradingView的webhook URL格式，统一 http://www.okbi.com/signalman

### TV参数说明：
### 一，exchange 目前只可以binance,支持更多的交易所，后续的版本继续跟新中
### 二，symbol,可以现有的永续合约交易对，比如说 BTCUSDT,ETCUSDT等
### 三，side三个选项 sell做空，buy做多，TP市价全平
### 四，amount，就是您要做空做多的数量，以币作为标价，也可以用USDT标价，和你在交易所的偏好设置要一致，目前只支持单向持仓，双向持仓后续版本推出。
### 五，robot_number,目前一台服务器只可以运行一个托管者，服务器会给每个托管者分配一个robot_number,不要填错了，V1版本的请我们群里的客服或者是老大。
### 六，user_security_code,安全码，自己确定安全码，可以任意。V1版本的托管者，请联系群里的客服或者是UP主，把您的安全码发过去设置。

# 联系UP主或者进入我们的群，把您的币安 API_KEY,API_SECRET发给UP主或者是客服，即可，后续版本，自己提交到网站设置。


# 有问题，可以加入我们的电报群询问： https://t.me/okbi_com

