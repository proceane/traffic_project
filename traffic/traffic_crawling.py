# 데이터 크롤링
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame as df
import pandas as pd

# 노선별 VMS표출내용 일괄조회 
def get_vms_message(request):
	route_no = request.GET.get('route_no') if request.GET.get('route_no') else '0010' 
	route_no = route_no.zfill(4)
	req = requests.get("http://data.ex.co.kr/openapi/vms/vmsMessageSrchByRoute?key=3383868115&type=xml&routeNo="+route_no+"&numOfRows=100")
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	vms_list = soup.findAll('vmsmessagesrchbyroutelists')
	vms_message = []

	for vms in vms_list:
		vmsmessage = vms.vmsmessage.string
		vmsmessage2 = vms.vmsmessage2.string
		vms_message.append({'vmsmessage' : vmsmessage, 'vmsmessage2' : vmsmessage2})

	return vms_message


# 구간 교통량 조회
def get_traffic_data(request):
	traffic_data = {}
	req = requests.get('http://data.ex.co.kr/openapi/odtraffic/trafficAmountByRealtime?key=3383868115&type=xml')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	traffic_list = soup.findAll('list')
	conzone_id = request.GET.get('conzone_id') if request.GET.get('conzone_id') else '0010CZE470' 
	route_no = request.GET.get('route_no') if request.GET.get('route_no') else '0010' 
	route_no = route_no.zfill(4)
	#print(route_no)
	updown_type_code = request.GET.get('updown_type_code') if request.GET.get('updown_type_code') else 'E'
	#print(conzone_id + ", " + route_no + ", " + updown_type_code)
	for traffic in traffic_list:
		if conzone_id == traffic.conzoneid.string and route_no == traffic.routeno.string and updown_type_code == traffic.updowntypecode.string :
			#print("success!")
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
	#print(len(traffic_data))
	return traffic_data

#top5 데이터 가져오기
def get_top5_data(request):
	traffic_top_data = {} #리턴값
	amount = []			#교통량
	speed = []			#속도
	ratio = []			#점유율
	conzone_name = []	#구간명
	route_name =[]		#고속도로명

	req = requests.get('http://data.ex.co.kr/openapi/odtraffic/trafficAmountByRealtime?key=3383868115&type=xml')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	traffic_list = soup.findAll('list')

	for traffic in traffic_list:
		amount.append(traffic.trafficamout.string)
		speed.append(traffic.speed.string)
		ratio.append(traffic.shareratio.string)
		conzone_name.append(traffic.conzonename.string)
		route_name.append(traffic.routename.string)

	#dataFrame으로 변환
	top_df = df(data={'route_name' : route_name, 'conzone_name' : conzone_name, 'amount' : amount, 'speed' : speed, 'ratio': ratio})

	#정렬할 값 숫자 변환
	top_df[['amount', 'speed', 'ratio']] = top_df[['amount', 'speed', 'ratio']].apply(pd.to_numeric)

	#속도 top5
	speed_df = top_df.sort_values(by=['speed'], ascending=False).head()
	#교통량 top5
	amount_df = top_df.sort_values(by=['amount'], ascending=False).head()
	#점유율 top5
	ratio_df = top_df.sort_values(by=['ratio'], ascending=False).head()

	traffic_top_data['speed_list'] = get_top5_list(speed_df)
	traffic_top_data['amount_list'] = get_top5_list(amount_df)
	traffic_top_data['ratio_list'] = get_top5_list(ratio_df)

	#print(len(traffic_top_data['amount_list']))

	return traffic_top_data

#dataframe -> list 변환
def get_top5_list(df_list):
	df_return_list = []
	for item in df_list.values :
	    df_return_list.append({
	        'route_name' : item[0],
	        'conzone_name' : item[1],
	        'amount' : item[2],
	        'speed' : item[3],
	        'ratio' : item[4]
	    })

	return df_return_list

#구간 조회
def getConzoneList(roadCode):
	conzone_list = pd.read_csv('traffic/data/conzoneList.csv', encoding='utf-8')
	#print(type(roadCode))
	conzone_df = conzone_list[(conzone_list['노선번호'] == int(roadCode))]
	context = []
	for item in conzone_df.values:
		context.append({
			'conzone_id' : item[0],
			'conzone_name' : item[9],
			'updown_type_code' : item[2]
		})
	return context

def getUpDownCode(roadCode, conzone_id):
	conzone_list = pd.read_csv('traffic/data/conzoneList.csv', encoding='utf-8')
	conzone_df = conzone_list[(conzone_list['노선번호'] == int(roadCode)) & (conzone_list['콘존ID'] == conzone_id)]
	context = []
	for item in conzone_df.values:
		context.append({
			'conzone_id' : item[0],
			'updown_type_code' : item[2]
		})
	return context
