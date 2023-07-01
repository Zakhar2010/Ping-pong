import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox

class CurrencyConverter(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Конвертер валют")
        self.setGeometry(100, 100, 500, 210)

        self.amount_label = QLabel("Сума:", self)
        self.amount_label.move(50, 30)
        self.amount_entry = QLineEdit(self)
        self.amount_entry.setGeometry(110, 30, 150, 20)

        self.from_label = QLabel("З:", self)
        self.from_label.move(50, 70)
        self.from_entry = QLineEdit(self)
        self.from_entry.setGeometry(110, 70, 150, 20)

        self.to_label = QLabel("У:", self)
        self.to_label.move(50, 110)
        self.to_entry = QLineEdit(self)
        self.to_entry.setGeometry(110, 110, 150, 20)

        self.convert_button = QPushButton("Конвертувати", self)
        self.convert_button.setGeometry(110, 150, 150, 30)
        self.convert_button.clicked.connect(self.convert_currency)

        self.USD_button = QPushButton("USD",self)
        self.USD_button.setGeometry(350, 25, 100, 30)
        #тут має бути функція кнопки
 
        self.EUR_button = QPushButton("EUR",self)
        self.EUR_button.setGeometry(350, 65, 100, 30)
        #тут має бути функція кнопки

        self.UAH_button = QPushButton("USD",self)
        self.UAH_button.setGeometry(350, 105, 100, 30)
        #тут має бути функція кнопки

    def convert_currency(self):
        amount = float(self.amount_entry.text())
        from_currency = self.from_entry.text().upper()
        to_currency = self.to_entry.text().upper()

        # Фіктивний курс валют для демонстрації
        exchange_rates = {
            "USD": {"EUR": 0.85, "UAH": 26.0},
            "EUR": {"USD": 1.18, "UAH": 30.0},
            "UAH": {"USD": 0.038, "EUR": 0.033}
        }

        try:
            result = amount * exchange_rates[from_currency][to_currency]
            QMessageBox.information(self, "Результат", f"Результат: {result:.2f}")
        except KeyError:
            QMessageBox.critical(self, "Помилка", "Невірно введена валюта.")
        except:
            QMessageBox.critical(self, "Помилка", "Не вдалося виконати конвертацію.")

    def USD_paste(self,):
        self.from_entry.text("USD")

    def EUR_paste(self,):
        self.from_entry.text("EUR")

    def UAH_paste(self,):
        self.from_entry.text("UAH")
        

if name == 'main':
    app = QApplication(sys.argv)
    converter = CurrencyConverter()
    converter.show()
    sys.exit(app.exec_())
