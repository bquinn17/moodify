from django.shortcuts import render
from textAnalysis.analyze import process_text
from playlistRequest.request import request_access_token, get_playlist, preform_post

from moodify.models import SpotifyUser
from django.utils import timezone
import datetime


def create_user(request):
    """
    Number 5
    :param request:
    :return:
    """
    if request.GET:
        user = SpotifyUser()
        user.access_token = request.GET['access_token']
        delta = int(request.GET['expires_in'])
        user.expires_at = timezone.now() + datetime.timedelta(seconds=delta)
        user.refresh_token = request.GET['refresh_token']
        user.save()


def refresh_token(user):
    # Number 7
    data = {
        'Authorization': '785d3e5e20de418e8426447f5cad289e:c991355fd674496d862339056925fcf2'
    }
    body = {
        'grant_type': 'refresh_token',
        'refresh_token': user.refresh_token
    }
    url = 'https://accounts.spotify.com/api/token'
    response = preform_post(url, data, body)
    user.access_token = response['access_token']
    delta = int(response['expires_in'])
    user.expires_at = timezone.now() + datetime.timedelta(seconds=delta)
    user.save()
    return


def spotify_request(request, auth_id=''):  # This will be hard coded for now
    if request.GET:
        user = SpotifyUser.objects.get(access_token=auth_id)
        if user.expires_at < timezone.now():
            refresh_token(user)

        text = request.GET['text']
        mood = process_text(text)
        options_hash = {
            'country': 'US',
            'limit': '50'
        }
        playlist = get_playlist(mood, auth_id, options_hash)


def get_access_token(auth_code):
    access_code = request_access_token(auth_code)


def callback(request):
    # Number 3
    if 'error' in request.GET.keys():
        error = request.GET["error"]
        print("Error: " + error)
    else:
        error = None

    state = request.GET["state"]
    print("State: " + state)

    if 'code' in request.GET:
        code = request.GET["code"]
        print("Code: " + code)

    # ?error=access_denied&state=STATE

    if not error:
        message = "Successfully Logged in"
        get_access_token(code)
    else:
        message = "Login failed"

    return render(request, 'login_response.html', {'message': message,
                                                   'error': error})

