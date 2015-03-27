//
//  AppDelegate.m
//  LoginOverlay
//
//  Created by Küng, Steve (tpc) on 26/03/15.
//  Copyright (c) 2015 github. All rights reserved.
//

#import "AppDelegate.h"

@interface AppDelegate ()

@property (weak) IBOutlet NSWindow *window;
@end

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
    [self launchbackdropWindow];
    [_spinner startAnimation:self];
    NSString *user = NSFullUserName();
    [_username setStringValue:user];
    
    //set main window
    [_window setCanBecomeVisibleWithoutLogin:true];
    [_window setLevel:NSScreenSaverWindowLevel+1];
    [_window orderFrontRegardless];
}

- (void)applicationWillTerminate:(NSNotification *)aNotification {
    // Insert code here to tear down your application
}

- (void)launchbackdropWindow {
    self.myWindowArray=[NSMutableArray new];
    NSColor *bgcolor = [NSColor darkGrayColor];
    //NSColor *bgcolor = [NSColor colorWithPatternImage:[NSImage imageNamed:@"os-x-yosemite-mac.jpg"]];
    
    int i = 0;
    for(NSScreen* screen in [NSScreen screens]) {
        NSRect screenRect = [screen frame];
        self.myWindow= [[NSWindow alloc] initWithContentRect:screenRect
                                                       styleMask:NSBorderlessWindowMask
                                                         backing:NSBackingStoreBuffered
                                                           defer:NO];
        
        
        [self.myWindow setCanBecomeVisibleWithoutLogin:true];
        [self.myWindow setLevel:NSStatusWindowLevel];
        [self.myWindow setBackgroundColor:bgcolor];
        [self.myWindow setOpaque:false];
        [self.myWindow setIgnoresMouseEvents:false];
        [self.myWindow setAlphaValue:(0.0)];
        [self.myWindow orderFrontRegardless];
        [NSAnimationContext beginGrouping];
        [[NSAnimationContext currentContext]setDuration:(0.5)];
        [[self.myWindow animator] setAlphaValue:(1.0)];
        [NSAnimationContext endGrouping];
        
        [self.myWindowArray addObject:self.myWindow];
        i++;
    }
    for (NSWindow *win in self.myWindowArray) {
        [win makeKeyAndOrderFront:NSApp];
        
    }
}

@end
