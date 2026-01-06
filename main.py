# pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QGridLayout

class ContactsFen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("========= Carnet d'adresses ============")  # titre
        self.setGeometry(100, 100, 400, 150)  # taille de la fenetre
        self.setStyleSheet("background-color:#99ccff;font-family:\"Times New Roman\"")

        En_tete = ["Nom", "Prénom","Téléphone", "Courriel"]

##
        grid = QGridLayout()
        self.setLayout(grid)
        for i in range(len(En_tete)):
            lbl = QLabel(En_tete[i])
            self.grid.addWidget(lbl, 0, i)

# 1 Créer un objet application Qt
        app = QApplication([])

# 3 la fenetre va etre visible
        self.show()
# 4 executer l'application
        app.exec()

