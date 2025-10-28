# Navigator

# On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

# Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

#     You always start on the "Home" page, which will not be included in the commands array.
#     Valid commands are:
#         "Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
#         "Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
#         "Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.

# For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
# Tests

# 1. navigate(["Visit About Us", "Back", "Forward"]) should return "About Us".
# 2. navigate(["Forward"]) should return "Home".
# 3. navigate(["Back"]) should return "Home".
# 4. navigate(["Visit About Us", "Visit Gallery"]) should return "Gallery".
# 5. navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) should return "Home".
# 6. navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]) should return "Contact".
# 7. navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]) should return "Visit Us".

def navigate(commands):
    history = []
    location = -1
    for command in commands:
        # print("Command: ", command)
        if command == "Back":
            location -= 1
        elif command == "Forward":
            if location + 1 < len(history):
                location += 1
            else:
                pass
        else:
            history.append(command[6:])
            location += 1
        # print("History: ",history,"Location: ",location)
    
    if len(history) == 0 or location <= -1:
        # print("Home")
        return "Home"
    else:
        # print(history[location])
        return history[location]

navigate(["Visit About Us", "Back", "Forward"])
navigate(["Forward"])
navigate(["Back"])
navigate(["Visit About Us", "Visit Gallery"])
navigate(["Visit About Us", "Visit Gallery", "Back", "Back"])
navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"])
navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"])

# Comments - finished, but kind of annoying. It took a few attempts to get it right, and I'm not even sure this is a good approach
# It's not immediately clear what the intended solution was, so even though I made it work, I'm not sure I fully grasped what was being taught here