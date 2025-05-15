def process_data(data, config):
    """Process data according to provided configuration."""
    result = data.copy()

    # Apply filters if specified
    if 'filters' in config:
        for filter_config in config['filters']:
            field = filter_config['field']
            value = filter_config['value']
            operator = filter_config.get('operator', '==')

            if operator == '==':
                result = [item for item in result if item.get(field) == value]
            elif operator == '!=':
                result = [item for item in result if item.get(field) != value]
            elif operator == '>':
                result = [item for item in result if item.get(field, 0) > value]
            elif operator == '<':
                result = [item for item in result if item.get(field, 0) < value]

    # Apply transformations if specified
    if 'transformations' in config:
        for transform in config['transformations']:
            field = transform['field']
            operation = transform['operation']

            if operation == 'uppercase':
                for item in result:
                    if field in item and isinstance(item[field], str):
                        item[field] = item[field].upper()
            elif operation == 'lowercase':
                for item in result:
                    if field in item and isinstance(item[field], str):
                        item[field] = item[field].lower()
            elif operation == 'round' and 'precision' in transform:
                precision = transform['precision']
                for item in result:
                    if field in item and isinstance(item[field], (int, float)):
                        item[field] = round(item[field], precision)

    return result


def display_table(data):
    """Display the processed data in a manual tabular format."""
    if not data:
        print("No data to display.")
        return

    # Get the headers (column names)
    headers = data[0].keys()
    headers_str = " | ".join([str(header).ljust(15) for header in headers])
    print(headers_str)
    print("-" * len(headers_str))  # Line separator

    # Display each row of data
    for item in data:
        row_str = " | ".join([str(value).ljust(15) for value in item.values()])
        print(row_str)


# Sample data
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 2, "name": "Desk Chair", "category": "Furniture", "price": 189.50},
    {"id": 3, "name": "Coffee Maker", "category": "Appliances", "price": 49.99},
    {"id": 4, "name": "Tablet", "category": "Electronics", "price": 299.99},
    {"id": 5, "name": "Bookshelf", "category": "Furniture", "price": 149.75}
]

# Configuration for electronics products
electronics_config = {
    "filters": [
        {"field": "category", "value": "Electronics"}
    ],
    "transformations": [
        {"field": "name", "operation": "uppercase"},
        {"field": "price", "operation": "round", "precision": 0}
    ]
}

# Process the data
electronics = process_data(products, electronics_config)
print("Electronics Products:")
display_table(electronics)

# Different configuration for furniture under $150
furniture_config = {
    "filters": [
        {"field": "category", "value": "Furniture"},
        {"field": "price", "value": 150, "operator": "<"}
    ]
}

affordable_furniture = process_data(products, furniture_config)
print("\nAffordable Furniture Products under $150:")
display_table(affordable_furniture)
