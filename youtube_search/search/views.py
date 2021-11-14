import requests
from django.core.paginator import Paginator
from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect

def index(request):
    videos = []

    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'  # url for the search results
        video_url = 'https://www.googleapis.com/youtube/v3/videos'   # url for the video results

        search_params = {
            'part' : 'snippet',
            'q' : "English News India Today",
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 100,
            'order':"date",
            'type' : 'video',
            'publishedAfter':'2021-11-4T00:00:00Z',
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items'] # coverts results into json format

        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 100
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        
        for result in results: #appends the result in vidoes and sends request through the videos list
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)

    
    return render(request, 'search/index.html', context) # final result