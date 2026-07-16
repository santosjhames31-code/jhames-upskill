class User:

    def __init__(self, firstName, lastName, likesCount, friendList):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendList = friendList

    def details(self):
        print(f"Name  : {self.firstName} {self.lastName} ")
        print(f"Likes : {self.likesCount}")
        print("Friends")
        for friend in self.friendList:
            print("-", friend)  

user1 = User("Jhames", "Santos", 67, ["Mark", "Gian", "Dave"] )
user1.details()