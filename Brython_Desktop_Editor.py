import eel
from free_port import localhost_free_port
import os
import sys
import subprocess

import tkinter as tk
from tkinter import filedialog

import pyautogui

import pkgutil
import encodings

from resource_path import resource_path



def all_encodings():
    modnames = set(
        [modname for importer, modname, ispkg in pkgutil.walk_packages(
            path=[os.path.dirname(encodings.__file__)], prefix='')])
    aliases = set(encodings.aliases.aliases.values())
    return modnames.union(aliases)



root = tk.Tk()
root.iconbitmap(resource_path('www/icon.ico'))
root.withdraw() # TRANSPARENTE
root.call('wm', 'attributes', '.', '-topmost', True) # TOP-MOST POSITION



eel.init('www')


@eel.expose
def arg_file_loader():
	if len(sys.argv) >= 2 and os.path.exists(sys.argv[1]):
		with open(sys.argv[1], 'r') as file:
			src = file.read()
			eel.client_load_file(src, os.getcwd()+'\\'+sys.argv[1])

@eel.expose
def file_dialog(mode):
	eel.switch_buttons()

	file_path = ''
	if mode == 'open':
		file_path = filedialog.askopenfilename(title='Abrir Script', filetypes=(('Python Files',"*.py"), ('Pythonw Files',"*.pyw")))
	elif mode == 'save':
		file_path = filedialog.asksaveasfilename(title='Guardar Script', filetypes=(('Python Files',"*.py"), ('Pythonw Files',"*.pyw")))


	if file_path and mode == 'open':
		try: # Intenta abrir el archivo de la forma normal
			with open(file_path) as file:
				src = file.read()
				open(resource_path('www/frame.py'), 'w').close()
				eel.client_load_file(src)
		except Exception: # Intenta abrirlo para todas las codificaciones
			for enc in all_encodings():
				try:
					with open(file_path, encoding=enc) as file:
						src = file.read()
						open(resource_path('www/frame.py'), 'w').close()
						eel.client_load_file(src)
						break
				except Exception:
					pass
	elif file_path and mode == 'save':
		src = eel.client_save_file()()
		if not file_path.lower().endswith('.py'):
			file_path += '.py'
		with open(file_path, 'w') as file:
			file.write(src)
			eel.success_notify('Archivo Guardado')

	if file_path:
		eel.window_file_path(file_path)

	eel.switch_buttons()
	#pyautogui.click()



@eel.expose
def sobreescribir_archivo(file_path, src):
	with open(file_path, 'w') as file:
		file.write(src)


@eel.expose
def sobreescribir_framepy(src):
	with open(resource_path('www/frame.py'), 'w') as frame:
		frame.write(src)



open(resource_path('www/frame.py'), 'w').close()



flags = ['--disable-extensions']
#flags = ['--user-data-dir=%s'%(os.getcwd()+'\\__userDataDir__'), '--disable-extensions']
#flags = ['--user-data-dir=%s'%'C:\\__tecnobillo_UDD__\\__brython_editor__', '--disable-extensions', '--start-fullscreen']
web_app_options = dict(
	mode='chrome-app',
	port=localhost_free_port(),
	chromeFlags=flags,
	)


eel.start('brython_desktop_editor.html', host='localhost', mode='chrome', options=web_app_options, position=(0,0), size=pyautogui.size())
