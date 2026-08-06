name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion: ").strip()
emoji = input("Enter your emoji: ").strip()
website = input("Enter your website: ").strip()


print("\nChoose your Stule: ")
print("1. Simple Line")
print("2 Vertical Lines")
print("3 Emoji sandwich")

style = input("Enter 1, 2 or 3 :").strip()

def generate_bio(style):
    if style == "1":
        return f"{em}"