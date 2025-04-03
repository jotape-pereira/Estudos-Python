# Como adicionar cores no terminal?

# txt = str(input())
# print(f'\033[0;30;41m{txt}\033[m')

# Definindo cores
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Usando
print(f"{BOLD}{GREEN}Nome{RESET}\t{BOLD}{BLUE}Idade{RESET}")
print(f"João\t{BLUE}25{RESET}")
print(f"Maria\t{RED}30{RESET}")