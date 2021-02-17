#!/usr/bin/env python
# coding: utf-8

from requests import get
import json
import time as t
from datetime import date, datetime

def getValue():

    prices = get('https://api.nomics.com/v1/currencies/ticker?key=ea386addbac03f4bb67ceb1f333a8d0a&ids=BTC,ETH&interval=1d&convert=USD&per-page=100&page=1')

    data = prices.json()

    bit_price = float(data[0]['price'])
    eth_price = float(data[1]['price'])

    e = get('https://api.ethplorer.io/getAddressInfo/0xed8b4b3ba4fd5a175613859cab6ab8f010276a3a?apiKey=freekey')
    data = e.json()

    eth_holdings = float(data['ETH']['balance'])

    b = get('https://blockchain.info/balance?active=16MuqwYTRT1qTFmwF5WsgfsrA9rE3UmPQN')
    data = b.json()

    bit_holdings1 = data['16MuqwYTRT1qTFmwF5WsgfsrA9rE3UmPQN']['final_balance']
    bit_holdings = 0.98

    eth_value = eth_holdings*eth_price
    bit_value = bit_holdings*bit_price

    return [bit_price,bit_value,bit_holdings,eth_price,eth_value,eth_holdings]

def main():
    file = open('README.md', 'w')
    today = date.today().strftime("%m/%d/%y")
    time = datetime.now().strftime("%H:%M:%S")

    coin_list = getValue()

    vals = coin_list[1]+coin_list[4]

    file.write('Welcome to the Meyers Crypto Portfolio Value tool. \n')
    file.write(f'As of {today} at {time} our valuation is ${vals} \n\n')
    file.write(f'BTC Price = ${coin_list[0]}\n ETH Price = ${coin_list[3]}\n')
    file.write(f'BTC Holdings = {coin_list[2]}BTC\n ETH holdings = {coin_list[5]}ETH \n')

    t.sleep(1)
main()






