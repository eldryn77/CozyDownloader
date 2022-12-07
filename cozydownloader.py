from urllib.parse import urlparse
import os
import datetime

url = input("Enter URL: ")

parsed_url = urlparse(url)

# Split the path into individual segments
path_segments = parsed_url.path.split('/')

length = len(path_segments)

if length == 4:
    print("\nVOD")
    
    # Build the URL to the m3u8 file
    final_url = 'https://cozycdn.foxtrotstream.xyz/' + path_segments[2] + '/' + path_segments[1] + '/' + path_segments [3] + '/index.m3u8'
    file_name = (path_segments[1] + '_' + path_segments [3])
    # Print information found and prompt user if they want to continue
    print("\nM3U8 URL: " + final_url)
    print("File Name: " + file_name)
    
    while True:
        cont = input("\nDownload? y/n > ")

        if cont == "n":
            print("Bye")
            break
        os.system('ffmpeg -i ' + (final_url) + ' -codec copy ' + (file_name) + '.mp4')
        print("Done")
        break

else: # Download ongoing livestreams
    print("\nLive")
    x = datetime.datetime.now()
    live_url = 'https://cozycdn.foxtrotstream.xyz/live/' + path_segments[1] + '/index.m3u8'

    # Print information found and prompt user if they want to continue
    print("\nM3U8 URL: " + live_url)

    while True:
        cont = input("\nPress Ctrl-C once to stop recording. \nDownload? y/n > ")

        if cont == "n":
            print("Bye")
            break

        print(live_url)
        os.system('ffmpeg -i ' + (live_url) + ' -codec copy ' + (path_segments[1]) + (x.strftime("_%Y-%m-%d_%H%M")) + '.mp4')
        break
        print("Done")
