import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
from math import floor

license = """The utility was created on python 2.7.10.
The "mac/pin_wifi" utility is designed to recover
a lost pincode from YOUR router"""
dre = """
░░░░░░░░░▄▄▄▄░░░░░░░░░░░░░░▄▄▄▄░░░░░░░░░
░░░░░▄▄█████████▄░░░░░░▄██████████▄░░░░░
░░░▄██████████████▄░░▄██████████████▄░░░
░▄██████████▀█████████████████████████▄░
▄██████████▀░░███████████████▀█████████▄
██████████▀░░░█████████▀░███▀░▀█████████
██████████░░▄░░████████░░███░░░█████████
▀███████▀░░██░░███████░░░░█░░░░▀███████▀
░▄▄▄▄▄▄▄▄▄███▄░░██▀▀▀▀░░░░▀░▄█▄▄▄▄▄▄▄▄▄░
░░████████████░░█░░░▄▄▄█░░░░██████████░░
░░░███████████░░░░▄█████░░░██████████░░░
░░░░▀██████████░░░██████░░▄████████▀░░░░
░░░░░░▀████████░░████████▄███████▀░░░░░░
░░░░░░░░▀███████▄██████████████▀░░░░░░░░
░░░░░░░░░░▀██████████████████▀░░░░░░░░░░
░░░░░░░░░░░░▀██████████████▀░░░░░░░░░░░░
░░░░░░░░░░░░░░▀██████████▀░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▀██████▀░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▀██▀░░░░░░░░░░░░░░░░░░"""


NAME = """𝕃𝕠𝕤𝕥 ℙ𝕀ℕ 𝕣𝕖𝕔𝕠𝕧𝕖𝕣𝕪 - 𝕞𝕒𝕔/𝕡𝕚𝕟_𝕨𝕚𝕗𝕚"""


def main():
	print(Fore.BLUE)
	MAC_adress = input('mac adress : ')
	One = Two = (int(MAC_adress, 16) & 0xFFFFFF) % 10000000
	Var1 = 0
	while Two:
		Var1 += 3 * (Two % 10)
		Two = floor(Two / 10)
		Var1 += Two % 10
	Two = floor(Two / 10)
	Var2 = (One * 10) + ((10 - (Var1 % 10)) % 10)
	Var3 = str(int(Var2))
	result = Var3.zfill(8)
	print(Fore.YELLOW, result)



print(Fore.RED, dre)
print(NAME)
stat_lock = input('Have you read the license agreement?(y/n)')
if stat_lock == 'y':
	main()
else:
	print(Fore.RED, license)
	read_license = input('Do you agree with the license agreement policy?(y/n)')
	if read_license == 'y':
		main()
	else:
		print('The utility has completed its work!')
		input('press enter...')

