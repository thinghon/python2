print("20224016-박소호")
def menu_list(items):
    option=1
    for choice in items:
        print(str(option)+"."+choice)
        option=option+1
    print(str(option)+".Quit")
    return option