# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to_dictionary.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oblood <oblood@student.21-school.ru>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 15:36:13 by oblood            #+#    #+#              #
#    Updated: 2022/09/18 15:36:15 by oblood           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def data():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return list_of_tuples

def to_dictionary(list_of_tuples):
    my_dict = dict(list_of_tuples)
    return my_dict

def print_dict():
    my_dict = to_dictionary(data())
    for key, value in my_dict.items():
        print("\'%s\' : \'%s\'" % (value, key))

if __name__ == '__main__':
    print_dict()