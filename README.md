# Custom word wrapper for Python Curses

This module employs regular expressions to segment the input string into discrete components, such as words and spaces. It attempts to insert these components individually into the container window, ensuring proper word wrapping.

## Using the word wrapper

The simplest way to utilize this module is to put the _word_wrapper.py_ file in the same directory as the file requiring word wrapping.

Import the module inside your main python file with `ìmport word_wrapper`

To use the wrapper in your code, call the _wordwrap_ function and provide the required arguments: 

`word_wrapper.wordwrap(window, string, attr=0)`

### The arguments

`window` is the name of the _Curses window_ to print in. This can also be a name of a _subwin_ or _derwin_.

`string` is the name of the variable that is holding the string to be wrapped. Line breaks and other whitespace characters are processed normally.

`attr` is an optional Curses text attribute, e.g. curses.A_REVERSE. If left blank, it deafults as 0 (no attribute).

Example:
```
import curses
from curses import wrapper

# import the word wrapper
import word_wrapper as ww

def main(stdscr):

    message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nNam tincidunt dui quis vestibulum feugiat."

    stdscr.clear()
    stdscr.refresh()

    my_window = curses.newwin(5, 20, 1, 2)
    my_window.clear()

    # use the word wrapper
    ww.wordwrap(my_window, message)

    my_window.refresh()
    stdscr.getch()

wrapper(main)
```
Note: Please don't be misled by the 'wrapper' imported from the Curses library; it is unrelated to the Word wrapper. It simply serves as a function to automatically handle the initialization and exit processes of a Curses application.

Any comments and critique are welcome!
