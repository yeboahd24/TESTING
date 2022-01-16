import requests

# Youtube video downloader
# https://www.youtube.com/watch?v=X8Z-_x-_8-U
def download_video(url):
    """
    Download video from youtube
    """
    print('Downloading video')
    response = requests.get(url, stream=True)
    with open('video.mp4', 'wb') as handle:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                handle.write(chunk)
    print('Video downloaded')
    
download_video('https://www.youtube.com/watch?v=sQpSvZYRf_0&list=PLfdtiltiRHWF0T2HE1D4hxN4vaeh4wW3g&index=8')