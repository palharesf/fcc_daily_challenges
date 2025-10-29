# Email Sorter

# On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.

# In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).

#     Sorting should be case-insensitive.
#     If more than one email has the same domain, sort them by their username.
#     Return an array of the sorted addresses.
#     Returned addresses should retain their original case.

# For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].
# Tests

# 1. sort(["jill@mail.com", "john@example.com", "jane@example.com"]) should return ["jane@example.com", "john@example.com", "jill@mail.com"].
# 2. sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]) should return ["bob@mail.com", "carol@mail.com", "alice@zoo.com"].
# 3. sort(["user@z.com", "user@y.com", "user@x.com"]) should return ["user@x.com", "user@y.com", "user@z.com"].
# 4. sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]) should return ["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"].
# 5. sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]) should return ["SAM@ALPHA.com", "sammy@alpha.com", "sara@alpha.com", "Sarah@Alpha.com", "simon@beta.com", "Simone@Beta.com"].

def sort(emails):
    # Sort emails by domain and username
    ranking = sorted(
        emails,
        key=lambda x: (x.split("@")[1].lower(), x.split("@")[0].lower()),
    )
    return ranking

sort(["jill@mail.com", "john@example.com", "jane@example.com"])
sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"])
sort(["user@z.com", "user@y.com", "user@x.com"])
sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"])
sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"])

# Comments - one of those challenges where I don't know what's happening, I get no learning from anything, there's no intuition involved, no feedback on what you're doing wrong, just kind of silly and annoying