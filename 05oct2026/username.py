blocked_usernames = ["admin","root","moderator"]
entered_username = "spandana_45"
if entered_username not in blocked_usernames:
    print("username is valid.")
else:
    print("username is blocked")