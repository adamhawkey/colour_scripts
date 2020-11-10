#!/usr/bin/env python
# -*- coding: utf-8 -*-

import colour
from colour.utilities.verbose import message_box
"""
C = 18 / 100
"""
C = input("Enter a 10bit Value: ")

message_box(('Encoding to video component signal value using "BT.709" OETF '
             'and given linear-light value:\n'
             '\n\t{0}'.format(C)))
print(colour.oetf_BT709(C))
print(colour.oetf(C, function='BT.709'))

print('\n')
