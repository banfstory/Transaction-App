from PyQt5 import QtWidgets

class PopulateTable:
    # populate table by setting columns and rows in the table
    def populate_table(self):
        self.setTransactionColumns()
        self.setTransactionRows()

    # set headers for the table
    def setTransactionColumns(self):
        self.transactions_list.setColumnCount(len(self.transactions_headers))
        self.transactions_list.setHorizontalHeaderLabels(self.transactions_headers)

    # get all transactions and set them into table
    def setTransactionRows(self):
        self.transactions_list.setRowCount(len(self.transactions_current))
        for row, transaction in enumerate(self.transactions_current):
            for index, header in enumerate(self.transactions_headers):
                self.transactions_list.setItem(row, index, QtWidgets.QTableWidgetItem(transaction[header]))