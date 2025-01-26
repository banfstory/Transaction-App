from tables import group_date_year
from ..populate_table import PopulateTable
import matplotlib.pyplot as plt
import numpy

class GroupDateYear(PopulateTable):
    def __init__(self, transactions_list, default, combo, button):
        self.transactions_headers = ['Date', 'Debit', 'Credit']
        self.graph_items = ['Multiple Bar Graph', 'Multiple Line Graph', 'Line Graph (Debit)', 'Line Graph (Credit)']
        self.transactions_list = transactions_list
        self.transactions_default = default
        self.transactions_current = list()
        self.graph_combo = combo
        self.graph_btn = button
        self.group_date_year()
        self.initalize_graph_combo()
        self.graph_btn.clicked.connect(self.display_graph)

    def initalize_graph_combo(self):
        self.graph_combo.clear()
        for name in self.graph_items:
            self.graph_combo.addItem(name)

    def display_graph(self):
        index = self.graph_combo.currentIndex()
        if index == 0: self.multiple_bar_graph()
        elif index == 1: self.multiple_line_graph()
        elif index == 2: self.plot_line_graph('Debit')
        elif index == 3: self.plot_line_graph('Credit')

    def group_date_year(self):
        temp_transactions = dict()
        for transaction in self.transactions_default:
            year = transaction['Date'].split("/")[2]
            # if year doesnt exist yet then create a new category property
            if year not in temp_transactions:
                temp_transactions[year] = {}
                temp_transactions[year]['Debit'] = 0
                temp_transactions[year]['Credit'] = 0
            curr = temp_transactions[year]
            # add debit or credit property value
            if transaction['Debit']:
                curr['Debit'] += float(transaction['Debit'])
            if transaction['Credit']:
                curr['Credit'] += float(transaction['Credit'])
        # append this to array so it can be populated into the table
        for key, value in temp_transactions.items():
            value['Debit'] = round(value['Debit'], 2)
            value['Credit'] = round(value['Credit'], 2)
            self.transactions_current.append({ 'Date': key, 'Debit': str(value['Debit']), 'Credit': str(value['Credit']) })
        self.populate_table()

    def multiple_bar_graph(self):
        w = 0.4
        year = []
        debit = []
        credit = []
        for i in range(len(self.transactions_current) - 1, -1, -1):
            year.append(self.transactions_current[i]['Date'])
            debit.append(float(self.transactions_current[i]['Debit']))
            credit.append(float(self.transactions_current[i]['Credit']))
        values = numpy.arange(len(year))
        plt.bar(values, debit, w, label='Debit')
        plt.bar(values+w, credit, w, label='Credit')
        plt.xticks(values, year)
        plt.title('Year Debit/Credit')
        plt.legend()
        plt.show()

    def multiple_line_graph(self):
        year = []
        debit = []
        credit = []
        for i in range(len(self.transactions_current) - 1, -1, -1):
            year.append(self.transactions_current[i]['Date'])
            debit.append(float(self.transactions_current[i]['Debit']))
            credit.append(float(self.transactions_current[i]['Credit']))
        plt.plot_date(year, debit, linestyle='solid', label="Debit")
        plt.plot_date(year, credit, linestyle='solid', label="Credit")
        plt.title('Year Debit/Credit')
        plt.legend()
        plt.show()

    def plot_line_graph(self, type):
        year = []
        result = []
        for i in range(len(self.transactions_current) - 1, -1, -1):
            result.append(float(self.transactions_current[i][type]))
            year.append(self.transactions_current[i]['Date'])
        plt.plot_date(year, result, linestyle='solid', label=type)
        plt.title(f'Year {type}')
        plt.legend()
        plt.show()

