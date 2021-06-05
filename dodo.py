def task_wheel():
	return {
		'actions': ['python3 setup.py bdist_wheel'],
	}
	
def task_html():
	return {
		'actions': ['sphinx-build -M html source build'],
	}
	
def task_pot():
	return {
		'actions': ['pybabel extract -o po/common.pot chat/common.py'],
		'file_dep': ['chat/__main__.py'],
		'targets': ['po/common.pot']
	}
	
def task_po():
	return {
		'actions': ['pybabel update -D app -i po/common.pot -l ru -d po -o po/ru/LC_MESSAGES/common.po'],
		'file_dep': ['po/common.pot'],
		'targets': ['po/ru/LC_MESSAGES/common.po'], 
	}
	
def task_mo():
	return {
		'actions': ['pybabel compile -D app -i po/ru/LC_MESSAGES/common.po -o po/ru/LC_MESSAGES/app.mo'],
		'file_dep': ['po/ru/LC_MESSAGES/common.po'], 
	}
	
def task_all():
	return {
		'actions': ['echo All'],
		'task_dep': ['mo', 'html', 'wheel'], 
	}
