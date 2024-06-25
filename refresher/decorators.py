import functools

user = {"username": "admin", "password": "<PASSWORD>", "access_level": "guest"}


def get_admin_password():
    return "1234"


def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function

def make_secure_with_param(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No admin permissions for {user['username']}"

        return secure_function
    return decorator


get_admin_password = make_secure(get_admin_password)

print(get_admin_password())


@make_secure
def better_get_admin_password():
    return "1234"

@make_secure_with_param("admin")
def even_better_get_admin_password():
    return "ADMIN"

@make_secure_with_param("guest")
def do_something():
    return "HI"


@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(better_get_admin_password("billing"))

print(get_admin_password.__name__)
print(do_something())

user = {"username": "admin", "password": "<PASSWORD>", "access_level": "admin"}
print(get_password("billing"))
print(even_better_get_admin_password())
