import time
import os

from colorama import init
from colorama import Fore

from art import tprint
from scripts.osinter import search_username

from scripts.getinfo import info_tg_account, instagram_account_info, github_info_account

init()

def osint():
    username = input('* Enter the user of the person you want to scan: ')
    search_username(username)

    return username


def main_menu():
    while True:
        choice = input("\nEnter 'e/E' to exit the program, 'i/I' for more info, or 'a/A' to try again: ").lower()
        if choice == 'a':
            return 'again'
        elif choice == 'i':
            return 'info'
        elif choice == 'e':
            return 'exit'
        else:
            print("Invalid input. Please try again.")


def main():
    os.system('cls')
    time.sleep(1)
    tprint('os1nt anqe1', font='small')
    print('\t\t\t', ' powered by ange1')
    print('__________________________________________________\n')

    while True:
        username = osint()

        while True:
            action = main_menu()

            if action == 'again':
                break  # Exit to outer loop to re-enter username
            elif action == 'info':
                github_info_account(username)
                instagram_account_info(username)
                info_tg_account(username)
            elif action == 'exit':
                print("Exiting...")
                return


if __name__ == '__main__':
    main()
