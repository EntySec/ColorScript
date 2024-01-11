"""
MIT License

Copyright (c) 2020-2024 EntySec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys


class Colors(object):
    """ Subclass of colorscript module.

    This subclass of colorscript module is intended for
    providing different color bindings for interface.
    """

    def __init__(self) -> None:
        super().__init__()

        self.BLACK = '\033[30m' if sys.platform == 'darwin' else '\001\033[30m\002'
        self.RED = '\033[31m' if sys.platform == 'darwin' else '\001\033[31m\002'
        self.GREEN = '\033[32m' if sys.platform == 'darwin' else '\001\033[32m\002'
        self.YELLOW = '\033[33m' if sys.platform == 'darwin' else '\001\033[33m\002'
        self.BLUE = '\033[34m' if sys.platform == 'darwin' else '\001\033[34m\002'
        self.PURPLE = '\033[35m' if sys.platform == 'darwin' else '\001\033[35m\002'
        self.CYAN = '\033[36m' if sys.platform == 'darwin' else '\001\033[36m\002'
        self.WHITE = '\033[77m' if sys.platform == 'darwin' else '\001\033[37m\002'

        self.END = '\033[0m' if sys.platform == 'darwin' else '\001\033[0m\002'
        self.BOLD = '\033[1m' if sys.platform == 'darwin' else '\001\033[1m\002'
        self.DARK = '\033[2m' if sys.platform == 'darwin' else '\001\033[2m\002'
        self.BENT = '\033[3m' if sys.platform == 'darwin' else '\001\033[3m\002'
        self.LINE = '\033[4m' if sys.platform == 'darwin' else '\001\033[4m\002'
        self.TWINK = '\033[5m' if sys.platform == 'darwin' else '\001\033[5m\002'
        self.BACK = '\033[7m' if sys.platform == 'darwin' else '\001\033[7m\002'

        self.REMOVE = '\033[1K\r' if sys.platform == 'darwin' else '\001\033[1K\r\002'
        self.CLEAR = '\033[H\033[J' if sys.platform == 'darwin' else '\001\033[H\033[J\002'
        self.NEWLINE = '\n' if sys.platform == 'darwin' else '\001\n\002'
