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
    usernameLabel = IBOutlet()
    image = IBOutlet()
    
    def showBackdrop(self):       
        # Base all sizes on the screen's dimensions.
        screenRect = NSScreen.mainScreen().frame()
        
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
        NSAnimationContext.currentContext().setDuration_(1.0)
        self.backdropWindow.animator().setAlphaValue_(1.0)
        NSAnimationContext.endGrouping()

    def windowDefault(self):
        username = NSFullUserName()
        self.usernameLabel.setStringValue_(username)
        self.image.image('/Users/kuengst/Desktop/imac.tiff')