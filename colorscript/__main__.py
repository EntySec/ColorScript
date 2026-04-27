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

import os
import sys

from typing import Tuple

from .colors import *


class ColorScript(object):
    """ Main class of colorscript module.

    This main class of colorscript module is intended for providing
    main ColorScript compiler.
    """

commands = {
        '%black': BLACK,
        '%red': RED,
        '%green': GREEN,
        '%yellow': YELLOW,
        '%blue': BLUE,
        '%purple': PURPLE,
        '%cyan': CYAN,
        '%white': WHITE,
        '%end': END,
        '%bold': BOLD,
        '%dark': DARK,
        '%bent': BENT,
        '%line': LINE,
        '%twink': TWINK,
        '%back': BACK,
        '%remove': REMOVE,
        '%clear': CLEAR,
        '%newline': NEWLINE,

        '%aliceblue': ALICE_BLUE,
        '%antiquewhite': ANTIQUE_WHITE,
        '%aqua': AQUA,
        '%aquamarine': AQUAMARINE,
        '%azure': AZURE,
        '%beige': BEIGE,
        '%bisque': BISQUE,
        '%blanchedalmond': BLANCHED_ALMOND,
        '%blueviolet': BLUE_VIOLET,
        '%brown': BROWN,
        '%burlywood': BURLYWOOD,
        '%cadetblue': CADET_BLUE,
        '%chartreuse': CHARTREUSE,
        '%chocolate': CHOCOLATE,
        '%coral': CORAL,
        '%cornflowerblue': CORNFLOWER_BLUE,
        '%cornsilk': CORNSILK,
        '%crimson': CRIMSON,
        '%darkblue': DARK_BLUE,
        '%darkcyan': DARK_CYAN,
        '%darkgoldenrod': DARK_GOLDENROD,
        '%darkgray': DARK_GRAY,
        '%darkgreen': DARK_GREEN,
        '%darkkhaki': DARK_KHAKI,
        '%darkmagenta': DARK_MAGENTA,
        '%darkolivegreen': DARK_OLIVE_GREEN,
        '%darkorange': DARK_ORANGE,
        '%darkorchid': DARK_ORCHID,
        '%darkred': DARK_RED,
        '%darksalmon': DARK_SALMON,
        '%darkseagreen': DARK_SEA_GREEN,
        '%darkslateblue': DARK_SLATE_BLUE,
        '%darkslategray': DARK_SLATE_GRAY,
        '%darkturquoise': DARK_TURQUOISE,
        '%darkviolet': DARK_VIOLET,
        '%deeppink': DEEP_PINK,
        '%deepskyblue': DEEP_SKY_BLUE,
        '%dimgray': DIM_GRAY,
        '%dodgerblue': DODGER_BLUE,
        '%firebrick': FIREBRICK,
        '%floralwhite': FLORAL_WHITE,
        '%forestgreen': FOREST_GREEN,
        '%fuchsia': FUCHSIA,
        '%gainsboro': GAINSBORO,
        '%ghostwhite': GHOST_WHITE,
        '%gold': GOLD,
        '%goldenrod': GOLDENROD,
        '%gray': GRAY,
        '%greenyellow': GREEN_YELLOW,
        '%honeydew': HONEYDEW,
        '%hotpink': HOT_PINK,
        '%indianred': INDIAN_RED,
        '%indigo': INDIGO,
        '%ivory': IVORY,
        '%khaki': KHAKI,
        '%lavender': LAVENDER,
        '%lavenderblush': LAVENDER_BLUSH,
        '%lawngreen': LAWN_GREEN,
        '%lemonchiffon': LEMON_CHIFFON,
        '%lightblue': LIGHT_BLUE,
        '%lightcoral': LIGHT_CORAL,
        '%lightcyan': LIGHT_CYAN,
        '%lightgoldenrodyellow': LIGHT_GOLDENROD_YELLOW,
        '%lightgray': LIGHT_GRAY,
        '%lightgreen': LIGHT_GREEN,
        '%lightpink': LIGHT_PINK,
        '%lightsalmon': LIGHT_SALMON,
        '%lightseagreen': LIGHT_SEA_GREEN,
        '%lightskyblue': LIGHT_SKY_BLUE,
        '%lightslategray': LIGHT_SLATE_GRAY,
        '%lightsteelblue': LIGHT_STEEL_BLUE,
        '%lightyellow': LIGHT_YELLOW,
        '%lime': LIME,
        '%limegreen': LIME_GREEN,
        '%linen': LINEN,
        '%magenta': MAGENTA,
        '%maroon': MAROON,
        '%mediumaquamarine': MEDIUM_AQUAMARINE,
        '%mediumblue': MEDIUM_BLUE,
        '%mediumorchid': MEDIUM_ORCHID,
        '%mediumpurple': MEDIUM_PURPLE,
        '%mediumseagreen': MEDIUM_SEA_GREEN,
        '%mediumslateblue': MEDIUM_SLATE_BLUE,
        '%mediumspringgreen': MEDIUM_SPRING_GREEN,
        '%mediumturquoise': MEDIUM_TURQUOISE,
        '%mediumvioletred': MEDIUM_VIOLET_RED,
        '%midnightblue': MIDNIGHT_BLUE,
        '%mintcream': MINT_CREAM,
        '%mistyrose': MISTY_ROSE,
        '%moccasin': MOCCASIN,
        '%navajowhite': NAVAJO_WHITE,
        '%navy': NAVY,
        '%oldlace': OLD_LACE,
        '%olive': OLIVE,
        '%olivedrab': OLIVE_DRAB,
        '%orange': ORANGE,
        '%orangered': ORANGE_RED,
        '%orchid': ORCHID,
        '%palegoldenrod': PALE_GOLDENROD,
        '%palegreen': PALE_GREEN,
        '%paleturquoise': PALE_TURQUOISE,
        '%palevioletred': PALE_VIOLET_RED,
        '%papayawhip': PAPAYA_WHIP,
        '%peachpuff': PEACH_PUFF,
        '%peru': PERU,
        '%pink': PINK,
        '%plum': PLUM,
        '%powderblue': POWDER_BLUE,
        '%rosybrown': ROSY_BROWN,
        '%royalblue': ROYAL_BLUE,
        '%saddlebrown': SADDLE_BROWN,
        '%salmon': SALMON,
        '%sandybrown': SANDY_BROWN,
        '%seagreen': SEA_GREEN,
        '%seashell': SEA_SHELL,
        '%sienna': SIENNA,
        '%silver': SILVER,
        '%skyblue': SKY_BLUE,
        '%slateblue': SLATE_BLUE,
        '%slategray': SLATE_GRAY,
        '%snow': SNOW,
        '%springgreen': SPRING_GREEN,
        '%steelblue': STEEL_BLUE,
        '%tan': TAN,
        '%teal': TEAL,
        '%thistle': THISTLE,
        '%tomato': TOMATO,
        '%turquoise': TURQUOISE,
        '%violet': VIOLET,
        '%wheat': WHEAT,
        '%whitesmoke': WHITE_SMOKE,
        '%yellowgreen': YELLOW_GREEN,
}

    def strip(self, line: str) -> str:
        """ Strip commands from line.

        :param str line: line to strip
        :return str: stripped line
        """

        for command in self.commands:
            line = line.replace(command, '')

        return line

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

        if path.endswith('colors'):
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

        result = self.parse_file(path)

        if result:
            output = open(outfile, 'w')
            output.write(result)
            output.close()
