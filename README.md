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
 


