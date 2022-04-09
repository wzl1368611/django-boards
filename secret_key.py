#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2020-8-9 23:11:00
# version: 1.0
# __author__: zhilong

import os,base64
a = os.urandom(66)
b = base64.b64encode(a)
b = b.decode()
print(b)
