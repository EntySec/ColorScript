# ColorScript

ColorScript is a scripting language for designing custom ASCII banners.

## Features

* Support for most common ASCII symbols including special ones.

## Installation

```shell
pip3 install git+https://github.com/EntySec/ColorScript
```

## Examples

```python
from colorscript import ColorScript

cs = ColorScript()
print(cs.parse_colors_script('test.colors'))
```
