def group_category(current, default):
    temp_transactions = dict()
    for transaction in default:
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
        current.append({ 'Category': key, 'Debit': str(value['Debit']), 'Credit': str(value['Credit']) })

def group_date_year(current, default):
    temp_transactions = dict()
    for transaction in default:
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
        current.append({ 'Date': key, 'Debit': str(value['Debit']), 'Credit': str(value['Credit']) })

def group_debit_credit(current, default):
    temp_transactions = { 'Debit': 0, 'Credit': 0 }
    for transaction in default:
        # add debit or credit property value
        if transaction['Debit']:
            temp_transactions['Debit'] += float(transaction['Debit'])
        if transaction['Credit']:
            temp_transactions['Credit'] += float(transaction['Credit'])
    # append this to array so it can be populated into the table
    for key, value in temp_transactions.items():
        value = round(value, 2)
        current.append({ 'Debit/Credit': key, 'Amount': str(value)})