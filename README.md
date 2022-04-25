# 好币量化托管者使用方法：

## linux系统的使用
## 一 关闭防火墙

（1）systemctl  status firewalld.service查看防火墙的状态；

（3）systemctl  stop firewalld.service关闭防火墙；

（6）systemctl  disable firewalld.service开机禁用防火墙；

（7）systemctl  is-enabled firewalld.service查看防火墙是否开机启动；

## 二 打开3621端口

各个服务器提供商打开的端口不进相同，默认全开的，个人使用多的服务商 www.henghost.com , www.jingdouyun.cn

## 三 下载托管者

wget https://github.com/OkbiQuant/OKTVbot/releases/download/v1.0.3/oktvbot_v1
打开托管者权限
chmod 777 oktvbot_v1
## 四 运行 
### nohup ./oktvbot_v1 &
# 即可

## 使用方法

## 专注于tradingview信号对接交易
用tradingview发送的消息体格式：
一 用 alert()函数消息格式：
{exchange":"binance","symbol":"BTCUSDT","side":"sell","amount":"0.01","robot_number":"100340","user_security_code": "xxxxxx"}
二 用函数的参数做警报的commet参数：（反斜杆是转义字符）
{\"exchange\":\"binance\",\"symbol\":\"BTCUSDT\",\"side\":\"buy\",\"amount\":\"0.15\",\"robot_number\":\"100000\",\"user_security_code\": \"official_robot\"}

如果是用

### TV参数说明：
### 一，exchange 目前只可以binance,支持更多的交易所，后续的版本继续跟新中
### 二，symbol,可以现有的永续合约交易对，比如说 BTCUSDT,ETCUSDT等
### 三，side三个选项 sell做空，buy做多，TP市价全平
### 四，amount，就是您要做空做多的数量，以币作为标价，也可以用USDT标价，看你在交易所的偏好设置，目前只支持单向持仓，双向持仓后续版本推出。
### 五，robot_number,目前一台机器人只可以运行一个托管者，服务器会给每个托管者分配一个robot_number,不要填错了，V1版本的请我们群里的客服或者是老大。
### 六，user_security_code,安全码，自己确定安全码，可以任意。V1版本的托管者，请联系群里的客服或者是UP主，把您的安全码发过去设置。


# 有问题，可以加入我们的电报群询问： https://t.me/okbi_com

