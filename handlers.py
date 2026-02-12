import types
import inspect

"""
Handler management module for Telegram bots.
This module includes the BotHandlerManager class, which is responsible for registering and managing handlers.
"""

class BotHandlerManager:
    """
    Base class for managing handlers in a bot.
    This class is responsible for registering and managing all handlers.
    """
    
    @staticmethod
    def _handler_factory(registry_name):
        """
        A factory for creating registration decorators, defined as a static method
        to be accessible as a class attribute.
        """
        def decorator_wrapper(*args, **kwargs):
            def decorator(func):
                # ثبت متادیتا روی خود تابع (func) در زمان تعریف کلاس
                if not hasattr(func, '_handler_info'):
                    func._handler_info = []
                func._handler_info.append({'registry': registry_name, 'args': args, 'kwargs': kwargs})
                return func
            return decorator
        return decorator_wrapper

    # تعریف دکوریتورها به عنوان ویژگی‌های کلاس (Class Attributes)
    # این کار آن‌ها را در زمان تعریف کلاس فرزند قابل دسترسی می‌سازد.
    on_message = _handler_factory('message')
    on_callback = _handler_factory('callback')
    on_stage = _handler_factory('stage')
    on_inline_query = _handler_factory('inline_query')

    def __init__(self):
        self.message_handlers = {}
        self.callback_handlers = {}
        self.stage_handlers = {}
        self.inline_query_handlers = {}

    def _register_handlers(self):
        """
        This method iterates through all methods of the class, finds decorated ones,
        and registers them in the appropriate dictionaries.
        """
        for attr_name in dir(self):
            # نادیده گرفتن متدهای سیستمی (Dunder methods) برای جلوگیری از خطای 'method-wrapper'
            if attr_name.startswith('__'):
                continue
            
            try:
                method = getattr(self, attr_name)
            except AttributeError:
                # در صورت خطای دسترسی به ویژگی، ادامه نده
                continue

            # اطمینان از اینکه شیء یک متد نمونه قابل فراخوانی است.
            if not isinstance(method, types.MethodType):
                continue
                
            # دریافت تابع اصلی (unbound function) برای دسترسی به متادیتا
            func = method.__func__
            
            # بررسی متادیتا ثبت هندلر
            if hasattr(func, '_handler_info'):
                for info in func._handler_info:
                    registry = info['registry']
                    args = info['args']
                    kwargs = info['kwargs']
                    
                    if registry == 'message':
                        # در اینجا args[0] متن فرمان یا پیام است
                        if args:
                            text = args[0]
                            # ثبت متد (Bound Method) برای حفظ دسترسی به 'self'
                            self.message_handlers[text] = method 
                    
                    elif registry == 'stage':
                        if args:
                            stage = args[0]
                            self.stage_handlers[stage] = ('exact', method)
                        elif 'startswith' in kwargs:
                            key = kwargs['startswith']
                            self.stage_handlers[key] = ('startswith', method)
                    
                    elif registry == 'inline_query':
                        self.inline_query_handlers['handler'] = method
                    
                    elif registry == 'callback':
                        if 'data' in kwargs:
                            key = kwargs['data']
                            self.callback_handlers[key] = ('exact', method)
                        elif 'startswith' in kwargs:
                            key = kwargs['startswith']
                            self.callback_handlers[key] = ('startswith', method)
                            
    def handle_message(self, message, user):
        """ Handles incoming messages. """
        text = message.get('text', '')
        handler = self.message_handlers.get(text)
        
        if handler:
            print(f"-> Handler found for message: '{text}'. Executing...")
            handler(message, user) 
            return True
        
        print(f"-> No specific handler found for message: '{text}'.")
        self.unknown_message(message, user)
        return False

    def handle_callback_query(self, callback_query, user):
        data = callback_query.data
        handler_info = self.callback_handlers.get(data)
        if handler_info and handler_info[0] == 'exact':
            handler_info[1](callback_query, user)
            return
        for prefix, (match_type, handler) in self.callback_handlers.items():
            if match_type == 'startswith' and data.startswith(prefix):
                handler(callback_query, user)
                return
        self.unknown_action(callback_query)
        
    def handle_inline_query(self, inline_query):
        if 'handler' in self.inline_query_handlers:
            self.inline_query_handlers['handler'](inline_query)

    def unknown_message(self, message, user):
        """ Default method for unknown messages. """
        print(f"-> Unknown message received: {message.get('text', 'N/A')}")
        pass
    
    def unknown_action(self, callback_query):
        """ Default method for unknown actions. """
        pass

