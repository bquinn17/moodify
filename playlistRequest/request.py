
from urllib.request import Request, urlopen
import random

# client_id = 'CLIENT_ID' #Your client id
# client_secret = 'CLIENT_SECRET' # Your secret


def request_access_token(auth_code):
    preform_post()


def preform_post(url, data, body=''):
    post_request = Request(url)  # "http://localhost/users/create"
    post_request.data = body

    for key in data.keys():
        post_request.add_header(key, data[key])

    response = urlopen(post_request).read()
    return response


def get_playlist(category_id, auth_id, options={}):
    playlists_hash = preform_get(category_id, auth_id, options)
    index = random.randint(0, len(playlists_hash))
    playlist = playlists_hash['items'][index]
    return playlist


def preform_get(category_id, auth_id, options={}):
    """
    Preforms the get request to Get a Category’s playlists
    :param category_id:
    :param auth_id:
    :param options:
    :return:
    """
    # curl -i -X GET "https://api.spotify.com/v1/browse/categories/party/playlists?country=BR&limit=2"
    # -H "Authorization: Bearer {your access token}"

    url = "https://api.spotify.com/v1/browse/categories/{0}/playlists".format(category_id)

    if options:
        url += "?"
    count = 0

    for option in options.keys():  # country: US
        url += option + "="
        if count < len(options) - 1:
            url += "&"

    get_request = Request(url)
    get_request.add_header("Authorization", "Bearer " + str(auth_id))

    response = urlopen(get_request).read()
    return response


if __name__ == "__main__":
    category = "rock"
    options_hash = {
        'country': 'US',
        'limit': '50'
    }
    auth_token = "TODO"
    preform_get(category, auth_token, options_hash)