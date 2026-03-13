'''
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album . The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information . Use the function to make three dictionaries representing different albums . Print each return value to show that the dictionaries are storing the album information correctly .
Add an optional parameter to make_album() that allows you to store the number of tracks on an album . If the calling line includes a value for the num- ber of tracks, add that value to the album’s dictionary . Make at least one new function call that includes the number of tracks on an album .
'''

def make_album(name,art_title,num_tracks=0):
    
    full = f"\n{name.title()} has {art_title.title()} album."
    
    if num_tracks:
        full = f"\n{name.title()} has {art_title.title()} album and it has {num_tracks} tracks"
    
    return full

print(make_album("jhon", "love"))
print(make_album("sam", "hate"))
print(make_album("adele", "hello",9))
