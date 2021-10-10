# astocks.py   阿思达克网爬虫
import requests
import numpy as np 
from lxml import etree
import csv
from user_agent import ua_list
import random
import time
from queue import Queue
from threading import Thread

class AsSpider:
	def __init__(self,codes):
		self.codes = codes
		self.url = 'http://www.aastocks.com/tc/stocks/market/ipo/upcomingipo/ipo-info?symbol={}&s=3&o=1#info'
		self.data = []
		self.code_queue = Queue()

	def url_in(self):
		# code入队列
		for code in self.codes:
			self.code_queue.put(code)

	def get_html(self):
		# 获取响应页面
		while not self.code_queue.empty():
			code = self.code_queue.get()
			url = self.url.format(code)
			try:
				html = requests.get(url, headers={'User-Agent':random.choice(ua_list)}).content.decode('utf-8')
			except :
				print('error:',code)
				continue
			self.parse_html(html,code)

	def parse_html(self,html,code):
		# 解析页面相关数据
		parse_html = etree.HTML(html)
		one_count = parse_html.xpath('//*[@id="UCIPOInfo"]/div[1]/table/tbody/tr[1]/td[2]/text()')[0]
		value = parse_html.xpath('//*[@id="UCIPOInfo"]/div[1]/table/tbody/tr[4]/td[2]/text()')[0].split(' - ')[-1]
		total_count = parse_html.xpath('//*[@id="UCIPOInfo"]/div[1]/table/tbody/tr[6]/td[2]/text()')[0]
		HK_count = parse_html.xpath('//*[@id="UCIPOInfo"]/div[1]/table/tbody/tr[7]/td[2]/text()')[0].split('(')[0]
		if '沒有相關資料' in parse_html.xpath('//*[@id="UCIPOInfo"]/div[2]/div[2]/table/tr/td/text()')[0]:
			old_stock = '0'
		else:
			old_stock = '1'
		# 将相关数据存储到self.data
		self.data.append([code, one_count, value, total_count, HK_count, old_stock])

	def write_csv(self):
		with open('../data/astocks.csv','a') as f:
			writer = csv.writer(f)
			writer.writerows(self.data)


	def main(self):
		self.url_in()
		# 多线程爬虫
		t_list = []
		for i in range(8):
			t = Thread(target=self.get_html)
			t_list.append(t)
			t.start()
		for t in t_list:
			t.join()

		# 写入csv
		self.write_csv()
		print(len(self.data))


if __name__ == '__main__':
	with open('../data/livermore.csv', encoding='utf-8') as f:
		codes = np.loadtxt(f, str, delimiter = ',', usecols=(0))
		# codes = ['01024', '01156']
		spider = AsSpider(codes)
		spider.main()



