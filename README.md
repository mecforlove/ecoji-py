# Ecoji-py 🏣🔉🦐🔼🍽🚃🔓☕

A Python3 implemention of [Ecoji](https://github.com/keith-turner/ecoji). Ecoji encodes data as 1024 [emojis][emoji], its base1024 with an emoji character set.  Give Ecoji a try at [ecoji.io](https://ecoji.io).

## Installing

- with pip

```bash
$pip3 install ecoji
```

- with source code

```bash
$git clone git@github.com:mecforlove/ecoji-py.git && cd ecoji-py && python3 setup.py install
```

## For CLI usage

- encode

```base
$echo -n hello | ecoji
👲🔩🚗🌷
```

- decode

```bash
$echo -n 👲🔩🚗🌷 | ecoji -d
hello%
```

Run `ecoji -h` to learn more about the CLI.

## For python lib

- encode

```python
>>> import io
>>> from ecoji import encode
>>> r = io.BytesIO(b'hello')
>>> w = io.StringIO()
>>> encode(r, w)
>>> print(w.getvalue())
👲🔩🚗🌷
```

- decode

```python
>>> import io
>>> from ecoji import decode
>>> r = io.StringIO('👲🔩🚗🌷')
>>> w = io.BytesIO()
>>> decode(r, w)
>>> print(w.getvalue())
b'hello'
```

Last but not the least, only Python3.x is supported.

[emoji]: https://unicode.org/emoji/
