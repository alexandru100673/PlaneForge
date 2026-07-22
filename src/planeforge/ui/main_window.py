"""Main application window for PlaneForge."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog, QLabel, QMainWindow, QToolBar


class MainWindow(QMainWindow):
    """Top-level window of the PlaneForge desktop application."""

    def __init__(self) -> None:
        """Initialize the main PlaneForge window."""
        super().__init__()

        self.setWindowTitle("PlaneForge")
        self.resize(1200, 800)
        self.setMinimumSize(800, 600)

        self._create_actions()
        self._create_menu_bar()
        self._create_toolbar()
        self._create_central_widget()
        self._create_status_bar()

    def _create_actions(self) -> None:
        """Create reusable user-interface actions."""
        self.open_pdf_action = QAction("Open PDF...", self)
        self.open_pdf_action.setShortcut("Ctrl+O")
        self.open_pdf_action.setStatusTip("Open a PDF plan")
        self.open_pdf_action.triggered.connect(self.open_pdf)

        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.setStatusTip("Close PlaneForge")
        self.exit_action.triggered.connect(self.close)

    def _create_menu_bar(self) -> None:
        """Create the application menu bar."""
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(self.open_pdf_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        self.menuBar().addMenu("&View")
        self.menuBar().addMenu("&Help")

    def _create_toolbar(self) -> None:
        """Create the main application toolbar."""
        toolbar = QToolBar("Main Toolbar", self)
        toolbar.setObjectName("main_toolbar")
        toolbar.setMovable(False)
        toolbar.addAction(self.open_pdf_action)

        self.addToolBar(toolbar)

    def _create_central_widget(self) -> None:
        """Create the initial empty document workspace."""
        self.placeholder = QLabel("No PDF loaded")
        self.placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.placeholder.setStyleSheet(
            """
            QLabel {
                color: #808080;
                font-size: 22px;
                border: 1px dashed #606060;
                margin: 24px;
            }
            """
        )

        self.setCentralWidget(self.placeholder)

    def open_pdf(self) -> None:
        """Open a Windows file dialog and select a PDF document."""
        file_path, _selected_filter = QFileDialog.getOpenFileName(
            self,
            "Open PDF plan",
            "",
            "PDF files (*.pdf)",
        )

        if not file_path:
            self.statusBar().showMessage("Open PDF cancelled", 3000)
            return

        selected_pdf = Path(file_path)

        self.placeholder.setText(selected_pdf.name)
        self.statusBar().showMessage(f"Selected: {selected_pdf}")

    def _create_status_bar(self) -> None:
        """Create the application status bar."""
        self.statusBar().showMessage("Ready")