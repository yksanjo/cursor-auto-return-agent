# ⌨️ Cursor Auto-Return Agent

![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub stars](https://img.shields.io/github/stars/yksanjo/cursor-auto-return-agent?style=social)


## 📸 Screenshots

### Main Dashboard
![Dashboard](screenshots/dashboard.png)
*Main interface and key features*

### Additional Views
![Features](screenshots/features.png)
*Additional functionality and views*

> **Note**: Screenshots will be added to the `screenshots/` directory. To add your own:
> 1. Take screenshots of your application
> 2. Save them in a `screenshots/` folder  
> 3. Update the image paths above


Automatically presses Command+Return (⌘+Enter) in Cursor IDE. Useful for triggering AI completions or other automated actions.

## Features

- ✅ Automatically presses Command+Return at configurable intervals
- ✅ Configurable press count (infinite or limited)
- ✅ Safe keyboard control with proper key release
- ✅ macOS optimized (uses pynput)

## Installation

```bash
cd cursor-auto-return-agent
pip install -r requirements.txt
```

## Usage

### Basic Usage (Infinite Presses)

```bash
python3 cursor_auto_return.py
```

This will press Command+Return every 2 seconds indefinitely. Press Ctrl+C to stop.

### Limited Presses

```bash
python3 cursor_auto_return.py --max-presses 10
```

Press Command+Return 10 times, then stop.

### Custom Interval

```bash
python3 cursor_auto_return.py --interval 1.5
```

Press every 1.5 seconds.

### Custom Delay Before Starting

```bash
python3 cursor_auto_return.py --delay 5
```

Wait 5 seconds before starting (gives you time to focus Cursor window).

## Examples

```bash
# Quick presses: 20 times, every 1 second
python3 cursor_auto_return.py --max-presses 20 --interval 1

# Slow presses: every 5 seconds, infinite
python3 cursor_auto_return.py --interval 5

# Custom: 5 presses, 3 second interval, 5 second delay
python3 cursor_auto_return.py --max-presses 5 --interval 3 --delay 5
```

## How It Works

1. The agent uses `pynput` to simulate keyboard input
2. It presses Command (⌘) + Return (Enter) simultaneously
3. Waits for the specified interval
4. Repeats until stopped or max presses reached

## Safety

- Always test with a small `--max-presses` first
- Make sure Cursor is focused before starting
- Use Ctrl+C to stop immediately if needed

## Requirements

- Python 3.7+
- macOS (for best results)
- pynput library

## License

MIT

