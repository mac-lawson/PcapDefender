from colorama import Fore, Back

def error(error):
	print(Back.WHITE + Fore.RED + "[ERR] " + error + Back.RESET + Fore.RESET)

def usage():
    print(Fore.BLUE + "Usage\n\t[-s] <query keyword> [-f] <.pcap file path>" + Fore.RESET)