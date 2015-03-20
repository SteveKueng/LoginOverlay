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
    # create IBOutlets for max 6 screens
    # for each a window in xib is needed
    backdropWindow1 = IBOutlet()
    backdropWindow2 = IBOutlet()
    backdropWindow3 = IBOutlet()
    backdropWindow4 = IBOutlet()
    backdropWindow5 = IBOutlet()
    backdropWindow6 = IBOutlet()

    usernameLabel = IBOutlet()
    spinner = IBOutlet()

    def showBackdrop(self):
        bd = [self.backdropWindow1, self.backdropWindow2, self.backdropWindow3, self.backdropWindow4, self.backdropWindow5, self.backdropWindow6]
        for i,screen in enumerate(NSScreen.screens()):
            if i < len(bd):
                screenRect = screen.frame()

                # Create a transparent, black backdrop window that covers the whole
                # screen and fade it in slowly.
                bd[i].setCanBecomeVisibleWithoutLogin_(True)
                bd[i].setLevel_(NSScreenSaverWindowLevel)
                bd[i].setFrame_display_(screenRect, True)
                translucentColor = NSColor.darkGrayColor().colorWithAlphaComponent_(1.0)
                bd[i].setBackgroundColor_(translucentColor)
                bd[i].setOpaque_(False)
                bd[i].setIgnoresMouseEvents_(True)
                bd[i].setAlphaValue_(0.0)
                bd[i].orderFrontRegardless()

                NSAnimationContext.beginGrouping()
                NSAnimationContext.currentContext().setDuration_(0.5)
                bd[i].animator().setAlphaValue_(1.0)
                NSAnimationContext.endGrouping()

    def windowDefault(self):
        self.spinner.startAnimation_(self)
        username = NSFullUserName()
        self.usernameLabel.setStringValue_(username)