from ..populate_table import PopulateTable
import matplotlib.pyplot as plt
from datetime import datetime

class ShowAll(PopulateTable):
    def __init__(self, transactions_list, default, combo, button):
        self.transactions_headers = ['Date', 'Description', 'Debit', 'Credit', 'Balance', 'Category']
        self.graph_items = ['Multiple Line Graph', 'Line Graph (Balance)', 'Line Graph (Debit)', 'Line Graph (Credit)']
        self.transactions_list = transactions_list
        self.transactions_default = default
        self.transactions_current = default.copy()
        self.graph_combo = combo
        self.graph_btn = button
        self.show_all()
        self.initalize_graph_combo()
        self.graph_btn.clicked.connect(self.display_graph)

    def initalize_graph_combo(self):
        self.graph_combo.clear()
        for name in self.graph_items:
            self.graph_combo.addItem(name)
    
    def display_graph(self):
        index = self.graph_combo.currentIndex()
        if index == 0: self.multiple_line_graph()
        elif index == 1: self.plot_line_graph('Balance')
        elif index == 2: self.plot_line_graph('Debit')
        elif index == 3: self.plot_line_graph('Credit')

    def show_all(self):
        self.populate_table()

    def multiple_line_graph(self):
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
        plt.title('Date Balance/Debit/Credit')
        plt.show()

    def plot_line_graph(self, type):
        format = '%d/%m/%Y'
        date = []
        result = []
        for transaction in self.transactions_current:
            if not transaction[type]:
                continue
            result.append(float(transaction[type]))
            date.append(datetime.strptime(transaction['Date'], format))
        plt.plot_date(date, result, linestyle='solid', label=type)
        plt.legend()
        plt.title(f'Date {type}')
        plt.show()
        