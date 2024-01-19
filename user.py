from osignal import signal

class User:
    user_changed = signal(object)

    def __init__(self, name: str) -> None:
        self.name = name
    
    def set_name(self, name: str):
        self.name = name
        self.user_changed.emit(self)

def watch_user_change(user: object):
    print("User changed", user)
    print(user.name)

user = User("test")
user.user_changed.connect(watch_user_change)
user.set_name("Test")