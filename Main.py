##########################################################
#    _____                __   _  ______        __    _  #
#   / ___/ ____   ____   / /_ (_)/_  __/____   / /__ (_) #
#   \__ \ / __ \ / __ \ / __// /  / /  / __ \ / //_// /  #
#  ___/ // /_/ // /_/ // /_ / /  / /  / /_/ // ,<  / /   #
# /____// .___/ \____/ \__//_/  /_/   \____//_/|_|/_/    #
#      /_/                                               #
#   created by Eliott FLECHTNER & Sebastien KERBOURC'H   #
##########################################################

# Print the tag
tag = "   _____                __   _  ______        __    _ \n  / ___/ ____   ____   / /_ (_)/_  __/____   / /__ (_)\n  \__ \ / __ \ / __ \ / __// /  / /  / __ \ / //_// / \n ___/ // /_/ // /_/ // /_ / /  / /  / /_/ // ,<  / /  \n/____// .___/ \____/ \__//_/  /_/   \____//_/|_|/_/   \n     /_/                                              \n"
print('-' * 54)
print('-' * 54)
print(tag)
print('-' * 54)
print('-' * 54)

# Import librairies& modules
from time import sleep
import subprocess
import sys
import spotipy.client as spotipy
import spotipy as spot
import os
os.chdir('[path to bot here]')

# Sleep interval
interval = 1

# Hide the console
IS_WIN32 = 'win32' in str(sys.platform).lower()
def subprocess_call(*args, **kwargs):
    if IS_WIN32:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        kwargs['startupinfo'] = startupinfo
    retcode = subprocess.call(*args, **kwargs)
    return retcode

# Get the API authorization token
token = spot.util.prompt_for_user_token('qrop', "user-read-currently-playing", client_id = 'client_id_here', client_secret = 'client_secret_here', redirect_uri = 'http://localhost:8888/callback')
sp = spotipy.Spotify(token)

# Get the type of the current playing track  
track = sp.current_user_playing_track()

# DEBUG FEATURE
if track == None:
    print("Nothing is currently being played by Spotify.")
else:
    print("Connected successfully!")
    print("Waiting for an ad to come up...")

# Check the track type and if it's an ad, mute the Spotify program using the MuteSpotify.exe application (in folder)
while track != None:
    # Print the current playing track type
    track_type = track["currently_playing_type"]

    # Check for the type of current playing track
    if track_type == "track" or track_type == "episode":
        # Constanly set Spotify's Windows volume to 100
        subprocess_call(["MuteSpotify.exe", "100"])
    else:
        # Mute Spotify
        subprocess_call(["MuteSpotify.exe", "0"])

    # Refresh the program each given interval & get current playing track
    track = sp.current_user_playing_track()
    sleep(interval)
