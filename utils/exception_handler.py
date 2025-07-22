from utils.AppiumUtils import AppiumUtils as AU
from functools import wraps

def handle_exceptions(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            AU.save_screenshot(f"{func.__name__}失败")
            print(f"{func.__name__}异常: {e}")
            raise
    return wrapper
