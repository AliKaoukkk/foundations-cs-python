class SocialMediaPlatform:
    def __init__(self):
        self.users = {}

    def addUser(self, username):
        if username in self.users:
            print("User already exists. Please use another username.")
        else:
            self.users[username] = []

    def removeUser(self, username):
        if username in self.users:
            for friend in self.users[username]:
                self.users[friend].remove(username)  # Remove user from friends' lists
            del self.users[username]
        else:
            print("User does not exist.")

    def sendRequest(self, user1, user2):
        if user1 not in self.users or user2 not in self.users:
            print("One or both users do not exist.")
        else:
            self.users[user1].append(user2)
            self.users[user2].append(user1)

    def removeFriend(self, user1, user2):
        if user1 not in self.users or user2 not in self.users:
            print("One or both users do not exist.")
        elif user2 not in self.users[user1] or user1 not in self.users[user2]:
            print("Users are not friends.")
        else:
            self.users[user1].remove(user2)
            self.users[user2].remove(user1)

    def viewFriends(self, username):
        if username in self.users:
            print("Friends of", username + ":", self.users[username])
        else:
            print("User does not exist.")

    def viewUser(self):
        print("Users on the platform:")
        for username in self.users:
            print(username)

    def displayMenu(self):
        while True:
            print("-" * 30)
            print("1. Add a user")
            print("2. Remove a user")
            print("3. Send a friend request")
            print("4. Remove a friend")
            print("5. View your list of friends")
            print("6. View the list of users")
            print("7. Exit")
            choice = input("Enter a choice: ")

            if choice == "1":
                username = input("Enter username: ")
                self.add_user(username)
            elif choice == "2":
                username = input("Enter username: ")
                self.remove_user(username)
            elif choice == "3":
                user1 = input("Enter your username: ")
                user2 = input("Enter friend's username: ")
                self.send_friend_request(user1, user2)
            elif choice == "4":
                user1 = input("Enter your username: ")
                user2 = input("Enter friend's username: ")
                self.remove_friend(user1, user2)
            elif choice == "5":
                username = input("Enter username: ")
                self.view_friends(username)
            elif choice == "6":
                self.view_all_users()
            elif choice == "7":
                print("Exiting the program.")
        else:
            print("Invalid choice. Please enter a valid option.")


