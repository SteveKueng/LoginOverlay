# -*- coding: utf-8 -*-
#
#  LoginOverlayAppDelegate.py
#  LoginOverlay
#
#  Created by Steve Küng on 17/03/15.
#  Copyright (c) 2015 Steve Küng. All rights reserved.
#

from objc import IBOutlet
from Foundation import *
from AppKit import *

class AppDelegate(NSObject):
    
    backdropWindow = IBOutlet()
    
    def applicationDidFinishLaunching_(self, sender):
        self.backdropWindow.showBackdrop()
