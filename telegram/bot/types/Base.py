def valid_params(locals):
    return {param_name: parama_val for param_name, parama_val in locals.items() if parama_val is not None and param_name !='self'}
class test():
    # @validate_parameters
    def __init__(self, param1, param2, param3=None, param4=None):
        payload = valid_params(locals())
        # payload = {param_name: parama_val for param_name, parama_val in locals().items() if parama_val is not None and param_name !='self'}
        # for param_name, parama_val in locals().items():
        #     print(param_name)
        #     if parama_val is not None and param_name !='self':
        #         payload[param_name] = parama_val
        print(payload)
# t = test('p1','p2', param3='p3')
