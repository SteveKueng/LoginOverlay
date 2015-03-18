# -*- coding: utf-8 -*-
#
#  LOWindowController.py
#  LoginOverlay
#
#  Created by Steve Küng on 18/03/15.
#  Copyright (c) 2015 Steve Küng. All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *

class LOWindowController(NSObject):
    backdropWindow = IBOutlet()
    window = IBOutlet()
    
    def showBackdrop(self):
        self.window.setLevel_(NSScreenSaverWindowLevel + 1)
        
        for screen in NSScreen.screens():
            # Base all sizes on the screen's dimensions.
            screenRect = screen.frame()
        
            # Create a transparent, black backdrop window that covers the whole
            # screen and fade it in slowly.
            self.backdropWindow.setCanBecomeVisibleWithoutLogin_(True)
            self.backdropWindow.setLevel_(NSScreenSaverWindowLevel)
            self.backdropWindow.setFrame_display_(screenRect, True)
            translucentColor = NSColor.darkGrayColor().colorWithAlphaComponent_(1.0)
            self.backdropWindow.setBackgroundColor_(translucentColor)
            self.backdropWindow.setOpaque_(False)
            self.backdropWindow.setIgnoresMouseEvents_(False)
            self.backdropWindow.setAlphaValue_(0.0)
            self.backdropWindow.orderFrontRegardless()
            NSAnimationContext.beginGrouping()
            NSAnimationContext.currentContext().setDuration_(0.5)
            self.backdropWindow.animator().setAlphaValue_(1.0)
            NSAnimationContext.endGrouping()

