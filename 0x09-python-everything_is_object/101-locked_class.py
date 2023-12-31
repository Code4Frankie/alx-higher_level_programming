#!/usr/bin/python3
"""Definition of a locked class."""


class LockedClass:
    """
    Stops the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
