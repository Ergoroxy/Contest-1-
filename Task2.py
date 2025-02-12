def typeBasedTransformer(**kwargs):
    Output = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):   # Makes a square 
            Output[key] = value ** 2
        elif isinstance(value, str):
            Output[key] = value[::-1]  # Reverses string
        elif isinstance(value, bool):
            Output[key] = not value    # Invert the value
        elif isinstance(value, (list, tuple)):
            Output[key] = value[::-1]  # Reverses numbers 
        elif isinstance(value, dict):
            if len(set(value.values())) == len(value.values()):  # Ensure unique values
                Output[key] = {v: k for k, v in value.items()}
            else:
                Output[key] = value  # Leave unchanged if values are not unique
        else:
            Output[key] = value  # Unsupported types remain unchanged
    return Output
