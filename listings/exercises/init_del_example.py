from colorama import init, Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
print(Style.BRIGHT + Fore.YELLOW + 'plum color')
print(Style.RESET_ALL)
print('back to normal now\n')


# pure ANSI way
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKRED = '\033[31m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET_DEFAULT = '\033[39m'


print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue? {bcolors.ENDC}")
print(f"{bcolors.OKRED}Warning: No active frommets remain. Continue? {bcolors.ENDC}")


class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print(f'\n{bcolors.OKRED}I am destructed{bcolors.ENDC}', self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)
