# NAME

ddp - data printer

# VERSION

0.0.1

# SYNOPSIS

```
import sys
from ddp import p, np

class A:
    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

data = A(abc="acc", a=A(x=dict(p=10, r=[20, (2, 0.01)])), s='Строка\n', b=b'binary\n', r=r'\n')

# print colored structure to sys.stdout
p(data)

# print colored structure to file stream
p(data, file=sys.stderr)

# print uncolored structure to file stream
p(data, file=sys.stderr, color=False)

# serialize structure to string
s = np(data)

# serialize structure to colored string (colors as escape sequences)
s = np(data, color=True)
```

# DESCRIPTION

Data recursive printer. Serialize any python3 data to string or print in console or file. 

# INSTALL

```sh
$ pip install ddp
```

# REQUIREMENTS

* colored

# AUTHOR

Kosmina O. Yaroslav <dart@cpan.org>

# LICENSE

MIT License

Copyright (c) 2020 Kosmina O. Yaroslav

