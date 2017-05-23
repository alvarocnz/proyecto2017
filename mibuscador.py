from sys import argv
import bottle
from bottle import Bottle,route,run,request,template,static_file,redirect,get,post, default_app, response, get, post
import os
import json
import requests



key="3d81dc5d3e3b814c444aedf077d52c1a"
url_base="https://api.flickr.com/services/rest"


@route('/')
def inicio():
	return template('inicio',method='get')


@route('/busqueda',method='post')
def busqueda():
#variables de busqueda de la aplicacion
	nombre=request.forms.get('foto')
	payload={"method":"flickr.photos.search","api_key":key,"text":nombre,"extras":"url_o,url_s","format":"json"}
	p=requests.get(url_base,params=payload)
	lista_url=[]
	codigo_foto=[]
	if p.status_code==200:
		documento = json.loads(p.text[14:-1])
#nos coge la foto
		for n in documento["photos"]["photo"]:
			if n.has_key("url_o"):
				lista_url.append([n['url_s'],n["url_o"]])
#nos coge el propietario
		for m in documento["photos"]["photo"]:
			if m.has_key("id"):
				codigo_foto.append(m['owner'])
				
		return template("resultado.tpl",lista1=lista_url,lista2=codigo_foto)





@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')


run(localhost='0.0.0.0',port=argv[1])



#url de la plantilla --> https://jayj.dk/html5-theme-v2/
