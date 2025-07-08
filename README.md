# `detect-qt-binding`

A lightweight utility to automatically detect which Qt Python binding is available in your environment.

## Features

- Detects installed Qt bindings (PyQt6, PySide6, PyQt5, PySide2, PyQt4, PySide)
- Checks both already imported modules and attempts to import available bindings
- Returns a typed `QtBindings` enum value or `None` if no binding is found

## Installation

```bash
pip install detect-qt-binding
```

## Usage

```python
from detect_qt_binding import detect_qt_binding, QtBindings

binding = detect_qt_binding()

if binding is None:
    print("No Qt binding found")
elif binding == QtBindings.PyQt6:
    print("PyQt6 detected")
# ... handle other cases
```

## API Reference

### `detect_qt_binding() -> Optional[QtBindings]`

Attempts to detect which Qt binding is available by:
1. Checking already imported modules
2. Attempting to import each known Qt binding

Returns:

- A `QtBindings` enum member if a binding is found
- `None` if no Qt binding is available

### `QtBindings` Enum

Available values:

- `PyQt6`
- `PySide6`
- `PyQt5`
- `PySide2`
- `PyQt4`
- `PySide`

## License

MIT License - Based on code from [pyqtgraph](https://github.com/pyqtgraph/pyqtgraph) (also MIT licensed)