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


get_admin_password = make_secure(get_admin_password)

print(get_admin_password())


@make_secure
def better_get_admin_password():
    return "1234"


@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(better_get_admin_password("billing"))

print(get_admin_password.__name__)

user = {"username": "admin", "password": "<PASSWORD>", "access_level": "admin"}
print(get_password("billing"))
