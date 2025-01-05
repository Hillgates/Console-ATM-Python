# HillgateSambo 2025


# These functions are intended to be used in some of my python projects
import os
import msvcrt
import random
import time

# Printing or outputs
def fprint(obj: object):
  print(obj, end='', flush=True)

def fprintln(obj: object):
  print(obj, flush=True)

def flush_input():
  while msvcrt.kbhit():
    msvcrt.getch()

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
def delay(x: float):
  time.sleep(x)

def print_any_dict(obj: dict, tabsize = 0):
  """Prints a dict, even if nested, will un-nest it (dict only)."""
  for key, value in obj.items():
    if type(value) == type({}):
      print(tabsize * " " + key)
      print_any_dict(value, tabsize+2)
      continue
    print(tabsize * " " + key, ':', value)

def IsCharAllowed(thechar: str, rule: str):
  """ rule can be ('a', '1', 'a1', 'a1_') """
  ch = ''
  if (thechar.lower() >= 'a' and thechar.lower() <= 'z'):
    ch = 'a'
  elif (thechar >= '0' and thechar <= '9'):
    ch = '1'
  elif ((thechar >= ' ' and thechar <= '/') or (thechar >= ':' and thechar <= '@') or (thechar >= '[' and thechar <= '`') or (thechar >= '{' and thechar <= '~')):
    ch = '_'
  
  if ch in rule: return True
  else: return False


def password_input(passwordChar = '*', charsRule = 'a1_', length = 8, showChars=False, submitOnEnter=False) -> str:
  """
  Arguments:
    passwordChar: The character to show instead of text type, default is '*'
    charsRule: Allowed characters (where: a is for all alphabets, 1 for all numerical digits, _ for standard keyboard symbols), default is every char ('a1_'). Possible chars are ('a', '1', 'a1', 'a1_'), any rule besides this... default will be used.
    length: Length of input, default = 8.
    showChars: If set to True, passwordChard will be ignored, and text typed will be displayed.
    submitOnEnter: Submits input when Enter is pressed... empty input (including trailing or leading spaces) is ignored.
  """
  if charsRule not in ('a', '1', 'a1', 'a1_'):
    charsRule = 'a1_'

  pos = 0
  result = ''
  while (pos < length and pos >= 0):
    ch = get_keyboard_press()
    if ch == '\x08': # Backspace
      if pos != 0:
        result = result[:-1]
        fprint('\x08 \x08') # Yerrrr!! That didnt come easily!
        pos -= 1
    elif ch == '\x1b': # Escape
      break
    elif ch == '' or ch == '\x00': # Some other buttons on my keyboard e.g F1-F12, Insert, etc.
      continue
    elif ch == '\r': # Enter
      if len(result.strip()) > 0 and submitOnEnter == True:
        break
    elif IsCharAllowed(ch, charsRule):
      result += ch
      if showChars:
        fprint(ch)
      else:
        fprint(passwordChar)
      pos += 1
    else:
      continue
  print()
  return result

if __name__ == "__main__":
  print("Press four characters: ", end='')
  four = password_input(length=4)
  print("You entered: " + four)
  print("Press any key to exit.")
  get_keyboard_press()
  clear_screen()