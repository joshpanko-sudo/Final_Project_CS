def calculate_metrics(base_value):
    # Calculate new data
    result_tax = base_value * 0.15
    result_total = base_value + result_tax
    
    # Return the values back to whoever called the function
    return result_tax, result_total
