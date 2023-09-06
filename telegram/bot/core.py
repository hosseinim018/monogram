def validate_parameters(func):
    def wrapper(*args, **kwargs):
        payload = {k: v for k, v in kwargs.items() if v is not None}
        # Call the original function and pass the payload
        return func(*args, payload=payload, **kwargs)

    return wrapper