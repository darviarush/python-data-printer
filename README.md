# NAME

**data_printer** - data printer and dumper

# VERSION

0.0.8

# SYNOPSIS

```python
from data_printer import p, np

import sys
from colored import fore, back, style

class A:
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

data = A(abc="acc", a=A(x=dict(p=10, r=[20, (2, 0.01)])), s='Строка\n', b=b'binary\n', r=r'\n')

# add ref to themselwes:
data.a.x['r'].append(data)  

# print colored structure to sys.stdout
p(data)

# print colored structure to file stream
p(data, file=sys.stderr)

# print uncolored structure to file stream
p(data, file=sys.stderr, color=False)

# serialize structure to string
s = np(data)

# serialize structure to string without indexes: [6] -> [0] 6
s = np(data, indexes=False)

# serialize structure to colored string (colors as escape sequences)
s = np(data, color=True)

# default color scheme
p(data, color=dict(
    bool = fore.LIGHT_BLUE,
    none = fore.LIGHT_BLUE,
    int = fore.LIGHT_YELLOW,
    float = fore.LIGHT_YELLOW,
    str = fore.LIGHT_GREEN,
    bytes = fore.LIGHT_MAGENTA,
    object = fore.LIGHT_RED,
    any = fore.LIGHT_GRAY,
    key = fore.LIGHT_CYAN,
    ref = fore.RED,
    punct = fore.WHITE,
))

# replace two colors
s = np(data, color=dict(
    bool = fore.LIGHT_RED,
    none = fore.LIGHT_YELLOW,
))

# print in perl-style (python - default) and without "[0] 7" in list "[7]". 
p(data, sep="perl", indexes=False)

# print in node-style
p(data, sep="node")

# self-style
p(data, sep=dict(
    kword=True,
    oword=True,
    kw=" => ",
    kv=" => ",
    object_open="bless {",
    object_close="}, %n",
    dict_open="{",
    dict_close="}",
    list_open="[",
    list_close="]",
    tuple_open="[",
    tuple_close="]",
    str='"%s"',
    bytes='do { use bytes; "%s" }',
    scalar='%n("%s")',      # for datetime.datetime and others
    none="undef",
    true="1",
    false="0"
))

# self-style with two and lambda on bytes
p(data, sep=dict(
    str='"%s"',
    bytes=lambda s: "".join(['Buffer.from(", ', ", ".join(["0x%X" % ch for ch in s]) ,')']),
))

# filters use for specific objects
import datetime
p([datetime.datetime.now()], filters={
    datetime.datetime: lambda obj, ddp: ddp.echo("⎈ ", ddp.color.key).echo(repr(obj), ddp.color.any),
})


# print without newline on the end
p(data, end="")

```

# DESCRIPTION

Data recursive printer. Serialize any python3 data to string or print in console or file.

Is colorised output.

Data printer check many references to one structure.

# INSTALL

```sh
$ pip install data-printer
```

# REQUIREMENTS

* colored

# AUTHOR

Kosmina O. Yaroslav <darviarush@mail.ru>

# LICENSE

MIT License

Copyright (c) 2020 Kosmina O. Yaroslav

