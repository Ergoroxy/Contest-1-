def kwargsAcceptFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    # Returns the inputs as a dictionary  
    return kwargs
