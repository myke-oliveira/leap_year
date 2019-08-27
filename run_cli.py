#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:50:55 2019

@author: myke
"""

from leap_year import is_leap_year

def main():
    while True:
        try:
            year = int(input('Type a year: '))
            break
        except ValueError:
            print('Invalid Value. Try again.')
    
    print(f'{year}: {"Leap Year" if is_leap_year(year) else "Not a Leap Year"}')

if __name__ == '__main__':
    main()
        