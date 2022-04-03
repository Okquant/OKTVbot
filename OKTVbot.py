# /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request
import ccxt
import time
import json
import logging
import os

app = Flask(__name__)


# order_side = ''


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

    config = {}
    if os.path.exists('./config.json'):
        config = json.load(open('./config.json', encoding="UTF-8"))
    else:
        logging.info("配置文件 config.json 不存在，程序即将退出")
        exit()

    config_users = config['users']

    symbol = json_data['symbol']
    side = json_data['side']
    position_amount = ''

    try:
        type = json_data['type']
    except Exception as e:
        print(str(e))

    for key in config_users:
        try:
            api_key = config_users[key]['api_key']
            api_secret = config_users[key]['api_secret']
            exchange = config_users[key]['exchange']
            password = config_users[key]['password']
            bot_tv_safe_connect_key = config_users[key]['bot_tv_safe_connect_key']

            if bot_tv_safe_connect_key != json_data['bot_tv_safe_connect_key']:
                break
            if json_data['author'] != 'https://t.me/okbi_com':
                break
            contract_type = {
                'type': config_users[key]['contract_type']
            }
            # 交易所API账户配置
            try:
                if exchange == 'binance':
                    ex = ccxt.binance({
                        'apiKey': api_key,
                        'secret': api_secret,
                        'enableRateLimit': True
                    })
                elif exchange == 'okex':
                    ex = ccxt.okex5(config={
                        'enableRateLimit': True,
                        'apiKey': api_key,
                        'secret': api_secret,
                        # okex requires this: https://github.com/ccxt/ccxt/wiki/Manual#authentication
                        'password': password,
                        'verbose': False,  # for debug output
                    })
                elif exchange == 'ftx':
                    ex = ccxt.binance({
                        'apiKey': api_key,
                        'secret': api_secret,
                        'enableRateLimit': True
                    })
                elif exchange == 'ftx':
                    ex = ccxt.bitmex({
                        'apiKey': api_key,
                        'secret': api_secret,
                        'enableRateLimit': True
                    })
            except Exception as e:
                print(str(e))

            # 观察自己合约账户的资金状况

            ex_balance_margin = ex.fetch_balance(contract_type)
            print(ex_balance_margin['USDT'])  # USDT这个资产的数量

            if (side == 'buy') or (side == 'sell'):
                #  根据信号做多单，还是空单
                amount = config_users[key]['amount']
                try:
                    create_order_info = ex.create_order(symbol, type, side, amount, params=contract_type)
                    print(create_order_info)
                except Exception as e:
                    time.sleep(1)
                    print(str(e))
                    try:
                        create_order_info = ex.create_order(symbol, type, side, amount, params=contract_type)
                        print(create_order_info)
                    except Exception as e:
                        print(str(e))
                        try:
                            create_order_info = ex.create_order(symbol, type, side, amount, params=contract_type)
                            print(create_order_info)
                        except Exception as e:
                            print(str(e))

            #  平仓信号
            if side == 'TP':
                j = 0
                while j < 3:
                    print('平仓 ', j)
                    positionRisk = ex.fapiPrivateV2GetPositionRisk()
                    for i in positionRisk:
                        if i['symbol'] == 'BTCUSDT':
                            print(i['positionAmt'])
                            position_amount = i['positionAmt']
                            continue
                    print(position_amount)
                    position_amount = float(position_amount)
                    print(position_amount)
                    if position_amount > float(0):
                        side = 'sell'
                    elif position_amount < float(0):
                        side = 'buy'
                        position_amount = abs(position_amount)
                    else:
                        print('空仓，没有平仓交易发生！')
                    try:
                        create_take_profit_order_info = ex.create_order(symbol, 'MARKET', side, position_amount,
                                                                        params=contract_type)
                        print(create_take_profit_order_info)
                    except Exception as e:
                        print(str(e))
                    j = j + 1
                    time.sleep(2)

        except Exception as e:
            print(str(e))

    return 'cookout'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
