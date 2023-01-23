# Fstrings and formatting
# firstname = "jeff"
# lastname = "stanley"
# full_name = f"{firstname} {lastname}"
# print(f"Hello, {full_name.title()}!")

# Demonstrate use of letter case
# name = input("What is your name?")
# print(f"Hello, {name.lower()}!")
# print(f"Hello, {name.upper()}!")
# print(f"Hello, {name.title()}!")

# Print Famous quote and the name of its author
# Added some logic in there because why not
 author = input("Who is your favorite author?")
 author_choice = author.lower()
 tolkien_quote = "'All those who wander are not lost.'"
 dost_quote = "'Be silent, heart, Be patient, humble, hold thy peace'"
 new_quote = "'You have power over your mind - not outside events. Realize this, and you will find strength.'"
 new_author = "marcus aurelius"
 if author_choice == "j.r.r. tolkien":
    print(f"Here is a quote,\n{tolkien_quote}\n --{author_choice.title()} ")
 elif author_choice == "dostoevsky":
    print(f"Here is a quote,\n{dost_quote}\n --{author_choice.title()} ")
 else:
   print(f"I dont know that author, but here is a quote by someone new,\n{new_quote}\n --{new_author.title()} ")

#Use strip functions
#name = "   jeff    "
#print(name.rstrip())
#print(name.strip())
print(name.lstrip())
