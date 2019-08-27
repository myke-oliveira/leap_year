#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from leap_year import is_leap_year

assert is_leap_year(1600) == True
assert is_leap_year(1732) == True
assert is_leap_year(1888) == True
assert is_leap_year(1944) == True
assert is_leap_year(2008) == True

assert is_leap_year(1742) == False
assert is_leap_year(1889) == False
assert is_leap_year(1951) == False
assert is_leap_year(2011) == False
assert is_leap_year(1700) == False
