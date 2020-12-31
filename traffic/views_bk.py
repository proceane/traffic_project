from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.template import loader
import re
# Create your views here.

#메인 페이지
def index(request) :
    name = {'page' : 'main_page'}
    return render(request, 'traffic/index.html', name)

#통계 페이지
def statistics(request) : 
	name = {'page' : 'statistics'}
	return render(request, 'traffic/statistics.html', name)

#사이트 정보 페이지
def infomation(request) : 
	name = {'page' : 'infomation'}
	return render(request, 'traffic/infomation.html', name)

#크롤링용 임포트
import requests
from bs4 import BeautifulSoup

#데이터 크롤링
import crawling

class getTrafficList(View):
	

	def post(self, request):
		req = requests.get('http://data.ex.co.kr/openapi/odtraffic/trafficAmountByRealtime?key=3383868115&type=xml')
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		traffic_list = soup.findAll('list')
		conzone_id = request.GET.get('conzone_id')
		route_no = request.GET.get('route_no')
		updown_type_code = request.GET.get('updown_type_code')
		print("conzone_id : ", conzone_id)
		for traffic in traffic_list:
			if conzone_id == traffic.conzoneid.string and route_no == traffic.routeno.string and updown_type_code == traffic.updowntypecode.string :
				traffic_data = {
    				'conzone_id' :  traffic.conzoneid.string,
    				'conzone_name' : traffic.conzonename.string,
    				'conzone_1' : traffic.conzonename.string.split('-')[0], 
    				'route_no' : traffic.routeno.string,
    				'route_name' : traffic.routename.string,
    				'speed' : traffic.speed.string,
    				'date_year' : traffic.stddate.string[:4],
    				'date_month' : traffic.stddate.string[4:6],
    				'date_date' : traffic.stddate.string[6:],
    				'time_hour' : traffic.stdhour.string[:2],
    				'time_min' : traffic.stdhour.string[2:],
    				'time_avg' : traffic.timeavg.string,
    				'share_ratio' : traffic.shartratio.string,
    				'traffic_amout' : traffic.trafficamout.string
    			}
		return render(request, self.template_name, traffic_data)

	def get(self, request):
		template_name = loader.get_template('traffic/index.html')
		traffic_data = {}
		req = requests.get('http://data.ex.co.kr/openapi/odtraffic/trafficAmountByRealtime?key=3383868115&type=xml')
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		traffic_list = soup.findAll('list')
		conzone_id = request.GET.get('conzone_id') if request.GET.get('conzone_id') else '0010CZE470' 
		route_no = request.GET.get('route_no') if request.GET.get('route_no') else '0010' 
		updown_type_code = request.GET.get('route_no') if request.GET.get('updown_type_code') else 'E'
		for traffic in traffic_list:
			if conzone_id == traffic.conzoneid.string and route_no == traffic.routeno.string and updown_type_code == traffic.updowntypecode.string :
				traffic_data = {
    				'conzone_id' :  traffic.conzoneid.string,
    				'conzone_name' : traffic.conzonename.string,
    				'conzone_1' : traffic.conzonename.string.split('-')[0], 
    				'route_no' : traffic.routeno.string,
    				'route_name' : traffic.routename.string,
    				'speed' : traffic.speed.string,
    				'date_year' : traffic.stddate.string[:4],
    				'date_month' : traffic.stddate.string[4:6],
    				'date_date' : traffic.stddate.string[6:],
    				'time_hour' : traffic.stdhour.string[:2],
    				'time_min' : traffic.stdhour.string[2:],
    				'time_avg' : traffic.timeavg.string,
    				'share_ratio' : traffic.shareratio.string,
    				'traffic_amount' : traffic.trafficamout.string
    			}

		print(traffic_data)
		return HttpResponse(template_name.render(traffic_data, request))

