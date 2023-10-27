"""
MIT License

Copyright (c) 2020-2023 EntySec

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

import os

from typing import Tuple

from .colors import Colors


class ColorScript(object):
    """ Main class of colorscript module.

    This main class of colorscript module is intended for providing
    main ColorScript compiler.
    """

    def __init__(self) -> None:
        super().__init__()

        self.colors = Colors()
        self.script_extension = "colors"

        self.commands = {
            '%black': self.colors.BLACK,
            '%red': self.colors.RED,
            '%green': self.colors.GREEN,
            '%yellow': self.colors.YELLOW,
            '%blue': self.colors.BLUE,
            '%purple': self.colors.PURPLE,
            '%cyan': self.colors.CYAN,
            '%white': self.colors.WHITE,
            '%end': self.colors.END,
            '%bold': self.colors.BOLD,
            '%dark': self.colors.DARK,
            '%bent': self.colors.BENT,
            '%line': self.colors.LINE,
            '%twink': self.colors.TWINK,
            '%back': self.colors.BACK,
            '%remove': self.colors.REMOVE,
            '%clear': self.colors.CLEAR,
            '%newline': self.colors.NEWLINE,
        }

    def parse(self, line: str) -> str:
        """ Parse line and remove comments.

        :param str line: line to parse
        :return str: parsed line
        """

        if line and line[0:8] != "%comment" and not line.isspace():
            for command in self.commands:
                line = line.replace(command, self.commands[command])

        return line

    @staticmethod
    def _read_file_lines(path: str) -> list:
        """ Read all code lines from file and exclude comments.

        :param str path: path to file
        :return list: code lines
        """

        lines = []

        with open(path) as file:
            for line in file:
                if line and line[0:8] != "%comment" and not line.isspace():
                    lines.append(line)

        return lines

    @staticmethod
    def _reverse_read_lines(path: str) -> list:
        """ Read all code lines reversed from file.

        :param str path: path to file
        :return list: reversed code lines
        """

        lines = []

        with open(path) as file:
            for line in reversed(list(file)):
                lines.append(line)

        return lines

    def _reversed_find_last_commands(self, lines: list) -> list:
        """ Find last commands from code lines.

        :param list lines: code lines
        :return list: last commands
        """

        buffer_commands = []

        for line in lines:
            buffer_line = line

            for command in self.commands:
                if command in buffer_line:
                    buffer_line = buffer_line.replace(command, " ")

            if buffer_line.isspace():
                buffer_commands.append(line.strip())
            else:
                break

        buffer_commands.reverse()

        return buffer_commands

    def _remove_empty_lines(self, lines: list) -> list:
        """ Remove empty lines.

        :param list lines: code lines
        :return list: cleaned lines
        """

        line_id = -1

        for _ in range(len(lines)):
            buffer_line = lines[line_id]

            for command in self.commands:
                if command in buffer_line:
                    buffer_line = buffer_line.replace(command, " ")

            if buffer_line.isspace():
                lines.pop(line_id)

        return lines

    def parse_file(self, path: str) -> Tuple[str, None]:
        """ Parse ColorScript from file.

        :param str path: path to file
        :return Tuple[str, None]: parsed script or None in case of failure
        """

        result = ""

        lines = self._read_file_lines(path)
        reversed_lines = self._reverse_read_lines(path)

        last_commands = self._reversed_find_last_commands(reversed_lines)
        last_commands = "".join(map(str, last_commands))

        lines = self._remove_empty_lines(lines)
        lines[-1] = lines[-1].strip('\n') + last_commands

        if path.endswith(self.script_extension):
            try:
                buffer_commands = ""

                for line in lines:
                    buffer_line = line

                    for command in self.commands:
                        if command in buffer_line:
                            buffer_line = buffer_line.replace(command, " ")

                    if buffer_line.isspace():
                        buffer_commands += line.strip()
                    else:
                        line = buffer_commands + line
                        buffer_commands = ""

                        for command in self.commands:
                            line = line.partition('%comment')[0]
                            line = line.replace(command, self.commands[command])

                        result += line

                return result

            except BaseException:
                pass

    def compile_file(self, path: str, outfile: str = 'a.out') -> None:
        """ Compile ColorScript / Parse and write to the file.

        :param str path: path to file
        :param str outfile: path to output file
        :return None: None
        """

        result = self.parse_colors_script(path)

        if result:
            output = open(outfile, 'w')
            output.write(result)
            output.close()
