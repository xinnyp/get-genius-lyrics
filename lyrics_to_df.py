import get_lyrics


def lyrics_to_df(data_dict, dataframe):
    for song in data_dict['songs']:
        response = get_lyrics.request_song_info(data_dict['artist'], song)
        json_obj = response.json()

        remote_song_info = None
        for hit in json_obj['response']['hits']:
            remote_song_info = hit
            break

        if remote_song_info:
            song_url = remote_song_info['result']['url']
            lyrics = get_lyrics.scrape_song_url(song_url)
        else:
            print(song + 'not found')
        if data_dict['album'] != None:
            song_data = {'artist': data_dict['artist'], 'album': data_dict['album'], 'song_name': song,
                        'lyrics': lyrics}
        else:
            song_data = {'artist': data_dict['artist'], 'song_name': song,
                         'lyrics': lyrics}
        dataframe = dataframe.append(song_data, ignore_index=True)

    return dataframe



