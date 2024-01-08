# ColorScript

[![Developer](https://img.shields.io/badge/developer-EntySec-blue.svg)](https://entysec.com)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://github.com/EntySec/ColorScript)
[![Forks](https://img.shields.io/github/forks/EntySec/ColorScript?style=flat&color=green)](https://github.com/EntySec/ColorScript/forks)
[![Stars](https://img.shields.io/github/stars/EntySec/ColorScript?style=flat&color=yellow)](https://github.com/EntySec/ColorScript/stargazers)
[![CodeFactor](https://www.codefactor.io/repository/github/EntySec/ColorScript/badge)](https://www.codefactor.io/repository/github/EntySec/ColorScript)

ColorScript is a scripting language for designing custom ASCII banners.

## Features

* Support for most common ASCII symbols including special ones.
* Covenient syntax, all colors marked with `%`. (`%red`, `%blue`, `%end`, etc.)
* Supports parsing files as well as just a line.

## Installation

```shell
pip3 install git+https://github.com/EntySec/ColorScript
```

## Examples

```python
from colorscript import ColorScript

cs = ColorScript()

text = """
Roses are %redred%end
Violets are %blueblue%end
Sugar is %whitesweet%end
And so are %greenyou%end
"""

print(cs.parse(text))
```
