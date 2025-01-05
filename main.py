# HillgateSambo 2025

from colors import *
from external_funtions import clear_screen, get_keyboard_press
import interface

def main():
  while True:
    atmObj = interface.start_menu()
    if atmObj: 
      if interface.atm_menu(atmObj):
        continue
    clear_screen()
    print("\nPress any key to exit." + Colors.END)
    get_keyboard_press()
    exit(0)

clear_screen()
main()
