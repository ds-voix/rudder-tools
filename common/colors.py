# yum install python3-colorama
import os
import colorama
from colorama import Fore, Back, Style

if ("NOCOLOR" in os.environ) and (os.environ["NOCOLOR"] == "1"):
  cc=''
  cm=''
  cb=''
  cg=''
  cr=''
  c_=''
  sb=''
  sd=''
  s_=''
else:
  os.system("")  # enables ansi escape characters in terminal
  cc=Fore.CYAN
  cm=Fore.MAGENTA
  cb=Fore.BLUE
  cg=Fore.GREEN
  cr=Fore.RED
  c_=Fore.RESET
  sb=Style.BRIGHT
  sd=Style.DIM
  s_=Style.RESET_ALL
