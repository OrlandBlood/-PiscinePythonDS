# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    first_method.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oblood <oblood@student.21-school.ru>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/19 20:43:11 by oblood            #+#    #+#              #
#    Updated: 2022/09/19 20:43:54 by oblood           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Research:
    def file_reader(self):
        file = open("data.csv", "r")
        text = file.read()
        return text

if __name__ == '__main__':
    m = Research()
    print(m.file_reader())