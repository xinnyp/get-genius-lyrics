# get-genius-lyrics
This can be used to scrape song lyrics using Genius API into dataframes

get_lyrics.py can be executed independently on the command line:

pyton get_lyrics.py <song_title> <artist_name>


lyrics_to_df.py contains the lyrics_to_df function(data_dict, dataframe)

- data_dict: dictionary in the following format

~~~~ 
{'artist': ARTIST_NAME, 'album': None or ALBUM_NAME, 'song_name' : [SONG_NAME1,SONG_NAME2...] } 
~~~~ 

-dataframe: requires a pandas df

and returns the following dictionary

~~~~ 
{'artist': 'ARTIST_NAME', 'album': None or 'ALBUM_NAME', 'song_name' : 'SONG_NAME' , lyrics: 'SONG_LYRICS'
~~~~ 


You will need a Genius API token to be able to use this
