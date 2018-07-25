from setuptools import setup, find_packages

setup(
	name="calculator",#name of the project
	version="v1.0",#number of the version
	author="louis",#author of the project
	author_email="louiscaixuran@163.com",#email used to connect the author
	description="calculator for demo",#desvription of the project
	url="",#the url os the github 
	packages=find_packages(),
	license="",#licence's name
	platforms="",#plate form of this project
	test_suite="test",

	entry_points={
		'console_scripts':[
			'cal = calculator.win:wincal',
			]
		}
)