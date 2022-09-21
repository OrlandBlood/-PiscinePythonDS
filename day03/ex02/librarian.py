# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    librarian.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oblood <oblood@student.21-school.ru>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/20 22:17:44 by oblood            #+#    #+#              #
#    Updated: 2022/09/20 22:18:26 by oblood           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

def main():

	try:
		venv = os.environ['VIRTUAL_ENV']
		user = os.environ['USER']
	except KeyError:
		venv = None
		print("wrong environment variable")
	if venv:
		if venv.endswith(f'ex02/{user}'):
			os.system("pip3 install beautifulsoup4 PyTest requests> /dev/null; pip3 freeze; pip3 freeze  > requirements.txt")
			os.system(f"rm archive.tar 2> /dev/null;tar -c -f archive.tar {user}")
		else:
			raise ValueError("wrong environment variable")


if __name__ == "__main__":
	main()
