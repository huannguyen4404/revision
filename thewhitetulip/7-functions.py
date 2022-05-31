def join(name, mode):
    return name + mode, name


one, two = join("m", "ambient")
print(one, two)
