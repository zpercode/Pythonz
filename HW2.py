from sys import argv

script, user_name = argv
prompt = 'Answer'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you enjoy to shop {user_name}?")
enjoy = input(prompt)

print(f"What stores you like shop at? {user_name}?")
shop = input(prompt)

print("How much money do you put aside a month for shopping?")
money = input(prompt)

print("Whhen you go can you pick me up a shirt?")
picking = input(prompt)
print(f"""
Alright, so you said {enjoy} to like shop.
So you like do your shopping at {shop}. that cool!.
You put aside {money} month to shop. spend that money!
""")
