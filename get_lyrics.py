import requests
import config
import sys
from bs4 import BeautifulSoup

def request_song_info(song_title, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + config.token}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response

def scrape_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    [h.extract() for h in html('script')]
    lyrics = html.find('div', class_='lyrics').get_text()
    return lyrics

def main():
    song_title = str(sys.argv[1])
    artist_name = str(sys.argv[2])
    print('{} by {}'.format(song_title, artist_name))
    response = request_song_info(song_title, artist_name)
    json_obj = response.json()
    remote_song_info = None

    for hit in json_obj['response']['hits']:
        if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
            remote_song_info = hit
            break

    if remote_song_info:
        song_url = remote_song_info['result']['url']
        lyrics = scrape_song_url(song_url)
        print(lyrics)
    else:
        print('lyrics not found')


if __name__ == '__main__':
    main()