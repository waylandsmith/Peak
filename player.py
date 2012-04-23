#/usr/bin/env python

import os
import pickle

# Player stats:

class PC(object):
    def __init__(self, name, physical, mental, status):
        self.name = name
        self.physical = physical
        self.mental = mental
        self.status = status
