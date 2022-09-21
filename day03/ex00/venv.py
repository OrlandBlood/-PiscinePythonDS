# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    venv.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oblood <oblood@student.21-school.ru>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/20 21:56:19 by oblood            #+#    #+#              #
#    Updated: 2022/09/20 21:57:55 by oblood           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!python3
import os


def main():
    print('Your current virtual env is ',os.environ['VIRTUAL_ENV'])


if __name__ == '__main__':
    main()