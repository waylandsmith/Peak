#/usr/bin/env python

import os
import pickle

# Player stats:

class PC(object):
    def __init__(self, name, physical, mental, spd, status):
        self.name = name
        self.physical = physical
        self.mental = mental
        self.spd = spd
        self.status = str(status)
    def chkStatus(self,physical,mental,spd):
        if self.physical < 0:
            self.status = "dead"
        elif self.mental < 0:
            self.status = "faint"
        elif self.spd < 0:
            self.status = "tko"
        return self.status
