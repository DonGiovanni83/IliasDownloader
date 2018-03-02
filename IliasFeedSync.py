import feedparser
import time


class IliasFeedSync:
	#RSS_Source = open('rssfeed.txt', 'r')
	#RSS_URL = RSS_Source.readline()

	#NewDownloads = open('PendingDownloadLinks.txt', 'r+')
	#AlreadyDownloaded = open('FeedDownloadTitles.txt', 'r+')

	#print "Updating your Feed. This will take a moment."

	#feed = feedparser.parse(RSS_URL)

	#LinksInFeed.truncate()
	
	def getNewObjects(feed, already, dowDoc):
		DownloadCounter = 0
		NewForumPostCounter = 0
		for item in feed.entries:
			already.seek(0)
			for lines in already:
				if item.link != lines:
					if 'file' in item.link:
						dowDoc.write(item.link +'\n')
						print "----------------------New File to Download----------------------"
						print('\n' + item.title + '\n')
						DownloadCounter = DownloadCounter+1
					elif 'frm' in item.link:
						print "-------------------------New Forum Post-------------------------"
						print ('\n' + item.title + '\n')
						NewForumPostCounter = NewForumPostCounter +1
				time.sleep(0.05)	


		print str(DownloadCounter) + " files are ready to be Downloaded"

	#NewDownloads.close()
	#AlreadyDownloaded.close()
