from pytube import YouTube,Search

def data(video):
    print(video)
    print(type(video.title))
    print()
    try:
        # urll = video.streams.filter(file_extension='mp4').url
        # print(urll)
        video = video.streams.get_highest_resolution()
        
    except:
        return
    data={
        'url':url,
        'thumbnail_url':video.thumbnail_url,
        'title':video.title
        
    }
    
    return data

def video(search_str='4k video song'):
    srch =Search(search_str)
    try:
        video_deatils = srch.results
    except:
        pass

    videos_data =[data(i) for i in video_deatils[:1]]
    # print(videos_data)
    # print(len(video_deatils))
    # print(len(videos_data))
    return videos_data[0]


if __name__=='__main__':
    print(video())
    
