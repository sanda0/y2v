#by sandakelum priyamantha
from pytube import YouTube,Playlist
import os
from tkinter import *
import tkinter as tk


def make_folder():
	home = os.path.expanduser("~")
	path = os.path.join(home,"Videos")
	path_to_y2v = os.path.join(path,"y2v")
	try:
		os.mkdir(path_to_y2v)
	except:
		# print("folder allready exists")
		pass
	return path_to_y2v


def get_list(link,path,text_obb):
	text_obb.insert(END,"starting....\n")
	text_obb.see(END)
	path_ = make_folder()
	path_ = os.path.join(path_,path)
	try:
		os.mkdir(path_)
	except:
		text_obb.insert(END,str(path_)+" is allready exists\n")
		text_obb.see(END)

	try:
		list_ = Playlist(link).video_urls
	# print(list_)
		text_obb.insert(END,str(len(list_))+" videos in this list.\n")
		text_obb.see(END)
	except:
		text_obb.insert(END,"[*]invalide link\n")
		text_obb.see(END)

	text_obb.insert(END,"\nDownloading path : %s\n"%(str(path_)))
	text_obb.see(END)
	for video in list_:
		try:
			# text_obb.insert(END,str(video)+"\n")
			# text_obb.see(END)
			opened_video = YouTube(video)
			load_video = opened_video.streams.first()
			file_size = str(int((load_video.filesize/1000)/1000))
			text_obb.insert(END,str(opened_video.title)+" downloading...\n")
			text_obb.see(END)
			load_video.download(path_)
			text_obb.insert(END,"Done..\n")
			text_obb.see(END)

		except:
			text_obb.insert(END,"con't open this link"+str(video)+"\n")
			text_obb.see(END)

		



def get_one(link,text_obb):
	text_obb.insert(END,"starting...\n")
	text_obb.see(END)
	path = make_folder()
	text_obb.insert(END,"\nDownloading path : %s\n"%(str(path)))
	text_obb.see(END)
	try:
		opened_video = YouTube(link)
		load_video = opened_video.streams.first()
		file_size=str(int((load_video.filesize/1000)/1000))
		text_obb.insert(END,str(opened_video.title)+" downloading...\n")
		text_obb.see(END)
		load_video.download(path)
		text_obb.insert(END,"Done....\n	")
		text_obb.see(END)
	except:
		text_obb.insert(END,"[*]invalide link.\n")

# run
make_folder()