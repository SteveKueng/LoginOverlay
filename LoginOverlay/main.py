# -*- coding: utf-8 -*-
#
#  main.py
#  LoginOverlay
#
#  Created by Steve Küng on 17/03/15.
#  Copyright (c) 2015 Steve Küng. All rights reserved.
#

# import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import AppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
