# lm_spider.py    利弗莫尔数据爬虫
import requests
import csv

class LmSpider:
	def __init__(self):
		self.url = 'https://h5stockserver.huanshoulv.com/aimapp/hkstock/hotNewStock?page=1&page_count=1000&stock_type=3&sort_field_name=issue_date&year={}&sort_type=1&is_newversion=true'
		

	def get_data(self,url):
		# 获取json数据
		data_json = requests.get(url).json()
		self.write_csv(data_json)

	def write_csv(self,data_json):
		# 解析数据
		stock_list = []  # 创建空列表储存所有股票数据
		for stock in data_json['data']['list']:
			stock_code = stock[4]
			complany = stock[58]
			issue_data = stock[9]
			plate = stock[26]
			market = stock[16]
			over_multiple = stock[2]
			one_price = stock[25]
			price = stock[18]
			issue_price = stock[11]
			# 将issue_price分解为上限定价和下限定价
			higt_price = issue_price.split('-')[-1]
			low_price = issue_price.split('-')[0]
			ipo_sponsor = stock[1]
			ipo_underwriter = stock[10]
			greenshoe = stock[39]
			one_prob = stock[24]
			must_count = stock[23]   # 
			prospectus_link = stock[42]
			# 提取必中手数数字
			if must_count:
				# must_count不为空时处理
				must_count = must_count[2:][:-5]
			open_rise = stock[19]
			close_rise = stock[22]
			stock_list.append([stock_code,complany,open_rise,close_rise,one_prob,must_count,issue_data,market,
				plate,one_price,over_multiple,price,low_price,higt_price,
				greenshoe,ipo_sponsor,ipo_underwriter,prospectus_link])
		
		# 写入csv
		with open('../data/livermore.csv','a') as f:
			writer = csv.writer(f)
			writer.writerows(stock_list)
		

	def main(self):
		for year in range(2021,2010,-1):
			#拼接url地址给get_data
			url = self.url.format(year)
			self.get_data(url)


if __name__ == '__main__':
	spider = LmSpider()
	spider.main()
