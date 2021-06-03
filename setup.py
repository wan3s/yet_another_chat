from setuptools import setup, find_packages

setup(
	name = "test_wheel",
	version = "0.0.1",
	packages = ["src",],
	package_data={'src': ['po/ru/LC_MESSAGES/func.po', 'po/ru/LC_MESSAGES/app.mo']},
	install_requires=['django','pymongo'],
)
