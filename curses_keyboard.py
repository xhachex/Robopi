import curses

#Curses init
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
  while True:
    char = screen.getch()
    if char == ord('q'):
      break
    elif == curses.KEY_UP:
      print ("up")
    elif == curses.KEY_DOWN:
      print ("down")

finally:
  #Cleanup
  curses.nocbreak()
  screen.keypad(0)
  curses.echo()
  curses.endwin()
