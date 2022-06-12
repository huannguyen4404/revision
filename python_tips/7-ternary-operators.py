is_nice = True
state = "nice" if is_nice else "not nice"


# NOT being Pythonic
# nice = True
# personality = ("mean", "nice")[nice]
# print("The cat is ", personality)

def show_name(real_name, display_name=None):
    display_name = display_name or real_name
    print(display_name)


show_name("Huan")
show_name("Huan", "Henry")
