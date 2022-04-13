# /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request
import ccxt
import time
import json
import logging
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/trader', methods=['POST'])
def trader():
    global ex
    data = request.get_data()
    print(data)
    data_utf_8 = data.decode('utf-8')
    print(data_utf_8)
    data_last_line = data_utf_8.split()[-1]
    print(data_last_line)
    json_data = json.loads(data_last_line)
    print(json_data)

    simple_config = {}
    if os.path.exists('./simple_config.json'):
        simple_config = json.load(open('./simple_config.json', encoding="UTF-8"))
    else:
        logging.info("配置文件 config.json 不存在，程序即将退出")
        exit()

    exchange = json_data['exchange']
    exchange_type = json_data['exchange_type']
    symbol = json_data['symbol']
    side = json_data['side']
    position_amount = ''
    author = 'https://t.me/okbi_com'
    amount = json_data['amount']

    if simple_config['service']['password'] != json_data['password']:
        print(str('您的安全码不对，无法为您执行'))
        exit()

    if author != json_data['author']:
        print(str('您在TradingView发送的数据，为了尊重作者，请加上 https://t.me/okbi_com, 重起软件'))
        exit()

    try:
        # 交易所API账户配置
        # 暂时只支持binance交易所，等待更新升级
        if exchange == 'binance':
            ex = ccxt.binance(config={
                'apiKey': simple_config['exchanges']['binance']['api_key'],
                'secret': simple_config['exchanges']['binance']['api_secret'],
                'enableRateLimit': True,
            })
        elif exchange == 'okx':
            ex = ccxt.okex5(config={
                'apiKey': simple_config['exchanges']['okx']['api_key'],
                'secret': simple_config['exchanges']['okx']['api_secret'],
                'enableRateLimit': True,
                'password': simple_config['exchanges']['okx']['password']
            })
        elif exchange == 'ftx':
            ex = ccxt.ftx(config={
                'apiKey': simple_config['exchanges']['ftx']['api_key'],
                'secret': simple_config['exchanges']['ftx']['api_secret'],
                'enableRateLimit': True
            })
        else:
            print('交易所有错，没有这个交易所')

        if (side == 'buy') or (side == 'sell'):
            #  根据信号做多单，还是空单
            print('准备在：', exchange, '交易所，执行买入多单或者空单操作！')
            k = 0
            while k < 10:
                create_order_info = {}
                print('第 ', k, ' 次尝试买入交易！')
                try:
                    create_order_info = ex.create_order(symbol, 'MARKET', side, amount,
                                                        params={'type': exchange_type})
                    print(create_order_info)
                    if create_order_info:
                        print('已经成功下单，退出循环')
                        break
                    time.sleep(3)
                except Exception as e:
                    print(str(e))
                k = k + 1
                time.sleep(3)

        #  平仓信号
        if side == 'TP':
            print('准备在：', exchange, '交易所，执行市价全平操作！')
            j = 0
            while j < 10:
                print('第 ', j, ' 次尝试平仓！')
                create_take_profit_order_info = {}
                positionRisk = binance.fapiPrivateV2GetPositionRisk()
                for i in positionRisk:
                    if i['symbol'] == 'BTCUSDT':
                        print(i['positionAmt'])
                        position_amount = i['positionAmt']
                        break
                print(position_amount)
                # position_amount = float(position_amount)
                # print(position_amount)
                if position_amount > float(0):
                    position_side = 'sell'
                elif position_amount < float(0):
                    position_side = 'buy'
                    position_amount = abs(position_amount)
                else:
                    print('空仓，没有平仓交易发生！')
                    break
                try:
                    create_take_profit_order_info = binance.create_order(symbol, 'MARKET', position_side,
                                                                         position_amount,
                                                                         params={'type': exchange_type})
                    print(create_take_profit_order_info)
                    if create_take_profit_order_info:
                        break
                except Exception as e:
                    print(str(e))
                j = j + 1
    except Exception as e:
        print(str(e))

    return 'ok'


if __name__ == '__main__':
    app.run(host='10.1.60.3', port=80, debug=True)
