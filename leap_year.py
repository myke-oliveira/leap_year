#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:29:35 2019

@author: myke
"""

is_leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
