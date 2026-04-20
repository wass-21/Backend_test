import random


class JackpotMachine:
    #define attributes
    #users --> username -> {password, balance, history, total_winnings}
    def __init__(self):
        self.users = {} 
        self.current_user = None
        self.pot = 0

    #sign_up function + check if username already exists + store the new user details
    def sign_up(self, username: str, password: str):
        if username in self.users: 
            raise Exception("Username already taken.")
        self.users[username] = {
            "password": password,
            "balance": 0.0,
            "history": [],
            "total_winnings": 0.0
        }
        print("Signup successfully")

    #sign_in function , check if the username exists or no +  check the password if correct or no 
    def sign_in(self, username: str, password: str):
        if username not in self.users:
            raise Exception("Username does not exist.")
        if self.users[username]["password"] != password:
            raise Exception("Incorrect password.")
        self.current_user = username 
        print("Signin successfully")

    #sign_out function , check if the current user exists first and then put it none to signout
    def sign_out(self):
        if not self.current_user:
            raise Exception("No user is currently signed in.")
        self.current_user = None

    def add_to_balance(self, amount: float):
        #the user should be signed in to add amount
        if not self.current_user:
            raise Exception("No user signed in.")
        if amount <= 0:
            raise Exception("Amount must be positive.")
        self.users[self.current_user]["balance"] += amount

    def view_balance(self):
        #always check if current user exists , the user should be signed in
        if not self.current_user:
            raise Exception("No user signed in.")
        return self.users[self.current_user]["balance"]
    
    def spin_jackpot(self):
        #the spin is for signedin user so we should check 
        if not self.current_user:
            raise Exception("No user signed in.")

        #we collect the user data
        user = self.users[self.current_user]

        #if the soin reduce 10 coins , so the balance should be greater than 10
        if user["balance"] < 10:
            raise Exception("Not enough balance to spin.")

        # Reduce 10 coins from the user balance and add them to the pot
        user["balance"] -= 10 
        self.pot += 10

        # Generate result (array of 3 random numbers from 0 to 9)
        result = [random.randint(0, 9) for _ in range(3)] 
        winnings = 0

        # Determine winnings
        if result[0] == result[1] == result[2]:
            if result[0] == 7: #if all the numbers are equals and equal 7 the user win the entire pot
                winnings = self.pot  # entire pot
            else:
                winnings = self.pot / 2 #if all numbers are equals the user win the half
        
        elif result.count(7) == 2: #if 2 of numbers are 7 , the user wins a quarter
            winnings = self.pot / 4

        # Update balances
        if winnings > 0:
            user["balance"] += winnings
            user["total_winnings"] += winnings #used to indicate the top 10 users
            self.pot -= winnings

        # Save history
        user["history"].append((result, winnings))

        return result
    
    def view_history(self):
        #check if the there a signed in user
        if not self.current_user:
            raise Exception("No user signed in.")
        return self.users[self.current_user]["history"]
    
    def leaderboard(self):
        # Sort users by total winnings 
        sorted_users = sorted(
            self.users.items(),
            key=lambda x: x[1]["total_winnings"],
            reverse=True 
        )
        #the lambda is just a quick, inline function. It tells Python how to extract the value to sort by.
        #reverse true because sorted return the elements in ascending order , we want them in descending order

        top_10 = sorted_users[:10] #we want only the first 10 users [:10]

        return [(username, data["total_winnings"]) for username, data in top_10]
    
if __name__ == "__main__":
    jm = JackpotMachine()

    # Sign up users
    jm.sign_up("wassim", "123")
    jm.sign_up("youssef", "111")

    jm.sign_in("wassim", "123")
    jm.add_to_balance(100)

    print("Wassim balance:", jm.view_balance())

    for _ in range(5):
        result = jm.spin_jackpot()
        print("Spin result:", result)

    print("Wassim history:", jm.view_history())
    jm.sign_out()

    # Youssef plays
    jm.sign_in("youssef", "111")
    jm.add_to_balance(50)

    for _ in range(3):
        print("Spin result:", jm.spin_jackpot())

    print("Youssef history:", jm.view_history())

    jm.sign_out()

    # Leaderboard
    print("Leaderboard:", jm.leaderboard())




