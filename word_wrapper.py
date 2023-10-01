# Word wrapper for Python Curses module by Ikaros Ainasoja

import re


def wordwrap(window, string, attr=0):
    # 'window', name of the window to print
    # 'string', variable containing the string to print
    # 'attr', optional curses attribute (e.g. curses.A_BOLD)

    # Get cursor position
    cursor_y, cursor_x = window.getyx()

    # Get window dimensions
    win_height, win_width = window.getmaxyx()

    # If string length <= window width: print the string.
    if len(string) + cursor_x <= win_width:
        window.addstr(string, attr)

    # Otherwise, split it into individual words and whitespaces,
    # put them in a list and try to print them one at a time.
    else:
        for item in wordlist(string):
            # Skip spaces in the beginning of a new line.
            if cursor_x == 0 and item == " ":
                continue

            # If list item lenght <= distance to window edge: print it.
            if len(item) + cursor_x <= win_width:
                window.addstr(item, attr)

            # Otherwise, move to the next line and try to fit it there.
            else:
                # If this would move the cursor out of bounds: error.
                if cursor_y == win_height - 1:
                    raise Exception("String too long for the window!")

                # Otherwise, print it.
                window.addstr(cursor_y + 1, 0, item, attr)

            # Get cursor position before the next list item.
            cursor_y, cursor_x = window.getyx()


# The function to split the string into individual elements
# and returning them as a list.
def wordlist(string):
    return re.split(r"(\s+|\n+)", string)
