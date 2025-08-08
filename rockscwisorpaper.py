import re, random
from colorama import Fore, Style

print(f"HI I am AI rock paper scissor")
user_name = input(f"{Fore.MAGENTA}Please Enter Your Name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Guest"

rock = [
    "Rock",
    "Paper",
    "Scissor"
]

print(f"\nAI Bot: Do you Want To Play{Fore.CYAN}{Style.RESET_ALL}")
Anser = input().lower()

if Anser == "yes":
    print(f"{Fore.YELLOW}AI BOT: Ok Lets Start{Style.RESET_ALL}")

    
    print(Fore.YELLOW + f"AI BOT: Paper")

    print(f"\nNow its your turn Pick Rock Paper Or Scissor")
    turn = input().lower()

if turn == "rock":
    print(f"{Fore.RED}Paper Covered Rock, YOU LOSE!{Style.RESET_ALL}")

elif turn == "paper":
    print(Fore.YELLOW + f"Its A Draw{Style.RESET_ALL}")

elif turn == "scissor":
    print(f"{Fore.GREEN}Scissor Cut Through Paper, You WIN{Style.RESET_ALL}")



elif Anser == "no":
    print(f"{Fore.RED}AI BOT: Ok! Goodbye👋{Style.RESET_ALL}")
