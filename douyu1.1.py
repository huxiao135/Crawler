##################################
#by hu
#Get the anchor data for the king of fighting in douyu
#selenium+pandas
import re
import urllib.request as ur
from bs4 import BeautifulSoup
import pandas as pd
################
#使用该库时需要正确的
from selenium import webdriver

class DySpyder():

	def __init__(self, url):
		self.url = url

		self.text=['rid','title','href','name','see_num']

	def open_url(self, url):
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106.115 Safari/537.36'}
		req = ur.Request(url=url, headers=headers)  # python2，urllib.request()
		response = ur.urlopen(req)  # python2，urllib2.urlopen()
		return response.read().decode('utf-8')

	def from_url_get_all_lis(self):
		soup=[]
		chrome_option = webdriver.ChromeOptions()
		chrome_option.add_argument('--no-sandbox')
		chrome_option.add_argument('--disable-dev-shm-usage')
		chrome_option.add_argument('--disable-gpu')
		chrome_option.add_argument('blink-settings=imagesEnabled=false')
		chrome_option.add_argument('--headless')
		chchromedriver = "C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe"
		driver = webdriver.Chrome(chrome_options=chrome_option, executable_path=chchromedriver)
		driver.get(self.url)

		while True:

			soup1 = BeautifulSoup(driver.page_source, 'html.parser')
			soup=soup+soup1.find('ul',id="live-list-contentbox").find_all('li')

			driver.find_element_by_class_name("shark-pager-next").click()


			try:
				driver.find_element_by_xpath('//*[@class="shark-pager-next shark-pager-disable shark-pager-disable-next"]')
				break
			except:
				continue

		return soup

	def from_url_get_all_lis2(self):
		data = self.open_url(self.url)
		soup1 = BeautifulSoup(data, 'html.parser')
		soup = []
		for x in soup1.find_all('a', class_="play-list-link"):
			y = x.get('data-rid')
			soup.append(y)
		return soup
		#正则表达式抽取数据
	def tv_spyder(self, x):
		rid = re.findall(""".*?data-rid="(.*?)".*""", str(x))[0]
		title = re.findall(""".*?title=(.*?)>.*""", str(x))[0]
		href = re.findall(""".*?href="(.*?)".*""", str(x))[0]
		name = re.findall('''.*<span class="dy-name ellipsis fl">(.*?)</span>.*''', str(x))[0]
		#name = soup.find('span',{'class':'dy-name ellipsis fi'})
		see_num = re.findall('''.*<span class="dy-num fr".*?>(.*?)</span>.*''', str(x))[0]
		t = rid, title, href, name, see_num
		return t
	def tv_spyder1(self,x):
		rid = re.findall(""".*?data-rid="(.*?)".*""",str(x))[0]
		print(rid)
		return rid
def get_url():
	return "https://www.douyu.com/g_wzry"
def main():

	douyu = DySpyder(get_url())
	lis=douyu.from_url_get_all_lis()
	a=pd.DataFrame(index=douyu.text,columns=range(len(lis)))
	i=0
	for x in lis:
		try:
			a[i]=douyu.tv_spyder(x)
			i=i+1
		except:
			print('bunengzhuaqu')
	a.to_csv('dome.csv')

if __name__ == '__main__':
	main()