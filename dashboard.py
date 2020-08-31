import colorama
from colorama import Fore, Back, Style
colorama.init()

class Dashboard:
    nameD1 = Fore.RED+"D"+Style.RESET_ALL
    nameD2 = Fore.YELLOW+"a"+Style.RESET_ALL
    nameD3 = Fore.GREEN+"r"+Style.RESET_ALL
    nameD4 = Fore.BLUE+"w"+Style.RESET_ALL
    nameD5 = Fore.MAGENTA+"i"+Style.RESET_ALL
    nameD6 = Fore.CYAN+"n"+Style.RESET_ALL
    name_DD = nameD1+nameD2+nameD3+nameD4+nameD5+nameD6
