class User:
    def __init__(self, username):
        self.username = username

    def access_level(self):
        return "No specific access"


class Admin(User):
    def access_level(self):
        return f"{self.username}: Full access (Admin)"


class Guest(User):
    def access_level(self):
        return f"{self.username}: Limited access (Guest)"

u1 = Admin("admin")
u2 = Guest("visitor")

print(u1.access_level())
print(u2.access_level())
