class User:
    def __init__(self, userID, userName):
        self.id = userID
        self.userName = userName
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "kelmen")
user2 = User("002", "jack")

user1.follow(user2)
print(user1.following)