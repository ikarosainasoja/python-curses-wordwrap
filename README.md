# Custom word wrapper for Python Curses

This module employs regular expressions to segment the input string into discrete components, such as words and spaces. It attempts to insert these components individually into the container window, ensuring proper word wrapping.

## Using the word wrapper

The simplest way to utilize this module is to put the _word_wrapper.py_ file in the same directory as the file requiring word wrapping.

Import the module inside your main python file with `ìmport word_wrapper as ww`

To use the wrapper in your code, call the _wordwrap_ function and provide the required arguments:

`ww.wordwrap(window, string, attr=0)`

`window`is the name of the _Curses window_ to print in. This can be also a _subwin_ or _derwin_.
`string`is the name of the variable that is holding the string to be wrapped. Line breaks and other whitespace characters are processed normally.
`attr`is an optional Curses text attribute, e.g. curses.A_REVERSE. If left blank, it deafults as 0 (no attribute).
