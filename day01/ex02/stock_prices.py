# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stock_prices.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oblood <oblood@student.21-school.ru>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/17 21:55:58 by oblood            #+#    #+#              #
#    Updated: 2022/09/18 14:31:38 by oblood           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def data():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    return COMPANIES, STOCKS

def stock_prices():
    if len(sys.argv) != 2:
        return
    
    s = sys.argv[1].capitalize()
    COMPANIES, STOCKS = data()
    if s in COMPANIES:
        print(STOCKS[COMPANIES[s]])
    else:
        print("Unknown company")

if __name__ == '__main__':
    stock_prices()