# Ecoji 🏣🔉🦐🔼

Ecoji encodes data as 1024 [emojis][emoji], its base1024 with an emoji character set.  As a bonus, includes code to decode emojis to original data.
The idea is from [here](https://github.com/keith-turner/ecoji). And this project is the implemention of Python3.

## Installing

- with pip

```bash
$pip install ecoji
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

If you want to know more about the CLI, just type `ecoji -h` in your terminal.

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