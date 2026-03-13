'''
8-8. User Albums: Start with your program from Exercise 8-7 . Write a while loop that allows users to enter an album’s artist and title . Once you have that information, call make_album() with the user’s input and print the dictionary that’s created . Be sure to include a quit value in the while loop .
'''

def make_album(name,art_title,num_tracks=0):
    
    full = f"\n{name.title()} has {art_title.title()} album."
    
    if num_tracks:
        full = f"\n{name.title()} has {art_title.title()} album and it has {num_tracks} tracks in it."
    
    return full

while True:
    print("(enter 'q' at any point to quit.)")
    
    artistName = input("Enter a artist name: ")
    if artistName == 'q':
        break
    
    albumTitle = input("Enter artist album title: ")
    if albumTitle == 'q':
        break
    
    albumTracks = input("Enter number of tracks in the album: ")
    if albumTracks == 'q':
        break
    
    print(make_album(artistName,albumTitle,albumTracks))
    
    
