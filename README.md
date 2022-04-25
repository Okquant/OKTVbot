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

wegt https://github.com/OkbiQuant/OKTVbot/releases/download/v1.0.3/oktvbot_v1
## 四 运行 
### nohup ./oktvbot_v1 &
# 即可

## 使用方法

## 专注于tradingview信号对接交易


### TV参数说明：
### 一，exchange 目前只可以binance
### 二，symbol,可以现有的永续合约交易对，比如说 BTCUSDT,ETCUSDT等
### 三，side三个选项 sell做空，buy做多，TP市价全平
### 四，amount，就是您要做空做多的数量，以币作为标价，单向持仓。
### 五，author,这个是固定字段，不可删除更改，目的是为了尊重作者
### 六，password,安全码，要和simple_config.json里的password一致，可自己写一个其他人不知道的值。


# 有问题，可以加入我们的电报群询问： https://t.me/okbi_com

