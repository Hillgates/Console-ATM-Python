# HillgateSambo 2024

from colors import *
import external_funtions as extf
import interface

def main():
  atmObj = interface.welcome_and_login()
  if atmObj: interface.main_menu_options(atmObj)


if __name__ == '__main__':
  extf.clear_screen()
  main()
  print("\nPress any key to exit." + Colors.END)
  extf.get_keyboard_press()