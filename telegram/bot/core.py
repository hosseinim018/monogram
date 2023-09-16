def validate_payload(locals):
    _locals = locals  # Create a copy of locals()
    _locals.pop('cls')  # Remove the key cls from _locals
    payload = {k: v for k, v in _locals.items() if v}  # Remove None values from payload
    return payload