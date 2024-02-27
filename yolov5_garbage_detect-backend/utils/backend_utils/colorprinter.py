from colorama import Fore, Back, Style


def print_red(text):
    color_text = Fore.RED + str(text) + Style.RESET_ALL
    print(color_text)


def print_green(text):
    color_text = Fore.GREEN + str(text) + Style.RESET_ALL
    print(color_text)


def print_yellow(text):
    color_text = Fore.YELLOW + str(text) + Style.RESET_ALL
    print(color_text)


def print_blue(text):
    color_text = Fore.BLUE + str(text) + Style.RESET_ALL
    print(color_text)


def print_magenta(text):
    color_text = Fore.MAGENTA + str(text) + Style.RESET_ALL
    print(color_text)


def print_cyan(text):
    color_text = Fore.CYAN + str(text) + Style.RESET_ALL
    print(color_text)


def print_white(text):
    color_text = Fore.WHITE + str(text) + Style.RESET_ALL
    print(color_text)


def print_black_bg(text):
    color_text = Back.BLACK + str(text) + Style.RESET_ALL
    print(color_text)


def print_white_bg(text):
    color_text = Back.WHITE + str(text) + Style.RESET_ALL
    print(color_text)
