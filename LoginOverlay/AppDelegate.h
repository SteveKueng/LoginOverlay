//
//  AppDelegate.h
//  LoginOverlay
//
//  Created by Küng, Steve (tpc) on 26/03/15.
//  Copyright (c) 2015 github. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface AppDelegate : NSObject <NSApplicationDelegate>
@property (weak) IBOutlet NSWindow *backdropWindow;
@property (weak) IBOutlet NSProgressIndicator *spinner;
@property (weak) IBOutlet NSTextField *username;
@property(strong) NSMutableArray *myWindowArray;
@property (strong)NSWindow* myWindow;
@property (weak) IBOutlet NSImageView *image;
@end

