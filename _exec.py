#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

if __name__ == '__main__':
    run = os.system('%s %s' % (sys.argv[1], sys.argv[2]))
    print '\nProgram exit with code "%d"' % run
    time.sleep(1000)

#print sys.argv
