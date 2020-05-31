# -*- coding: utf-8 -*-
"""
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
"""
__all__ = ['subnet4']


def subnet4(ip_addresses, max_address_bits=32):
    """
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
    """
    assert hasattr(ip_addresses, '__iter__') is True
    assert type(max_address_bits) is int and max_address_bits > 0
    max_address = 2 ** max_address_bits - 1
    addition, product = 0, max_address
    for ip_address in ip_addresses:
        assert hasattr(ip_address, '__and__') and hasattr(ip_address, '__or__')
        addition |= ip_address
        product &= ip_address
    ip_address_bits = len(bin(addition - product)) - 2
    net_address = addition & (max_address ^ (2 ** ip_address_bits - 1))
    return net_address, (max_address_bits - ip_address_bits)
