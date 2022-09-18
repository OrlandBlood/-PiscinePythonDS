# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    names_extractor.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oblood <oblood@student.21-school.ru>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 17:47:28 by oblood            #+#    #+#              #
#    Updated: 2022/09/18 17:48:32 by oblood           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def names_extractor():
    if len(sys.argv) != 2:
        return
    with open(sys.argv[1]) as f1:
        emails = f1.readlines()
    f2 = open("employees.tsv", "a")
    f2.write("Name\tSurname\tE-mail\n")
    for email in emails:
        tmp = email.replace('@', '.')
        name = tmp.split('.')[0].capitalize()
        surname = tmp.split('.')[1].capitalize()
        line = name + "\t" + surname + "\t" + email
        f2.write(line)
    f1.close()
    f2.close()

if __name__ == '__main__':
    names_extractor()