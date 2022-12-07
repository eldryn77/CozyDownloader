from urllib.parse import urlparse
import os

url = input("Enter URL: ")

parsed_url = urlparse(url)

# Split the path into individual segments
path_segments = parsed_url.path.split('/')

# Build the URL to the m3u8 file
final_url = 'https://cozycdn.foxtrotstream.xyz/' + path_segments[2] + '/' + path_segments[1] + '/' + path_segments [3] + '/index.m3u8'
file_name = (path_segments[1] + '_' + path_segments [3])

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
