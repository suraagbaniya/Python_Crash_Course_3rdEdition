'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python . Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message .
'''

def make_shirt(size="large",message="I love python"):
        print(f"\nThe size of the t-shirt is {size}.\nThe message on that t-shirt says '{message}'\n")

make_shirt()
make_shirt("medium")
make_shirt("small","I love C++")