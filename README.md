# OKTVbot
## 使用方法

## 专注于tradingview信号对接交易

## TradingView发送post请求的,请求体格式：
### {"exchange":"binance","symbol":"BTCUSDT","side":"sell","amount":"0.015","author":"https://t.me/okbi_com","password": "qerewetr"}
TV参数说明：
一，exchange 目前只可以binance
二，symbol,可以现有的永续合约交易对，比如说 BTCUSDT,ETCUSDT等
三，side三个选项 sell做空，buy做多，TP市价全平
四，amount，就是您要做空做多的数量，以币作为标价，单向持仓。
五，author,这个是固定字段，不可删除更改，目的是为了尊重作者
六，password,安全码，要和simple_config.json里的password一致，可自己写一个其他人不知道的值。


### 请求路径格式 http://127.0.0.1:80/trader

### 已经更新安全机制

### 建议用进程守护程序：
### supervisor 守护， 

# 有问题，可以加入我们的电报群询问： https://t.me/okbi_com

## https://www.yuque.com/okbiquant/oktvbot
