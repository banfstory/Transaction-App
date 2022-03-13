from ..populate_table import PopulateTable
import matplotlib.pyplot as plt

class GroupDebitCredit(PopulateTable):
    def __init__(self, transactions_list, default, combo, button):
        self.transactions_headers = ['Debit/Credit', 'Amount']
        self.graph_items = ['Bar Graph', 'Pie Graph']
        self.transactions_list = transactions_list
        self.transactions_default = default
        self.transactions_current = list()
        self.graph_combo = combo
        self.graph_btn = button
        self.group_debit_credit()
        self.initalize_graph_combo()
        self.graph_btn.clicked.connect(self.display_graph)

    def initalize_graph_combo(self):
        self.graph_combo.clear()
        for name in self.graph_items:
            self.graph_combo.addItem(name)

    def display_graph(self):
        index = self.graph_combo.currentIndex()
        if index == 0: self.bar_graph()
        elif index == 1: self.pie_graph()

    def group_debit_credit(self):
        temp_transactions = { 'Debit': 0, 'Credit': 0 }
        for transaction in self.transactions_default:
            # add debit or credit property value
            if transaction['Debit']:
                temp_transactions['Debit'] += float(transaction['Debit'])
            if transaction['Credit']:
                temp_transactions['Credit'] += float(transaction['Credit'])
        # append this to array so it can be populated into the table
        for key, value in temp_transactions.items():
            value = round(value, 2)
            self.transactions_current.append({ 'Debit/Credit': key, 'Amount': str(value)})
        self.populate_table()

    def bar_graph(self):
        labels = []
        values = []
        for transaction in self.transactions_current:
            labels.append(transaction['Debit/Credit'])
            values.append(float(transaction['Amount']))
        plt.bar(labels, values)
        plt.xlabel('Debit/Credit')
        plt.ylabel('Amount')
        plt.title('Debit vs Credit')
        plt.show()
    
    def pie_graph(self):
        slices = []
        labels = []
        for transaction in self.transactions_current:
            labels.append(transaction['Debit/Credit'])
            slices.append(float(transaction['Amount']))
        plt.pie(slices, labels=labels)
        plt.title("Debit vs Credit")
        plt.legend()
        plt.show()
