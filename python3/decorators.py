from functools import wraps
"""
def my_dec(func):
    @wraps(func)
    def wrapper():
        print("*****************")
        result = func()     # call original function
        print("*****************")
        return result        # return the original result
    return wrapper

@my_dec
def greet():
    print("Hello from Python")

greet()
"""
def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role!= "admin":
            print("Access denied!")
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea(role):
     print("Access grnated to tea")

access_tea("admin")
access_tea("user")