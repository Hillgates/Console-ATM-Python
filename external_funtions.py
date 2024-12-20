# HillgateSambo 2024


# These functions are intended to be used in some of my python projects
import os
import msvcrt
import random
import time

def special_enumerate(iterable: list, indeces: list):
  """
  Returns an enumerate, but using indeces for indexing instead of numbers.

  iterable
    an object supporting iteration

  The special_enumerate object yields pairs containing a count (from start, which
  defaults to zero) and a value yielded by the iterable argument.

  special_enumerate is useful for obtaining an indexed list:
    (indeces[0], seq[0]), (indeces[1], seq[1]), (indeces[2], seq[2]), ..."""
  
  if len(iterable) != len(indeces): return
  final_enumerate = []
  for i in range(len(iterable)):
    final_enumerate.append((indeces[i], iterable[i]))
  
  return tuple(final_enumerate)

# Generate n random numbers
def generate_ndigits(ndigits:int = 0):
    
    numbers = ""
    for _ in range(ndigits):
        numbers += str(random.randint(0, 9))
    return int(numbers)

def get_keyboard_press():
  try:
    key =  msvcrt.getch().decode()
    return key
  except UnicodeDecodeError:
    return ''


def clear_screen():
  os.system("cls")

# Function to wait for some amount of time in seconds
def delay(period: float) -> None:
  start_time = float(time.time())
  while ( start_time + period >= float(time.time())):
    pass # Do nothing until time delay elapses

def print_any_dict(obj: dict, tabsize = 0):
  """Prints a dict, even if nested, will un-nest it (dict only)."""
  for key, value in obj.items():
    if type(value) == type({}):
      print(tabsize * " " + key)
      print_any_dict(value, tabsize+2)
      continue
    print(tabsize * " " + key, ':', value)

def password_input(chars = 'a1_', length = 8) -> str:
  """
  Arguments:
    chars: Allowed characters (where: a is for all alphabets, 1 for all numerical digits, _ for basic keyboard symbols... perhaps excluding '\\\\' ?), default is every char ('a1_').
    length: Length of input, default = 8.
  """
  pos = 0
  result = ''
  while (pos < length and pos >= 0):
    ch = get_keyboard_press()
    if ch == '\x08': # Backspace
      result = result[:-1]
      print('\b', end='')
      pos -= 1
    elif ch == '\x1b': # Escape
      return ''
    elif ch == '5':
      print('\x02', end='')
    else: # I need to check other keys, ahhhhhhh
      result += ch
      print('*', end='')
      pos += 1
  print()
  return result

if __name__ == "__main__":
  print("Enter 4 digits: ", end='')
  fourdigits = password_input(length=4)
  print("You entered:", fourdigits)

  print("Press any key to exit.")
  get_keyboard_press()
  clear_screen()