# ColorScript

<p>
    <a href="https://entysec.com">
        <img src="https://img.shields.io/badge/developer-EntySec-blue.svg">
    </a>
    <a href="https://github.com/EntySec/ColorScript">
        <img src="https://img.shields.io/badge/language-Python-blue.svg">
    </a>
    <a href="https://github.com/EntySec/ColorScript/forks">
        <img src="https://img.shields.io/github/forks/EntySec/ColorScript?color=green">
    </a>
    <a href="https://github.com/EntySec/ColorScript/stargazers">
        <img src="https://img.shields.io/github/stars/EntySec/ColorScript?color=yellow">
    </a>
    <a href="https://www.codefactor.io/repository/github/EntySec/ColorScript">
        <img src="https://www.codefactor.io/repository/github/EntySec/ColorScript/badge">
    </a>
</p>

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
