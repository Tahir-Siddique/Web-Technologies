# # Create an empty set
# s = set()
# # Add elements to set
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# s.add(3)  # < ---
# print(s)
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper


@announce
def hello():
    print("Hello, World!")


hello()
