'''Note:Downloading copyrighted content without permission is
illegal and can result in legal consequences.

I am going to download a video
from my own YouTube channel for the demo purpose.
'''

# Installing pytube library to call required functions to complete the task
# Pip install pytube

# Importing YouTube Function from pytube Library/Module
from pytube import YouTube

# Initializing variable with Youtube Video URL which we want to Download
youtube_video = 'https://www.youtube.com/watch?v=nr_OjLnAmfQ&t=27s'

# Passing Url while calling Youtube Function for Youtube API Connection 
youtube_object = YouTube(youtube_video)

# Storing Highest Resolution(Quality) of the Video
get_highest_resolution = youtube_object.streams.get_highest_resolution()

'''Storing path where we want to download out video(It is optional,
If we don’t give any path video will get download on Default path)'''

download_path = r"C:\Users\shiva\OneDrive\Desktop\Shivangi\PYTHON\Python_Tasks"
get_highest_resolution.download(download_path)

# printing confirmation message
print('Successfully Downloaded Youtube Video!')
