from datetime import datetime
from MainUI import Ui_MainWindow
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
from table.show_all.show_all import ShowAll
from table.group_category.group_category import GroupCategory
from table.group_date_year.group_date_year import GroupDateYear
from table.group_debit_credit.group_debit_credit import GroupDebitCredit
import csv
import re

class App(Ui_MainWindow):
    def __init__(self):
        self.table = None
        self.transactions_default = list()

    def initalization(self):
        self.browse_btn.clicked.connect(self.browse_file)
        self.show_combo.currentIndexChanged.connect(self.display_results)
        #self.graph_btn.clicked.connect(self.display_graph)

    # this will read the file with the path from your computer and read the .csv file and stores it into an array
    def browse_file(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(None, 'Select .csv file', '', 'Excel (*.csv *.xls )')[0]
        if file_name:
            self.currentFileLabel.setText(file_name)
            self.currentFileLabel.setToolTip(file_name)
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                reg = r"\s  +"
                self.transactions_default = list()
                for transaction in csv_reader:
                    transaction['Description'] = re.sub(reg, ' ', transaction['Description'].strip())
                    self.transactions_default.append(transaction)
                self.display_results(self.show_combo.currentIndex())
    
    def display_graph(self):
        index = self.graph_combo.currentIndex()
        if index == 0: self.line_graph()
        elif index == 1: self.bar_graph()
        elif index == 2: self.pie_graph() 
    
    # display results based on the selected item in the combo box
    def display_results(self, index):
        if index == 0: self.table = ShowAll(self.transactions_list, self.transactions_default, self.graph_combo, self.graph_btn)
        elif index == 1: self.table = GroupCategory(self.transactions_list, self.transactions_default, self.graph_combo, self.graph_btn)
        elif index == 2: self.table = GroupDateYear(self.transactions_list, self.transactions_default, self.graph_combo, self.graph_btn)
        else: self.table = GroupDebitCredit(self.transactions_list, self.transactions_default, self.graph_combo, self.graph_btn)

    def line_graph(self):
        format = '%d/%m/%Y'
        balance_date = []
        balance = []
        credit_date = []
        credit = []
        debit_date = []
        debit = []
        for transaction in self.transactions_current:
            balance_date.append(datetime.strptime(transaction['Date'], format))
            balance.append(float(transaction['Balance']))
            if transaction['Credit']:
                credit_date.append(datetime.strptime(transaction['Date'], format))
                credit.append(float(transaction['Credit']))
            if transaction['Debit']:
                debit_date.append(datetime.strptime(transaction['Date'], format))
                debit.append(float(transaction['Debit']))
        plt.plot_date(balance_date, balance, linestyle='solid', label="Balance")
        plt.plot_date(credit_date, credit, linestyle='solid', label="Credit")
        plt.plot_date(debit_date, debit, linestyle='solid', label="Debit")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App()
    ui.setupUi(MainWindow)
    ui.initalization()
    MainWindow.show()
    sys.exit(app.exec_())