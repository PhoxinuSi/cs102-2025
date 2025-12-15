import sys

try:
    import curses
    test_screen = curses.initscr()
    curses.endwin()
    print("Curses поддерживается!")
except Exception as e:
    print(f"Curses НЕ поддерживается: {e}")
    print("Используйте альтернативный вариант")