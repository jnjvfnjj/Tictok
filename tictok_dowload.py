import requests
import random

input_url = input('URL видео')
get_id_video = input_url.split('?')
current_id = get_id_video[0].split('/')[5]
video_api = requests.get(f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={current_id}').json()
# print(video_api)
video_url = video_api.get('aweme_list')[0].get('video').get('play_addr').get('url_list')[0]
print(video_url)
if video_url:
    print("скачиваем видео...")
    title_video = video_api.get('aweme_list')[0].get('desc')
    if title_video != ' ':
        title_video = random.randint(1111, 22222)
    try:
        with open(f'video/{title_video}.mp4','wb') as video_file:
            video_file.write(requests.get(video_url).content)
        print('Видео успешно скачан в шапку video')
    except Exception as error:
        print(f'Error: {error}')
else:print('')
