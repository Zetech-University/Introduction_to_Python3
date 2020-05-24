
def reverse(arg):
    if type(arg) == bool:
        arg = not arg
        print(arg)
    else:
        print("Boolean expected")

reverse(False)      # Returns True
reverse(True)       # Returns Fasle
reverse(1)      # Returns 'Boolean expected'
reverse('lady')      # Returns 'Boolean expected'