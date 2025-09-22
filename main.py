import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Application PyQt6 - Debug Test")
        self.setGeometry(100, 100, 400, 300)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Composants
        self.label = QLabel("👋 Bienvenue dans PyQt6 !")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.counter = 0
        self.button = QPushButton("Cliquez-moi !")
        self.button.clicked.connect(self.on_button_click)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Barre de statut
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Application prête")

    def on_button_click(self) -> None:
        """Gestionnaire de clic - placez un breakpoint ici pour tester le debug"""
        self.counter += 1
        self.label.setText(f"🎯 Bouton cliqué {self.counter} fois !")
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage(f"Compteur : {self.counter}")


def main() -> int:
    """Point d'entrée de l'application"""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())