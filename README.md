# traffic_project
한국도로공사(http://data.ex.co.kr/)의 교통량 데이터를 이용하여 고속도로의 교통량을 한눈에 볼수 있는 프로그램입니다.<br>
It is a program that allows you to view the traffic of the highway you want at a glance using data of Korea Expressway Corporation(http://data.ex.co.kr/).
## Getting Start
본 프로젝트는 Django로 만들어졌으며 프로젝트를 구동하기 위해서는 아래 예제를 실행하셔야 합니다.<br>
This project made with Django Framework, and you need to run the example below if you want to operate this project.
### Prerequisites

해당 프로젝트에 사용된 언어는 python-3.8.5입니다.<Br>
The language used for this project is python-3.8.5.

프로젝트 구동을 위해 Anaconda를 설치해야 합니다.<br>
https://www.anaconda.com/products/individual

만약 pip버전이 낮다면 업그레이드를 해줍니다.<br>
If the pip version is low, upgrade it,
```
pip -m pip install --upgrade pip
```

### Virtual Environment
1. 빈 폴더를 생성한 뒤 명령 프롬프트에서 생성된 폴더 위치로 이동한 후에 아래 명령어를 입력합니다.<br>
Make empty folder, navigate to the created folder at the command prompt and enter the following command.
```
conda create -n traffic
```
'traffic'은 가상환경이름입니다. 원하시는 가상환경 이름이 있다면 변경하셔도 좋습니다.<br>
'traffic' is the name of the virtual environment. if you have the name of virtual environment you want, you can change it.

2. 가상환경을 실행합니다.
Activate the virtual environment you made.
```
conda activate traffic
```

3. Django를 설치합니다. Install Django.
```
pip install django
```

4. Django 프로젝트를 생성합니다. Create Django project.
```
django-admin startproject traffic_project
```
'traffic_project'는 이 프로젝트명과 동일하기 때문에 바꾸지 않는것을 권장합니다.<br>
Since 'traffic_project' is the same as this project name, it is not recommended to change it.<br>

5. 해당 github파일을 해당 프로젝트에 넣습니다.
 
### Authentication key
프로그램을 사용하기 위해서는 인증키가 필요합니다.<br>
You need an authentication key to use the program.

https://data.ex.co.kr/openapi/apikey/requestKey 에서 인증키를 받으세요.<br>
Get an authentication key from the link.

인증키를 받은 후에 traffic_crawling.py 7행에 인증키를 입력합니다.<br>
After get an authentication key, enter an key in traffic_crawling.py line 7
```python
key = "" # http://data.ex.co.kr/에서 발급받은 키
```

### Run project
manage.py가 있는 디렉터리에서 해당 명령어를 입력합니다.
```
python manage.py runserver
```

## Example of use
![교통량_img_1](https://user-images.githubusercontent.com/62143949/109973695-13491b00-7d3c-11eb-9552-9a67c3ae87d4.JPG)
select box로 고속도로와 구간을 검색하면 해당 구간의 교통량, 평균통행시간, 평균속도, 점유율을 확인할 수 있습니다.<br>
If you search for a highway and section using the select box, you can see the traffic, average time, average speed and occupancy rate of the section.

![교통량_img_2](https://user-images.githubusercontent.com/62143949/109973821-3378da00-7d3c-11eb-8c66-a1c9c3b570fd.JPG)
하단에서는 교통량, 속도, 점유율 Top5구간을 확인할 수 있습니다.<br>
At the bottom, you can see the traffic, speed, and occupancy Top-5 sections.

## Reference
### html template
https://github.com/ColorlibHQ/gentelella

### Django guide
https://docs.djangoproject.com/ko/3.1/intro/tutorial01/

### Anaconda virtual environment guide
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
