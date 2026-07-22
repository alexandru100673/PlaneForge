"""PlaneForge application entry point."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from planeforge.ui.main_window import MainWindow


def main() -> int:
    """Start the PlaneForge desktop application."""
    application = QApplication(sys.argv)
    application.setApplicationName("PlaneForge")
    application.setOrganizationName("PlaneForge")

    main_window = MainWindow()
    main_window.show()

    return application.exec()


if __name__ == "__main__":
    raise SystemExit(main())