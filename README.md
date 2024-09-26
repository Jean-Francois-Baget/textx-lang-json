# textx-lang-json

(./img/logos.jpg)

**textx-lang-json** is a python implementation of the JSON (JavaScript Object Notation) data interchange format [RFC8259](https://www.rfc-editor.org/rfc/rfc8259) using the [textX](https://textx.github.io/textX/) meta-language. Though it is not intended to replace the standard python JSON encoder and decoder [Lib/json](https://docs.python.org/3/library/json.html), which is much faster, it is a good alternative when you want to mix some JSON in your own textX grammar, or a good starting point should you want to develop your own JSON-like grammar.

The `textxjson` package provides a parser (basically a *textX* *metamodel*), able to build a *textx* *model* from a JSON file or string. This model can be visualized, for educational purpose, but more importantly can be *decoded* to obtain the usual (as done by [Lib/json](https://docs.python.org/3/library/json.html)) python representation of the JSON document.

## Installation

TO DO when registered on pip.

### Testing

```
python -m unittest
```
```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.452s

OK
```


## Usage

### Obtaining the parser

The first thing 

```python
from textx import metamodel_for_language

parser = metamodel_for_language('textxjson')
```


