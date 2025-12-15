import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.screen = None

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        try:
            rows = self.life.rows
            cols = self.life.cols

            for r in range(rows + 1):
                y = r * 2
                for c in range(cols):
                    x = c * 3
                    screen.addstr(y, x, "+--")
                screen.addstr(y, cols * 3, "+")

            for r in range(rows):
                y = r * 2 + 1
                for c in range(cols + 1):
                    x = c * 3
                    screen.addstr(y, x, "|")
        except curses.error:
            pass

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        try:
            for r in range(self.life.rows):
                for c in range(self.life.cols):
                    y = r * 2 + 1
                    x = c * 3 + 1

                    if self.life.curr_generation[r][c]:
                        screen.addstr(y, x, "  ", curses.A_REVERSE)
                    else:
                        screen.addstr(y, x, "  ")
        except curses.error:
            pass

    def run(self) -> None:
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        curses.curs_set(0)

        try:
            self.screen.nodelay(True)

            while True:
                self.screen.clear()

                key = self.screen.getch()
                if key in (ord("e"), ord("E")):
                    break

                self.draw_borders(self.screen)
                self.draw_grid(self.screen)

                self.screen.refresh()
                self.life.step()
                curses.napms(150)

        finally:
            self.screen.keypad(False)
            curses.nocbreak()
            curses.echo()
            curses.curs_set(1)
            curses.endwin()


if __name__ == "__main__":
    game = GameOfLife((20, 40), randomize=True)

    console = Console(game)
    console.run()
