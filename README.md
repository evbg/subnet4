# subnet4

**subnet4** - A small and simple Python module with function to calculate the minimum subnet containing IP addresses from the input set

---

*Contents:*
**[Installation](#installation)** |
**[Documentation](#documentation)** |
**[Running the tests](#running-the-tests)** |
**[Versioning](#versioning)** |
**[Authors](#authors)** |
**[License](#license)**

---

## Getting Started

### Installation

#### Manual install
```
git clone https://github.com/evbg/subnet4.git
cd subnet4
python setup.py install
```

#### Installing directly from the [repository](https://github.com/evbg/subnet4) on GitHub.com
```
pip install git+https://github.com/evbg/subnet4.git
```


### Documentation

```
Help on package subnet4:

NAME
    subnet4

DESCRIPTION
    This module provides basic functionality for calculating
    the minimum common subnet for an arbitrary set of IP addresses


    Typical usage:

        1. Import modules:

        >>> from subnet4 import subnet4

        Optional import for conversion:
        >>> import socket
        >>> import struct

        2. Input preparation:

        a.) Optional conversion:
        >>> IPsQuad = ('192.168.0.5', '192.168.2.17', '192.168.3.21')
        >>> IPs32Bit = (socket.inet_aton(i) for i in IPsQuad)
        >>> IPsLong = (struct.unpack('!I', i)[0] for i in IPs32Bit)

        b.) Without prior conversion:
        >>> # IPsLong = (3232235525, 3232236049, 3232236309)

        3. Usage:

        >>> (Subnet_address, Subnet_mask) = subnet4(IPsLong)
        >>> print((Subnet_address, Subnet_mask))
        (3232235520, 22)

        Optional inverse transform:
        >>> Subnet_32Bit = struct.pack('!I', Subnet_address)
        >>> Subnet_quad = socket.inet_ntoa(Subnet_32Bit)
        >>> print('{}/{}'.format(Subnet_quad, Subnet_mask))
        192.168.0.0/22

PACKAGE CONTENTS
    tests (package)

FUNCTIONS
    subnet4(ip_addresses, max_address_bits=32)
        Takes an iterable sequence of positive integers.

        Returns a tuple consisting of the minimum subnet address and netmask.
        The subnet is calculated based on the received set of IP addresses.

        Examples of usage:

        # 10.0.0.0/21
        >>> subnet4(range(167772672, 167773695, 64))
        (167772160, 21)

        An empty set does not throw an exception, but returns a tuple (0, -1):
        (perhaps raising an exception should be added in the future)
        >>> subnet4([])
        (0, -1)

        >>> subnet4([0])
        (0, 31)

        >>> subnet4([1])
        (0, 31)

        >>> subnet4([2])
        (2, 31)

        >>> subnet4([2**32-1])
        (4294967294, 31)

        >>> subnet4([2, 3])
        (2, 31)

        >>> subnet4([1, 2])
        (0, 30)

        >>> subnet4([2, 3, 4])
        (0, 29)

        >>> subnet4([1, 2, 3, 4, 5])
        (0, 29)

        # 10.0.0.0/24
        >>> subnet4([167772160, 167772294, 167772192, 167772167, 167772324])
        (167772160, 24)

        # 64.0.0.0/2
        >>> subnet4([1742463364, 1311235649, 1182087098])
        (1073741824, 2)

        # 0/0
        >>> subnet4([3257689175, 1742463364, 2311235649, 3182087098, 3806496640])
        (0, 0)

DATA
    __all__ = ['subnet4']
```

## Running the tests

subnet4 has been tested on the following versions of Python: 2.7, 3.4, 3.5, 3.6, 3.7, 3.8, pypy, pypy3.

### Unit tests

#### Running the tests via [tox](https://tox.readthedocs.io/) tool
```
git clone https://github.com/evbg/subnet4.git
cd subnet4
tox
```


## Versioning

We use [SemVer](http://semver.org/) for versioning.


## Authors

* **Evgeny V. Bogodukhov** - *Initial work* - [evbg](https://github.com/evbg)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
