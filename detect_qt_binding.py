import sys

from enum import Enum
from typing import Optional


class QtBindings(Enum):
    PyQt6 = 'PyQt6'
    PySide6 = 'PySide6'
    PyQt5 = 'PyQt5'
    PySide2 = 'PySide2'
    PyQt4 = 'PyQt4'
    PySide = 'PySide'


def detect_qt_binding():
    # type: () -> Optional[QtBindings]

    # Check if any Qt binding is already imported
    for enum_member in QtBindings:
        if enum_member.value in sys.modules:
            return enum_member

    # Try importing if none found
    for enum_member in QtBindings:
        try:
            __import__(enum_member.value)
            return enum_member
        except ImportError:
            pass

    return None
