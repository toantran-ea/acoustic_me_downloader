# Acoustic me - Downloader


import wget
import urllib2
import re

from bs4 import BeautifulSoup

def download_song(song_url):
	print 'Now downloading ' + song_url
	wget.download(song_url)

def extract_songs(url):
	#parse page at url
	print 'Analyzing url for songs in page ....'
	urls = []
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)
	for link in soup.findAll('a', attrs={'href': re.compile('mp3$')}):
   		urls.append(link.get('href'))
   	print 'Done analyzing song urls. Found ' + str(len(urls)) +  ' song urls.'
   	return urls	

def download(page_url):
	downloaded_songs = 0
	for song in extract_songs(page_url):
		download_song(song)
		downloaded_songs += 1
	return downloaded_songs

if __name__ == '__main__':
	print 'Start downloading songs ....'
	song_number = download('http://yan.vn/radio/acoustic-tinh-bang-khuang/')
	print 'Finish downloading ' + str(song_number) + ' songs'


