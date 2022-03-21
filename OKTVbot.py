#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from socket import *
from time import ctime
import json
import ccxt
import configparser
import os
import logging

# 读取配置文件，优先读取json格式，如果没有就读取ini格式
config = {}
if os.path.exists('./config.json'):
    config = json.load(open('./config.json', encoding="UTF-8"))
elif os.path.exists('./config.ini'):
    conf = configparser.ConfigParser()
    conf.read("./config.ini", encoding="UTF-8")
    for i in dict(conf._sections):
        config[i] = {}
        for j in dict(conf._sections[i]):
            config[i][j] = conf.get(i, j)
else:
    logging.info("配置文件 config.json 不存在，程序即将退出")
    exit()

# 服务配置
# listenHost = config['service']['listen_host']
debugMode = config['service']['debug_mode']

# 交易所API账户配置
accountConfig = {
    'apiKey': config['account']['api_key'],
    'secret': config['account']['secret'],
    'enableRateLimit': True
}

# 格式化日志
LOG_FORMAT = "%(pastime)s - %(levelness)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d/ %H:%M:%S %p"
logging.basicConfig(filename='binance_trade.log', level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.FileHandler(filename='okex_trade.log', encoding=)

# 定义服务器名称
HOST = config['service']['listen_host']
BUFSIZE = 1024
addr = (HOST, 80)

# 定义服务器属性
tcpsersock = socket(AF_INET, SOCK_STREAM)
tcpsersock.bind(addr)
tcpsersock.listen(5)

while True:
    print('等待TradingView交易信号...，如果遇到问题，请加电报群：https://t.me/okbi_com')
    tcpcliscock, adder = tcpsersock.accept()
    print('...连接：', adder)
    while True:
        data = tcpcliscock.recv(BUFSIZE)
        if not data:
            break
        print(data)

        # 返回给请求机器的信息
        data_send = {
            "hello": "我已经收到你到信息了！"
        }
        data_s = json.dumps(data_send)
        print(data_s)
        data_s = data_s.encode()
        print(data_s)

        # 接收信息，由于接收到的信息是编码后的bytes信息，需要进行decode
        # 开始处理对接交易所的逻辑
        print(data)
        data_utf_8 = data.decode('utf-8')
        print(data_utf_8)
        data_last_line = data_utf_8.split()[-1]
        print(data_last_line)
        json_data = json.loads(data_last_line)
        print(json_data)
        ret = json_data['side']
        print(ret)
        symbol = json_data['symbol']
        amount = config['trading']['amount']
        type = json_data['type']
        side = json_data['side']


        binance = ccxt.binance(config={
            'apiKey': accountConfig['apiKey'],
            'secret': accountConfig['secret'],
            'enableRateLimit': True,
        })

        # 做的是永续合约future
        params = {
            'type': 'future'
        }

        # 观察自己合约账户的资金状况
        binance_balance_margin = binance.fetch_balance({'type': 'future'})
        print(binance_balance_margin['USDT'])  # USDT这个资产的数量

        # 根据信号做多单，还是空单
        create_order_info = binance.create_order(symbol, type, side, amount, params={'type': 'future'})
        print(create_order_info)

        # 平仓信号
        if side == 'TP':
            fetch_order_info = binance.fetch_orders(symbol, limit=1, params={'type': 'future'})
            print(fetch_order_info)
            fetch_order_side = fetch_order_info[0]['side']
            print(fetch_order_side)
            if fetch_order_side == 'BUY':
                fetch_order_side = 'sell'
                tp_order_info = binance.create_order(symbol, type, fetch_order_side, fetch_order_info['amount'],
                                                     params={'type': 'future'})
                print(tp_order_info)
                print('已经平多仓')
            elif fetch_order_side == 'SELL':
                fetch_order_side = 'buy'
                tp_order_info = binance.create_order(symbol, type, fetch_order_side, fetch_order_info['amount'],
                                                     params={'type': 'future'})
                print(tp_order_info)
                print('已经平空仓')
            else:
                print('没有执行平仓动作！')
        # 加上时间戳后的信息发送，需要通过编码，以bytes的形式发送
        tcpcliscock.send(data_s)
    tcpcliscock.close()

tcpsersock.close()
