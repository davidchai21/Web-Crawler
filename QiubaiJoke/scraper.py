# -*- coding: utf-8 -*-
import urllib.request # Python3 merged urllib2 into urllib :)
import re
import os

class QiuBai():
	def __init__(self):
		self.url="https://www.qiushibaike.com/text/page/"
		self.agent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
		self.header={"User-Agent": self.agent}

	def getText(self,n):
		request=urllib.request.Request(self.url+str(n),headers=self.header)
		response=urllib.request.urlopen(request)
		data=str(response.read(),'utf-8')
		pattern=re.compile('<div class="content">.*?<span>\n\n\n(.*?)\n.*?\n</span>.*?<span.*?>.*?</span>.*?</div>',re.S)
		items=re.findall(pattern,data)
		return items

	def show(self,n):
		t=self.getText(n)
		for i in range(len(t)):
			print("-->"+t[i]+"\n")

	def start(self):
		n=1
		while True:
			self.show(n)
			l=input("***Press Enter to continue... If you want to quit, please input q and press Enter:")
			if l=="q" or l=="Q":
				print("Byebye!!!")
				break;
			else:
				os.system('clear')
				n=n+1


a=QiuBai()
a.start()