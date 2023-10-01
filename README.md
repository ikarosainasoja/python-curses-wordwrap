# Custom word wrapper for Python Curses

![Python Curses word wrapper image](https://github.com/ikarosainasoja/misc-files/blob/main/img/python-curses-wordwrap.png)

This module employs regular expressions to segment the input string into discrete components, such as words and spaces. It attempts to insert these components individually into the container window, ensuring proper word wrapping.

## Using the word wrapper

The simplest way to utilize this module is to put the _word_wrapper.py_ file in the same directory as the file requiring word wrapping.

Import the module inside your main python file with `ìmport word_wrapper`

To use the wrapper in your code, call the _wordwrap_ function and provide the required arguments: 

`word_wrapper.wordwrap(window, string, attr=0)`

### The arguments

| Argument | Description |
| --- | --- |
| _window_ | is the name of the Curses window to print in. This can also be a name of a subwin or derwin. |
| _string_ | is the name of the variable that is holding the string to be wrapped. Line breaks and other whitespace characters are processed normally. |
| _attr_ | is an optional Curses text attribute, e.g. curses.A_REVERSE. If left blank, it deafults as 0 (no attribute). |

Example:
```python
# import curses mobule
import curses
from curses import wrapper

# import the word wrapper
import word_wrapper as ww


def main(stdscr):
    # string to wrap
    message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nNam tincidunt dui quis vestibulum feugiat."

    # clear and refresh the terminal
    stdscr.clear()
    stdscr.refresh()

    # let's create a new window, clear it and draw a border
    my_window = curses.newwin(10, 20, 7, 30)
    my_window.clear()
    my_window.box()

    # maybe we want another window inside the first one
    inner_window = my_window.derwin(8, 18, 1, 1)
    inner_window.clear()

    # use the word wrapper
    ww.wordwrap(inner_window, message)

    # refresh the windows
    inner_window.refresh()
    my_window.refresh()

    # wait for user input
    stdscr.getch()

# end curses application
wrapper(main)
```
Note: Please don't be misled by the 'wrapper' imported from the Curses library; it is unrelated to the Word wrapper. It simply serves as a function to automatically handle the initialization and exit processes of a Curses application.

Any comments and critique are welcome!
