//
//  AppDelegate.m
//  LoginOverlay
//
//  Created by Küng, Steve (tpc) on 26/03/15.
//  Copyright (c) 2015 github. All rights reserved.
//

#import "AppDelegate.h"
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/sysctl.h>

@interface AppDelegate ()

@property (weak) IBOutlet NSWindow *window;
@end

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
    // start the backdropwindows
    [self launchbackdropWindow];
    
    // start spinner animation
    [_spinner startAnimation:self];
    
    //get username and write to label
    NSString *user = NSFullUserName();
    [_username setStringValue:user];
    
    //set image for hardware
    [_image setImage:[NSImage imageNamed:[self getImage]]];
    
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

- (NSString *) machineModel {
    size_t len = 0;
    sysctlbyname("hw.model", NULL, &len, NULL, 0);
    
    if (len)
    {
        char *model = malloc(len*sizeof(char));
        sysctlbyname("hw.model", model, &len, NULL, 0);
        NSString *model_ns = [NSString stringWithUTF8String:model];
        free(model);
        return model_ns;
    }
    
    return @"Just an Apple Computer"; //incase model name can't be read
}

- (NSString *)getImage {
    NSString *model = [self machineModel];
    NSString *img = @"";
    
    if ([model hasPrefix:@"MacBookAir"]) {
        img = @"emptymacbookair.tiff";
    } else if ([model hasPrefix:@"MacBookPro"]) {
        img = @"emptymacbookpro.tiff";
    } else if ([model hasPrefix:@"MacMini"]) {
        img = @"emptymacmini.tiff";
    } else if ([model hasPrefix:@"iMac"]) {
        img = @"emptyimac.tiff";
    } else {
        img = @"emptygenericdisplay.tiff";
    }
    return img;
}

@end
