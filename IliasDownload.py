import feedparser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class IliasDownload:
	RSS_Source = open('rssfeed.txt', 'r')
	RSS_URL = RSS_Source.readline()

	NewDownloads = open('PendingDownloadLinks.txt', 'r+')
	AlreadyDownloaded = open('FeedDownloadTitles.txt', 'r+')

	print "Updating your Feed. This will take a moment."

	feed = feedparser.parse(RSS_URL)

	#LinksInFeed.truncate()

	IliasFeedSync.getNewObjects(feed, AlreadyDownloaded, NewDownloads)

	NewDownloads
	AlreadyDownloaded.close()
                                      
