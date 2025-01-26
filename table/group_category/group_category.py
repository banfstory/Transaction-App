from tables import group_category
from ..populate_table import PopulateTable
import matplotlib.pyplot as plt
import numpy

class GroupCategory(PopulateTable):
    def __init__(self, transactions_list, default, combo, button):
        self.transactions_headers = ['Category', 'Debit', 'Credit']
        self.graph_items = ['Multiple Bar Graph', 'Line Graph (Debit)', 'Line Graph (Credit)']
        self.transactions_list = transactions_list
        self.transactions_default = default
        self.transactions_current = list()
        self.graph_combo = combo
        self.graph_btn = button
        self.group_category()
        self.initalize_graph_combo()
        self.graph_btn.clicked.connect(self.display_graph)

    def initalize_graph_combo(self):
        self.graph_combo.clear()
        for name in self.graph_items:
            self.graph_combo.addItem(name)
    
    def display_graph(self):
        index = self.graph_combo.currentIndex()
        if index == 0: self.multiple_bar_graph()
        elif index == 1: self.line_graph_debit()
        elif index == 2: self.line_graph_credit()

    def group_category(self):
        temp_transactions = dict()
        for transaction in self.transactions_default:
            # if category doesnt exist yet then create a new category property
            if transaction['Category'] not in temp_transactions:
                temp_transactions[transaction['Category']] = {}
                temp_transactions[transaction['Category']]['Debit'] = 0
                temp_transactions[transaction['Category']]['Credit'] = 0
            curr = temp_transactions[transaction['Category']]
            # add debit or credit property value
            if transaction['Debit']:
                curr['Debit'] += float(transaction['Debit'])
            if transaction['Credit']:
                curr['Credit'] += float(transaction['Credit'])
        # append this to array so it can be populated into the table
        for key, value in temp_transactions.items():
            value['Debit'] = round(value['Debit'], 2)
            value['Credit'] = round(value['Credit'], 2)
            self.transactions_current.append({ 'Category': key, 'Debit': str(value['Debit']), 'Credit': str(value['Credit']) })
        self.populate_table()

    def multiple_bar_graph(self):
        w = 0.4
        category = []
        debit = []
        credit = []
        for transaction in self.transactions_current:
            category.append(transaction['Category'])
            debit.append(transaction['Debit'])
            credit.append(transaction['Credit'])
        values = numpy.arange(len(category))
        plt.bar(values, debit, w, label='Debit')
        plt.bar(values+w, credit, w, label='Credit')
        plt.xticks(values, category)
        plt.title('Category Debit/Credit')
        plt.legend()
        plt.show()

    def line_graph_debit(self):
        for transaction in self.transactions_current:
            slices = []
            labels = []
            for transaction in self.transactions_current:
                labels.append(transaction['Category'])
                slices.append(float(transaction['Debit']))
        plt.pie(slices, labels=labels)
        plt.title("Category Debit Breakdown")
        plt.legend()
        plt.show()

    def line_graph_credit(self):
        for transaction in self.transactions_current:
            slices = []
            labels = []
            for transaction in self.transactions_current:
                labels.append(transaction['Category'])
                slices.append(float(transaction['Credit']))
        plt.pie(slices, labels=labels)
        plt.title("Category Credit Breakdown")
        plt.legend()
        plt.show()