class User:
    def __init__(self,user_id, username):
        self.id= user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follower (self, user):
        user.followers += 1
        self.following += 1
user_1 = User("001","garen")
user_2= User("001", "jack")


user_1.follower(user_2)
user_2.follower(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)