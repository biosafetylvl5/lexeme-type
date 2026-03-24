# lexeme-type

![Tests](.github/badges/tests-badge.svg)
![Coverage](.github/badges/coverage-badge.svg)
![Mypy](.github/badges/mypy-badge.svg)
![Ruff](.github/badges/ruff-badge.svg)
![Install](.github/badges/install-badge.svg)
![CSpell](.github/badges/cspell-badge.svg)
![Commitizen](.github/badges/commitizen-badge.svg)

![GitHub Release](https://img.shields.io/github/v/release/biosafetylvl5/lexeme-type)
![PyPI - Version](https://img.shields.io/pypi/v/lexeme-type)
![Pepy Total Downloads](https://img.shields.io/pepy/dt/lexeme-type?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dm/lexeme-type)
[![GitHub stars](https://img.shields.io/github/stars/biosafetylvl5/lexeme-type.svg)](https://github.com/biosafetylvl5/lexeme-type/stargazers)

# Lexeme type

Lightweight no-dependency helper for treating singular and plural spellings as equivalent.

A drop‑in str subclass that normalizes English nouns so that their
singular and plural forms compare as equal, hash to the same key, and work
inside Pydantic v2 models. Ignores capitalization.

Examples

```python
>>> from partial_lexeme.lexeme import Lexeme
>>> Lexeme("reader") == "readers" == Lexeme("readers")
True
>>> {Lexeme("analyses"): 1} == {"analysis": 1}
True

>>> from pydantic import BaseModel
>>> class _Plugin(BaseModel):
>>>     kind: Lexeme
>>>     interface: Lexeme
>>> model = _Plugin(kind="reader", interface="readers")
>>> model.kind == model.interface == "reader"
True
```
