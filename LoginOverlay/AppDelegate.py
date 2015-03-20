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
import time

class AppDelegate(NSObject):

	LOWindowController = IBOutlet()
	image = IBOutlet()

	def applicationWillFinishLaunching_(self, sender):
		self.LOWindowController.windowDefault()
		self.LOWindowController.showBackdrop()
		
	def applicationDidFinishLaunching_(self, notification):
		img = NSImage.imageNamed_('emptymacbookpro.tiff')
		self.image.setImage_(img)