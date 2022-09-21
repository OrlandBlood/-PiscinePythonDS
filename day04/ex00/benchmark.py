# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    benchmark.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oblood <oblood@student.21-school.ru>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/20 23:48:02 by oblood            #+#    #+#              #
#    Updated: 2022/09/21 21:38:19 by oblood           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!python3
import timeit

def get_mail_list():
    return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

def loop_list(mail_list: list = get_mail_list()):
    result = []
    for i in mail_list:
        if i.find('@gmail.com') >= 0:
            result.append(i)
    return result
    
def compr_list(mail_list: list = get_mail_list()):
    return [i for i in mail_list if i.find('@gmail.com') >= 0]


def main():
    n = 1000000
    loop_time = timeit.timeit('loop_list()', 'from __main__ import loop_list', number=n)
    compr_time = timeit.timeit('compr_list()', 'from __main__ import compr_list', number=n)

    if loop_time > compr_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    print(loop_time, 'vs', compr_time)


if __name__ == "__main__":
    main()