# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_types.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oblood <oblood@student.21-school.ru>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/17 20:11:33 by oblood            #+#    #+#              #
#    Updated: 2022/09/18 16:27:11 by oblood           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def data_types():
    a = 7
    b = "hello"
    c = 5.2
    d = True
    e = ['1', '2', '3', '4']
    f = {}
    g = ()
    h = set()
    print('[%s, %s, %s, %s, %s, %s, %s, %s]'
          % (
              type(a).__name__, type(b).__name__ ,
              type(c).__name__, type(d).__name__,
              type(e).__name__, type(f).__name__ ,
              type(g).__name__, type(h).__name__
            )
          )

if __name__ == '__main__':
  data_types()
