corr_username="admin"
corr_password="pass123"
usernames={"user","admin","test"}
passwords={"1234","admin","pass123","qwerty"}
for user in usernames:
    for pwd in passwords:
        print(f"trying {user}/{pwd}")
        if user==corr_username and pwd==corr_password:
            print(f"login successful with {user}/{pwd}")
            break
    else:
        continue
    break
