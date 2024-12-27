# HillgateSambo 2024

from colors import *
import external_funtions as extf
import interface

def main():
  while True:
    atmObj = interface.welcome_and_login()
    if atmObj: interface.main_menu_options(atmObj)
    extf.clear_screen()
    print("\nPress '0' to exit or any other key to continue." + Colors.END)
    if extf.get_keyboard_press() == '0': exit()

extf.clear_screen()
main()
