from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import connection
import error_codes
import customer
import diagrams


class ErrorMessage(QMessageBox):
    def setupUi(self, msg, message):
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)


class Tab(QtWidgets.QWidget):

    def setupUi(self, tab_2, Name):
        tab_2.setObjectName(Name)
        current_customer = customer.Customer(Name, {})

        def sprawdzStan():
            self.stanPortfelaContent.setText(current_customer.getCurrencies())
            self.SprawdzStanFrame.setVisible(True)
            self.KupWaluteFrame.setVisible(False)
            self.WymienWaluteFrame.setVisible(False)
            self.sprawdzStanButton.setStyleSheet("background-color : #999")
            self.kupWaluteButton.setStyleSheet("background-color : #ccc")
            self.wymienWaluteButton.setStyleSheet("background-color : #ccc")
            self.sprawdzStanButton.setEnabled(False)
            self.kupWaluteButton.setEnabled(True)
            self.wymienWaluteButton.setEnabled(True)
            self.sprawdzStanImage.setVisible(True)
            self.kupWaluteImage.setVisible(False)
            self.wymienWaluteImage.setVisible(False)

        self.sprawdzStanButton = QtWidgets.QPushButton(tab_2)
        self.sprawdzStanButton.clicked.connect(sprawdzStan)
        self.sprawdzStanButton.setGeometry(QtCore.QRect(30, 50, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sprawdzStanButton.setFont(font)
        self.sprawdzStanButton.setObjectName("sprawdzStanButton")
        self.sprawdzStanButton.setStyleSheet("background-color : #ccc")

        def kupWalute():
            self.KupWaluteFrame.setVisible(True)
            self.SprawdzStanFrame.setVisible(False)
            self.WymienWaluteFrame.setVisible(False)
            self.sprawdzStanButton.setStyleSheet("background-color : #ccc")
            self.kupWaluteButton.setStyleSheet("background-color : #999")
            self.wymienWaluteButton.setStyleSheet("background-color : #ccc")
            self.sprawdzStanButton.setEnabled(True)
            self.kupWaluteButton.setEnabled(False)
            self.wymienWaluteButton.setEnabled(True)
            self.sprawdzStanImage.setVisible(False)
            self.kupWaluteImage.setVisible(True)
            self.wymienWaluteImage.setVisible(False)

        self.kupWaluteButton = QtWidgets.QPushButton(tab_2)
        self.kupWaluteButton.clicked.connect(kupWalute)
        self.kupWaluteButton.setGeometry(QtCore.QRect(30, 200, 241, 91))
        self.kupWaluteButton.setFont(font)
        self.kupWaluteButton.setObjectName("kupWaluteButton")
        self.kupWaluteButton.setStyleSheet("background-color : #ccc")

        def wymienWalute():
            self.KupWaluteFrame.setVisible(False)
            self.SprawdzStanFrame.setVisible(False)
            self.WymienWaluteFrame.setVisible(True)
            self.sprawdzStanButton.setStyleSheet("background-color : #ccc")
            self.kupWaluteButton.setStyleSheet("background-color : #ccc")
            self.wymienWaluteButton.setStyleSheet("background-color : #999")
            self.sprawdzStanButton.setEnabled(True)
            self.kupWaluteButton.setEnabled(True)
            self.wymienWaluteButton.setEnabled(False)
            self.sprawdzStanImage.setVisible(False)
            self.kupWaluteImage.setVisible(False)
            self.wymienWaluteImage.setVisible(True)

        self.wymienWaluteButton = QtWidgets.QPushButton(tab_2)
        self.wymienWaluteButton.clicked.connect(wymienWalute)
        self.wymienWaluteButton.setGeometry(QtCore.QRect(30, 350, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wymienWaluteButton.setFont(font)
        self.wymienWaluteButton.setObjectName("wymienWaluteButton")
        self.wymienWaluteButton.setStyleSheet("background-color : #ccc")

        self.SprawdzStanFrame = QtWidgets.QFrame(tab_2)
        self.SprawdzStanFrame.setGeometry(QtCore.QRect(330, 180, 361, 321))
        self.SprawdzStanFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SprawdzStanFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SprawdzStanFrame.setObjectName("SprawdzStanFrame")
        self.SprawdzStanFrame.setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(14)

        self.sprawdzStanImage = QtWidgets.QLabel(tab_2)
        self.sprawdzStanImage.setGeometry(QtCore.QRect(450, 30, 111, 111))
        self.sprawdzStanImage.setText("")
        self.sprawdzStanImage.setPixmap(QtGui.QPixmap("wallet.png"))
        self.sprawdzStanImage.setObjectName("sprawdzStanImage")
        self.sprawdzStanImage.setVisible(False)

        # Creating SprawdzStanFrame
        self.stanPortfelaLabel = QtWidgets.QLabel(self.SprawdzStanFrame)
        self.stanPortfelaLabel.setGeometry(QtCore.QRect(20, 0, 131, 31))
        self.stanPortfelaLabel.setObjectName("stanPortfelaLabel")
        self.stanPortfelaLabel.setFont(font)

        self.stanPortfelaContent = QtWidgets.QLabel(self.SprawdzStanFrame)
        self.stanPortfelaContent.setGeometry(QtCore.QRect(20, 40, 321, 261))
        self.stanPortfelaContent.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.stanPortfelaContent.setObjectName("stanPortfelaContent")
        self.stanPortfelaContent.setFont(font)
        # End of creating SprawdzStanFrame

        self.KupWaluteFrame = QtWidgets.QFrame(tab_2)
        self.KupWaluteFrame.setGeometry(QtCore.QRect(300, 160, 411, 211))
        self.KupWaluteFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KupWaluteFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KupWaluteFrame.setObjectName("KupWaluteFrame")
        self.KupWaluteFrame.setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(14)

        self.kupWaluteImage = QtWidgets.QLabel(tab_2)
        self.kupWaluteImage.setGeometry(QtCore.QRect(450, 30, 111, 111))
        self.kupWaluteImage.setText("")
        self.kupWaluteImage.setPixmap(QtGui.QPixmap("money.png"))
        self.kupWaluteImage.setObjectName("kupWaluteLabel")
        self.kupWaluteImage.setVisible(False)

        # Creating KupWaluteFrame
        self.walutaComboBox = QtWidgets.QComboBox(self.KupWaluteFrame)
        self.walutaComboBox.setGeometry(QtCore.QRect(200, 40, 141, 31))
        self.walutaComboBox.setObjectName("walutaComboBox")
        self.walutaComboBox.addItems(connection.ReadTableOfCurrencies())
        self.walutaComboBox.setFont(font)

        self.wybierzWaluteLabel = QtWidgets.QLabel(self.KupWaluteFrame)
        self.wybierzWaluteLabel.setGeometry(QtCore.QRect(40, 40, 141, 31))
        self.wybierzWaluteLabel.setObjectName("wybierzWaluteLabel")
        self.wybierzWaluteLabel.setText("Wybierz walutę:")
        self.wybierzWaluteLabel.setFont(font)

        self.iloscLabel = QtWidgets.QLabel(self.KupWaluteFrame)
        self.iloscLabel.setGeometry(QtCore.QRect(40, 80, 91, 41))
        self.iloscLabel.setObjectName("iloscLabel")
        self.iloscLabel.setText("Ilość:")
        self.iloscLabel.setFont(font)

        self.iloscSpinBox = QtWidgets.QDoubleSpinBox(self.KupWaluteFrame)
        self.iloscSpinBox.setGeometry(QtCore.QRect(200, 90, 141, 31))
        self.iloscSpinBox.setObjectName("iloscSpinBox")
        self.iloscSpinBox.setMaximum(1e+18)
        self.iloscSpinBox.setFont(font)

        def kup():
            amount = self.iloscSpinBox.text().replace(",", ".")
            current_customer.payment(self.walutaComboBox.currentText(), float(amount))

        self.kupButton = QtWidgets.QPushButton(self.KupWaluteFrame)
        self.kupButton.clicked.connect(kup)
        self.kupButton.setGeometry(QtCore.QRect(130, 140, 131, 41))
        self.kupButton.setObjectName("kupButton")
        self.kupButton.setText("Kup")
        self.kupButton.setFont(font)
        # End of creating KupWaluteFrame

        self.WymienWaluteFrame = QtWidgets.QFrame(tab_2)
        self.WymienWaluteFrame.setGeometry(QtCore.QRect(300, 160, 401, 301))
        self.WymienWaluteFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WymienWaluteFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WymienWaluteFrame.setObjectName("WymienWaluteFrame")
        self.WymienWaluteFrame.setVisible(False)

        self.wymienWaluteImage = QtWidgets.QLabel(tab_2)
        self.wymienWaluteImage.setGeometry(QtCore.QRect(450, 30, 111, 111))
        self.wymienWaluteImage.setText("")
        self.wymienWaluteImage.setPixmap(QtGui.QPixmap("exchange.png"))
        self.wymienWaluteImage.setObjectName("wymienWaluteLabel")
        self.wymienWaluteImage.setVisible(False)

        # Creating WymienWaluteFrame
        self.kupLabel = QtWidgets.QLabel(self.WymienWaluteFrame)
        self.kupLabel.setGeometry(QtCore.QRect(50, 40, 121, 31))
        self.kupLabel.setObjectName("kupLabel")
        self.kupLabel.setText("Kup walutę: ")
        self.kupLabel.setFont(font)

        self.iloscWLabel = QtWidgets.QLabel(self.WymienWaluteFrame)
        self.iloscWLabel.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.iloscWLabel.setObjectName("IloscWLabel")
        self.iloscWLabel.setText("Ilość:")
        self.iloscWLabel.setFont(font)

        self.zaLabel = QtWidgets.QLabel(self.WymienWaluteFrame)
        self.zaLabel.setGeometry(QtCore.QRect(50, 160, 111, 31))
        self.zaLabel.setObjectName("zaLabel")
        self.zaLabel.setText("Za walutę:")
        self.zaLabel.setFont(font)

        self.iloscWSpinBox = QtWidgets.QDoubleSpinBox(self.WymienWaluteFrame)
        self.iloscWSpinBox.setGeometry(QtCore.QRect(180, 100, 141, 31))
        self.iloscWSpinBox.setMaximum(1e+18)
        self.iloscWSpinBox.setObjectName("iloscWSpinBox")
        self.iloscWSpinBox.setFont(font)

        self.walutaKupowanaComboBox = QtWidgets.QComboBox(self.WymienWaluteFrame)
        self.walutaKupowanaComboBox.setGeometry(QtCore.QRect(180, 40, 141, 31))
        self.walutaKupowanaComboBox.setObjectName("walutaKupowanaComboBox")
        self.walutaKupowanaComboBox.addItems(connection.ReadTableOfCurrencies())
        self.walutaKupowanaComboBox.setFont(font)

        self.walutaZaComboBox = QtWidgets.QComboBox(self.WymienWaluteFrame)
        self.walutaZaComboBox.setGeometry(QtCore.QRect(180, 160, 141, 31))
        self.walutaZaComboBox.setObjectName("walutaZaComboBox")
        self.walutaZaComboBox.addItems(connection.ReadTableOfCurrencies())
        self.walutaZaComboBox.setFont(font)

        def wymien():
            amount = self.iloscWSpinBox.text().replace(",", ".")
            error = current_customer.exchange(self.walutaZaComboBox.currentText(),
                                              self.walutaKupowanaComboBox.currentText(), float(amount))
            if type(error) == int:
                msg = ErrorMessage()
                if error == error_codes.CONNECTION_TO_NBP_PROBLEM:
                    msg.setupUi(msg, "Problem z połączeniem do nbp")
                if error == error_codes.NOT_ENOUGH_CURRENCY:
                    msg.setupUi(msg, "Brak środków na wykonanie operacji")
                else:
                    msg.setupUi(msg, str(error))
                x = msg.exec_()

        self.wymienButton = QtWidgets.QPushButton(self.WymienWaluteFrame)
        self.wymienButton.clicked.connect(wymien)
        self.wymienButton.setGeometry(QtCore.QRect(110, 210, 131, 41))
        self.wymienButton.setObjectName("wymienButton")
        self.wymienButton.setText("Wymień")
        self.wymienButton.setFont(font)

        # setting text
        self.sprawdzStanButton.setText("Sprawdź stan portfela")
        self.kupWaluteButton.setText("Kup walutę")
        self.wymienWaluteButton.setText("Wymień walutę")
        self.stanPortfelaLabel.setText("Stan Portfela:")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("Kantor")

        def sprawdzKurs():
            self.SprawdzKursFrame.setVisible(True)
            self.DodajKlientaFrame.setVisible(False)
            self.SprawdzHistorieFrame.setVisible(False)
            self.sprawdzKursButton.setStyleSheet("background-color : #999")
            self.historiaKursuButton.setStyleSheet("background-color : #ccc")
            self.dodajKlientaButton.setStyleSheet("background-color : #ccc")
            self.sprawdzKursButton.setEnabled(False)
            self.historiaKursuButton.setEnabled(True)
            self.dodajKlientaButton.setEnabled(True)
            self.sprawdzHistorieImage.setVisible(False)
            self.dodajKlientaImage.setVisible(False)
            self.sprawdzKursImage.setVisible(True)

        self.sprawdzKursButton = QtWidgets.QPushButton(self.tab)
        self.sprawdzKursButton.clicked.connect(sprawdzKurs)
        self.sprawdzKursButton.setGeometry(QtCore.QRect(30, 50, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sprawdzKursButton.setFont(font)
        self.sprawdzKursButton.setObjectName("sprawdzKursButton")

        def historiaKursu():
            self.SprawdzHistorieFrame.setVisible(True)
            self.SprawdzKursFrame.setVisible(False)
            self.DodajKlientaFrame.setVisible(False)
            self.sprawdzKursButton.setStyleSheet("background-color : #ccc")
            self.historiaKursuButton.setStyleSheet("background-color : #999")
            self.dodajKlientaButton.setStyleSheet("background-color : #ccc")
            self.sprawdzKursButton.setEnabled(True)
            self.historiaKursuButton.setEnabled(False)
            self.dodajKlientaButton.setEnabled(True)
            self.sprawdzHistorieImage.setVisible(True)
            self.dodajKlientaImage.setVisible(False)
            self.sprawdzKursImage.setVisible(False)

        self.historiaKursuButton = QtWidgets.QPushButton(self.tab)
        self.historiaKursuButton.clicked.connect(historiaKursu)
        self.historiaKursuButton.setGeometry(QtCore.QRect(30, 200, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.historiaKursuButton.setFont(font)
        self.historiaKursuButton.setObjectName("historiaKursuButton")

        def dodajKlienta():
            self.SprawdzHistorieFrame.setVisible(False)
            self.DodajKlientaFrame.setVisible(True)
            self.SprawdzKursFrame.setVisible(False)
            self.sprawdzKursButton.setStyleSheet("background-color : #ccc")
            self.historiaKursuButton.setStyleSheet("background-color : #ccc")
            self.dodajKlientaButton.setStyleSheet("background-color : #999")
            self.sprawdzKursButton.setEnabled(True)
            self.historiaKursuButton.setEnabled(True)
            self.dodajKlientaButton.setEnabled(False)
            self.sprawdzHistorieImage.setVisible(False)
            self.dodajKlientaImage.setVisible(True)
            self.sprawdzKursImage.setVisible(False)

        self.dodajKlientaButton = QtWidgets.QPushButton(self.tab)
        self.dodajKlientaButton.clicked.connect(dodajKlienta)
        self.dodajKlientaButton.setGeometry(QtCore.QRect(30, 350, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dodajKlientaButton.setFont(font)
        self.dodajKlientaButton.setObjectName("dodajKlientaButton")

        self.SprawdzKursFrame = QtWidgets.QFrame(self.tab)
        self.SprawdzKursFrame.setGeometry(QtCore.QRect(310, 170, 441, 291))
        self.SprawdzKursFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SprawdzKursFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SprawdzKursFrame.setObjectName("SprawdzKursFrame")
        self.SprawdzKursFrame.setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(14)

        self.sprawdzKursImage = QtWidgets.QLabel(self.tab)
        self.sprawdzKursImage.setGeometry(QtCore.QRect(450, 30, 111, 111))
        self.sprawdzKursImage.setText("")
        self.sprawdzKursImage.setPixmap(QtGui.QPixmap("dolar.png"))
        self.sprawdzKursImage.setObjectName("sprawdzKursImage")
        self.sprawdzKursImage.setVisible(False)

        # Creating SprawdzKursFrame
        self.wejsciowaLabel = QtWidgets.QLabel(self.SprawdzKursFrame)
        self.wejsciowaLabel.setGeometry(QtCore.QRect(10, 35, 161, 20))
        self.wejsciowaLabel.setObjectName("wejsciowaLabel")
        self.wejsciowaLabel.setFont(font)

        self.wyjsciowaLabel = QtWidgets.QLabel(self.SprawdzKursFrame)
        self.wyjsciowaLabel.setGeometry(QtCore.QRect(10, 85, 191, 41))
        self.wyjsciowaLabel.setObjectName("wyjsciowaLabel")
        self.wyjsciowaLabel.setFont(font)

        self.wejsciowaCombo = QtWidgets.QComboBox(self.SprawdzKursFrame)
        self.wejsciowaCombo.setGeometry(QtCore.QRect(210, 30, 141, 31))
        self.wejsciowaCombo.setFont(font)
        self.wejsciowaCombo.setObjectName("wejsciowaCombo")
        self.wejsciowaCombo.addItems(connection.ReadTableOfCurrencies())

        self.wyjsciowaCombo = QtWidgets.QComboBox(self.SprawdzKursFrame)
        self.wyjsciowaCombo.setGeometry(QtCore.QRect(210, 90, 141, 31))
        self.wyjsciowaCombo.setObjectName("wyjsciowaCombo")
        self.wyjsciowaCombo.addItems(connection.ReadTableOfCurrencies())
        self.wyjsciowaCombo.setFont(font)

        self.kursLabel = QtWidgets.QLabel(self.SprawdzKursFrame)
        self.kursLabel.setGeometry(QtCore.QRect(120, 220, 71, 21))
        self.kursLabel.setObjectName("kursLabel")
        self.kursLabel.setFont(font)

        self.wynikKursLabel = QtWidgets.QLabel(self.SprawdzKursFrame)
        self.wynikKursLabel.setGeometry(QtCore.QRect(220, 220, 101, 21))
        self.wynikKursLabel.setObjectName("wynikKursLabel")
        self.wynikKursLabel.setFont(font)

        def podajKurs():
            kurs = connection.getRate(self.wejsciowaCombo.currentText(), self.wyjsciowaCombo.currentText())
            if kurs == error_codes.CONNECTION_TO_NBP_PROBLEM:
                msg = ErrorMessage()
                msg.setupUi(msg, "Problem z połączeniem do nbp")
                x = msg.exec_()
                return
            kurs = round(kurs, 4)
            self.wynikKursLabel.setText(str(kurs))

        self.podajKursButton = QtWidgets.QPushButton(self.SprawdzKursFrame)
        self.podajKursButton.clicked.connect(podajKurs)
        self.podajKursButton.setGeometry(QtCore.QRect(120, 140, 151, 51))
        self.podajKursButton.setObjectName("podajKursButton")
        self.podajKursButton.setText("Podaj kurs")
        self.podajKursButton.setFont(font)
        # End of Creating SprawdzKursyFrame

        self.DodajKlientaFrame = QtWidgets.QFrame(self.tab)
        self.DodajKlientaFrame.setGeometry(QtCore.QRect(335, 140, 341, 261))
        self.DodajKlientaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DodajKlientaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DodajKlientaFrame.setObjectName("DodajKlientaFrame")
        self.DodajKlientaFrame.setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(14)

        self.dodajKlientaImage = QtWidgets.QLabel(self.tab)
        self.dodajKlientaImage.setGeometry(QtCore.QRect(450, 30, 111, 111))
        self.dodajKlientaImage.setText("")
        self.dodajKlientaImage.setPixmap(QtGui.QPixmap("account.png"))
        self.dodajKlientaImage.setObjectName("dodajKlientaImage")
        self.dodajKlientaImage.setVisible(False)

        # Creating DodajKlientaFrame
        self.wprowImieLabel = QtWidgets.QLabel(self.DodajKlientaFrame)
        self.wprowImieLabel.setGeometry(QtCore.QRect(10, 60, 141, 31))
        self.wprowImieLabel.setFont(font)
        self.wprowImieLabel.setObjectName("wprowImieLabel")

        self.wprowImieLine = QtWidgets.QLineEdit(self.DodajKlientaFrame)
        self.wprowImieLine.setGeometry(QtCore.QRect(160, 55, 171, 41))
        self.wprowImieLine.setFont(font)
        self.wprowImieLine.setObjectName("wprowImieLine")

        def stworzKonto():
            tab_temp = Tab()
            tab_temp.setupUi(tab_temp, self.wprowImieLine.text())
            self.tabWidget.addTab(tab_temp, self.wprowImieLine.text())

        self.stworzKontoButton = QtWidgets.QPushButton(self.DodajKlientaFrame)
        self.stworzKontoButton.clicked.connect(stworzKonto)
        self.stworzKontoButton.setGeometry(QtCore.QRect(80, 120, 151, 51))
        self.stworzKontoButton.setObjectName("stworzKontoButton")
        self.stworzKontoButton.setFont(font)
        # End of creating DodajKlientaFrame

        self.SprawdzHistorieFrame = QtWidgets.QFrame(self.tab)
        self.SprawdzHistorieFrame.setGeometry(QtCore.QRect(310, 170, 441, 291))
        self.SprawdzHistorieFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SprawdzHistorieFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SprawdzHistorieFrame.setObjectName("SprawdzHistorieFrame")
        self.SprawdzHistorieFrame.setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(14)

        self.sprawdzHistorieImage = QtWidgets.QLabel(self.tab)
        self.sprawdzHistorieImage.setGeometry(QtCore.QRect(450, 30, 111, 111))
        self.sprawdzHistorieImage.setText("")
        self.sprawdzHistorieImage.setPixmap(QtGui.QPixmap("plot.png"))
        self.sprawdzHistorieImage.setObjectName("sprawdzHistorieImage")
        self.sprawdzHistorieImage.setVisible(False)

        # Creating SprawdzHistorieFrame
        self.cenaWalutyLabel = QtWidgets.QLabel(self.SprawdzHistorieFrame)
        self.cenaWalutyLabel.setGeometry(QtCore.QRect(10, 35, 121, 20))
        self.cenaWalutyLabel.setObjectName("cenaWalutyLabel")
        self.cenaWalutyLabel.setFont(font)

        self.podawanaWLabel = QtWidgets.QLabel(self.SprawdzHistorieFrame)
        self.podawanaWLabel.setGeometry(QtCore.QRect(10, 85, 191, 41))
        self.podawanaWLabel.setObjectName("podawanaWLabel")
        self.podawanaWLabel.setFont(font)

        self.liczbaDniLabel = QtWidgets.QLabel(self.SprawdzHistorieFrame)
        self.liczbaDniLabel.setGeometry(QtCore.QRect(10, 155, 181, 20))
        self.liczbaDniLabel.setObjectName("liczbaDniLabel")
        self.liczbaDniLabel.setFont(font)

        self.cenaWalutyComboBox = QtWidgets.QComboBox(self.SprawdzHistorieFrame)
        self.cenaWalutyComboBox.setGeometry(QtCore.QRect(210, 30, 141, 31))
        self.cenaWalutyComboBox.setObjectName("cenaWalutyComboBox")
        self.cenaWalutyComboBox.addItems(connection.ReadTableOfCurrencies())
        self.cenaWalutyComboBox.setFont(font)

        self.podawanaWComboBox = QtWidgets.QComboBox(self.SprawdzHistorieFrame)
        self.podawanaWComboBox.setGeometry(QtCore.QRect(210, 90, 141, 31))
        self.podawanaWComboBox.setObjectName("podawanaWComboBox")
        self.podawanaWComboBox.addItems(connection.ReadTableOfCurrencies())
        self.podawanaWComboBox.setFont(font)

        self.liczbaDniSpinBox = QtWidgets.QSpinBox(self.SprawdzHistorieFrame)
        self.liczbaDniSpinBox.setGeometry(QtCore.QRect(210, 150, 141, 31))
        self.liczbaDniSpinBox.setMaximum(254)
        self.liczbaDniSpinBox.setMinimum(2)
        self.liczbaDniSpinBox.setObjectName("liczbaDniSpinBox")
        self.liczbaDniSpinBox.setFont(font)

        def generuj():
            error = diagrams.drawDiagram(self.cenaWalutyComboBox.currentText(), self.podawanaWComboBox.currentText(),
                                         self.liczbaDniSpinBox.value())
            if error == error_codes.CONNECTION_TO_NBP_PROBLEM:
                msg = ErrorMessage()
                msg.setupUi(msg, "Problem z połączeniem do nbp")
                x = msg.exec_()
            if error == error_codes.DATES_DONT_MATCH:
                msg = ErrorMessage()
                msg.setupUi(msg, "Nieaktualne dane")
                x = msg.exec_()

        self.generujWykresButton = QtWidgets.QPushButton(self.SprawdzHistorieFrame)
        self.generujWykresButton.clicked.connect(generuj)
        self.generujWykresButton.setGeometry(QtCore.QRect(120, 210, 151, 51))
        self.generujWykresButton.setObjectName("generujWykresButton")
        self.generujWykresButton.setFont(font)

        self.tabWidget.addTab(self.tab, "Kantor")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sprawdzKursButton.setText(_translate("MainWindow", "Sprawdź kurs"))
        self.historiaKursuButton.setText(_translate("MainWindow", "Sprawdź historie kursu"))
        self.dodajKlientaButton.setText(_translate("MainWindow", "Dodaj klienta"))
        self.wejsciowaLabel.setText(_translate("MainWindow", "Waluta wejściowa:"))
        self.wyjsciowaLabel.setText(_translate("MainWindow", "Waluta wyjściowa:"))
        self.kursLabel.setText(_translate("MainWindow", "Kurs:"))
        self.wynikKursLabel.setText(_translate("MainWindow", "0,0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Kantor"))
        self.wprowImieLabel.setText(_translate("MainWindow", "Wprowadź imię: "))
        self.stworzKontoButton.setText(_translate("MainWindow", "Stwórz konto"))
        self.cenaWalutyLabel.setText(_translate("MainWindow", "Cana waluty:"))
        self.podawanaWLabel.setText(_translate("MainWindow", "Podawana w walucie:"))
        self.liczbaDniLabel.setText(_translate("MainWindow", "Liczba dni:"))
        self.generujWykresButton.setText(_translate("MainWindow", "Generuj wykres"))

