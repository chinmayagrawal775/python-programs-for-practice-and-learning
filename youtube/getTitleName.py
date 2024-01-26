
from pytube import Playlist
import datetime

p = Playlist('https://youtube.com/playlist?list=PLbGui_ZYuhiiaQjuOfvgx_-gzVBlCxrk0')

# for video in p.videos:
#     print(video.title)

for video in p.videos:
    l= video.length
    lt = str(datetime.timedelta(seconds=l))
    print(lt.removeprefix('0:'))

# time = str(datetime.timedelta(seconds=401))
# print(type(time.removeprefix('0:')))

# print('a' + ' ' + 'b')

# str = 'Set Date Methods in JavaScript (Hindi)'

# # print(str.removesuffix('Hindi)'))
# print(str.__contains__(' in JavaScript (Hindi)'))
