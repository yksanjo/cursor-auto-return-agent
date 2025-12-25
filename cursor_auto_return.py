#!/usr/bin/env python3
"""
Cursor Auto-Return Agent
Automatically presses Command+Return (⌘+Enter) in Cursor IDE
This can be used to trigger AI completions or other actions automatically.
"""

import time
import sys
import platform
from typing import Optional

try:
    if platform.system() == "Darwin":  # macOS
        from pynput import keyboard
        from pynput.keyboard import Key, KeyCode
    else:
        print("⚠️  This script is designed for macOS. For other platforms, use pyautogui.")
        from pynput import keyboard
        from pynput.keyboard import Key, KeyCode
except ImportError:
    print("❌ Error: 'pynput' library is required. Install it with: pip install pynput")
    sys.exit(1)


class CursorAutoReturnAgent:
    """Agent that automatically presses Command+Return in Cursor IDE."""
    
    def __init__(self, interval: float = 2.0, max_presses: Optional[int] = None):
        """
        Initialize the auto-return agent.
        
        Args:
            interval: Time in seconds between each Command+Return press
            max_presses: Maximum number of presses (None for infinite)
        """
        self.interval = interval
        self.max_presses = max_presses
        self.press_count = 0
        self.running = False
        self.controller = keyboard.Controller()
        
    def press_command_return(self):
        """Press Command+Return combination."""
        try:
            # Press Command (⌘) + Return
            self.controller.press(Key.cmd)
            self.controller.press(Key.enter)
            time.sleep(0.05)  # Small delay for key press
            self.controller.release(Key.enter)
            self.controller.release(Key.cmd)
            
            self.press_count += 1
            print(f"✅ Pressed Command+Return ({self.press_count})")
            return True
        except Exception as e:
            print(f"❌ Error pressing keys: {e}")
            return False
    
    def start(self, delay: float = 3.0):
        """
        Start the auto-return agent.
        
        Args:
            delay: Initial delay before starting (gives time to focus Cursor)
        """
        print("🚀 Cursor Auto-Return Agent")
        print(f"⏱️  Interval: {self.interval} seconds")
        print(f"🔢 Max presses: {self.max_presses or 'Infinite'}")
        print(f"⏳ Starting in {delay} seconds... (Focus Cursor window now!)")
        print("⚠️  Press Ctrl+C to stop\n")
        
        time.sleep(delay)
        
        self.running = True
        
        try:
            while self.running:
                if self.max_presses and self.press_count >= self.max_presses:
                    print(f"\n✅ Reached max presses ({self.max_presses}). Stopping.")
                    break
                
                self.press_command_return()
                time.sleep(self.interval)
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Stopped by user")
            self.stop()
    
    def stop(self):
        """Stop the auto-return agent."""
        self.running = False
        print(f"📊 Total presses: {self.press_count}")


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Automatically press Command+Return in Cursor IDE",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Press Command+Return every 2 seconds (infinite)
  python3 cursor_auto_return.py
  
  # Press 10 times with 3 second interval
  python3 cursor_auto_return.py --max-presses 10 --interval 3
  
  # Quick presses every 1 second
  python3 cursor_auto_return.py --interval 1
        """
    )
    
    parser.add_argument("--interval", type=float, default=2.0,
                       help="Time in seconds between presses (default: 2.0)")
    parser.add_argument("--max-presses", type=int, default=None,
                       help="Maximum number of presses (default: infinite)")
    parser.add_argument("--delay", type=float, default=3.0,
                       help="Initial delay before starting (default: 3.0)")
    
    args = parser.parse_args()
    
    agent = CursorAutoReturnAgent(
        interval=args.interval,
        max_presses=args.max_presses
    )
    
    agent.start(delay=args.delay)


if __name__ == "__main__":
    main()

