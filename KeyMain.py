#!/usr/bin/python3

# FB 2024-Mar-26 

#   from CWpi an idea of 
#   Yoshihiro Kawamata
#       (kaw@on.rim.or.jp, ex JH0NUQ)

import os.path
import InputOutputPort as port
import PaddleKeyer     as pdl
import CwUtilities     as utl
import ConsoleCommands as cmd

print("Welcome to cw_keyb_keyer.py")
print("  '?'   for the short help.")
print("  <TAB> for command completion.")

# load initial configuration file
#
initfile=os.path.expanduser('~/.picwrc')
try:
    if os.path.exists(initfile):
        print()
        cmd.load_file(initfile)
except:
    pass

# command console
#
while True:
    # read user's input
    #
    try:
        line=input("\n"+utl.speedstr()+\
                   ('/REC' if mem.recording else '')+\
                   ':')
        print()
    except KeyboardInterrupt:
        continue
    except EOFError:
        break

    if not cmd.parser(line):
        break

# termination processes
#
pdl.terminate()
port.terminate()
print()
print("Bye bye...")
