# Programme utiliser sqlite et PyQt6
# Importer les packages necessaires

import sqlite3

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QLabel, \
    QMessageBox


def popup_warning(titre, message):
    QMessageBox.warning(fen, titre, message)


def CreerTable():
    print("créer la table")
    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute(
        "CREATE TABLE if not exists Persons(PersonID int PRIMARY KEY,Nom varchar(255),Prenom varchar(255),Mail varchar(255));")
    conn.commit()


def InsererDansTablePersonne():
    print("inser dans la table")

    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    # requette ici
    try:
        cursor.execute(
            "INSERT INTO Persons VALUES (" + lineEditID.text() + ",'" + lineEditNom.text() + "','" + lineEditPreNom.text() + "','" + lineEditMail.text() + "');")
    except Exception as e:
        print("L'ID doit être un entier pas encore enregistré")
        popup_warning("Attention", "L'ID doit être un entier pas encore enregistré")

    conn.commit()
    AfficherTout()


def SupprimerId():
    print("supprimer dans la table")
    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    # requette ici
    try:
        cursor.execute("DELETE FROM Persons WHERE PersonID=" + lineEditSuppID.text() + ";")
    except Exception as e:
        print("Bien vouloir sélectionner l'ID du contact à supprimer")
        popup_warning("Attention", "Bien vouloir sélectionner l'ID du contact à supprimer.")

    conn.commit()
    AfficherTout()


def AfficherTout():
    print("afficher toute la table")
    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    # requette ici
    cursor.execute("SELECT * FROM Persons")
    resultat = cursor.fetchall()

    # QTable
    qtab.setRowCount(len(resultat))
    qtab.setColumnCount(4)
    qtab.setGeometry(50, 250, 450, 200)
    qtab.setHorizontalHeaderLabels(['Id', 'Nom', 'Prénom', 'Mail'])
    #
    for i in range(len(resultat)):
        for j in range(4):
            qtab.setItem(i, j, QTableWidgetItem(str(resultat[i][j])))


def ModifierTable():
    global selected_row
    if selected_row < 0:
        print("Aucune ligne sélectionnée")
        return

    # Afficher le NOUVEAU texte (ex : la colonne Nom)
    print("Modifier la table")
    newNom = qtab.item(selected_row, 1).text()
    print("Nouveau Nom:", qtab.item(selected_row, 1).text())
    newPrenom = qtab.item(selected_row, 2).text()
    print("Nouveau Prenom:", qtab.item(selected_row, 2).text())
    newMail = qtab.item(selected_row, 3).text()
    print("Nouveau Mail:", newMail)
    SelectID = qtab.item(selected_row, 0).text()

    conn = sqlite3.connect("projet.db")
    cursor = conn.cursor()
    print("Select ID:" + SelectID)
    print(
        "UPDATE Persons SET Nom='" + newNom + "', Prenom='" + newPrenom + "', Mail='" + newMail + "'  WHERE PersonID=" + SelectID + ";")
    cursor.execute(
        "UPDATE Persons SET Nom='" + newNom + "', Prenom='" + newPrenom + "', Mail='" + newMail + "'  WHERE PersonID=" + SelectID + ";")

    print("Nouveau Nom:" + newNom)
    conn.commit()
    print("Nouveau Nom:" + newNom)
    AfficherTout()


# 1-fenetre
app = QApplication([])
fen = QWidget()
fen.setWindowTitle("/*/  Carnet d'Adresses  /*/")
fen.setGeometry(100, 100, 650, 500)
fen.setStyleSheet("""
    QWidget {
        background: qlineargradient(
            x1:0, y1:0, x2:0, y2:1,
            stop:0 #d4f5e3,
            stop:1 #b8ebd1
        );
    }
""")
CreerTable()

labelTitre = QLabel("Carnet d'adresses", fen)
labelTitre.setGeometry(0, 0, 650, 50)  # largeur de la fenêtre, hauteur du bandeau
labelTitre.setAlignment(Qt.AlignmentFlag.AlignCenter)

labelTitre.setStyleSheet("""
    background-color: #2ecc71;   /* vert doux */
    color: white;
    font-size: 22px;
    font-weight: bold;
    border-bottom: 2px solid #27ae60;
""")

# 2- Créer un boutton créer la table
# btn1 = QPushButton(fen)
# btn1.setText("Créer Table")
# btn1.setGeometry(500, 100, 100, 30)
# btn1.clicked.connect(CreerTable)

# 2- Créer un boutton inserer
btn2 = QPushButton(fen)
btn2.setText("Inserer")
btn2.setGeometry(500, 150, 100, 30)
btn2.setStyleSheet("""

    font-weight: bold;
    font-size: 12px;
    background-color: #a8e6c8;
    padding: 4px;
    border: 1px solid #7fcfa9;

""")
btn2.clicked.connect(InsererDansTablePersonne)

# 2- Créer des champs pour le btn inserer
lineEditID = QLineEdit(fen)
lineEditID.setGeometry(50, 150, 100, 30)
lineEditNom = QLineEdit(fen)
lineEditNom.setGeometry(150, 150, 100, 30)
lineEditPreNom = QLineEdit(fen)
lineEditPreNom.setGeometry(250, 150, 100, 30)
lineEditMail = QLineEdit(fen)
lineEditMail.setGeometry(350, 150, 100, 30)

# 2- Créer un boutton AfficherTout
# btn3 = QPushButton(fen)
# btn3.setText("AfficherTout")
# btn3.setGeometry(500, 250, 100, 30)
# btn3.clicked.connect(AfficherTout)


# 2- Créer un boutton modifier la table
btn5 = QPushButton(fen)
btn5.setText("Modifier")
btn5.setGeometry(500, 250, 100, 30)
btn5.setStyleSheet("""

    font-weight: bold;
    font-size: 12px;
    background-color: #a8e6c8;
    padding: 4px;
    border: 1px solid #7fcfa9;

""")
btn5.clicked.connect(ModifierTable)

# QTable
qtab = QTableWidget(fen)
qtab.setRowCount(4)
qtab.setColumnCount(4)
qtab.setGeometry(50, 250, 450, 200)
qtab.setStyleSheet("""
    QHeaderView::section {
        font-weight: bold;
        font-size: 12px;
        background-color: #a8e6c8;
        padding: 4px;
        border: 1px solid #7fcfa9;
    }
""")
qtab.setHorizontalHeaderLabels(['Id', 'Nom', 'Prénom', 'Mail'])

selected_row = -1


def getClickedCell(row, column):
    print('clicked!', row, column)
    print(qtab.item(row, column).text())
    global selected_row
    selected_row = row


#    lineEditSuppID.setText(str(qtab.item(row, column).text()))


qtab.cellClicked.connect(getClickedCell)

#
# 2- Créer un boutton supprimer
btn4 = QPushButton(fen)
btn4.setText("Supprimer")
btn4.setGeometry(500, 200, 100, 30)
btn4.setStyleSheet("""

    font-weight: bold;
    font-size: 12px;
    background-color: #a8e6c8;
    padding: 4px;
    border: 1px solid #7fcfa9;

""")
btn4.clicked.connect(SupprimerId)

# lineEditSuppID = QLineEdit(fen)
# lineEditSuppID.setGeometry(350, 200, 100, 30)

AfficherTout()
fen.show()
app.exec()