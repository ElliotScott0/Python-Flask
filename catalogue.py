from datetime import *
import time
import sys
import socket
import json
import requests
# First we set our credentials

from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash
catalogue_app =Flask(__name__)
catalogue_app.debug = True


@catalogue_app.route('/Video/<video>')
def video_page(video):
    print (video)
    url = 'http://128.0.0.7/myflix/videos?filter={"video.uuid":"'+video+'"}'
    headers = {}
    payload = json.dumps({ })
    print (request.endpoint)
    response = requests.get(url)
    print (url)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])
    jResp = response.json()
    print (type(jResp))
    print (jResp)
    for index in jResp:
        for key in index:
           if (key !="_id"):
              print (index[key])
              for key2 in index[key]:
                  print (key2,index[key][key2])
                  if (key2=="Name"):
                      video=index[key][key2]
                  if (key2=="file"):
                      videofile=index[key][key2]
                  if (key2=="pic"):
                      pic=index[key][key2]
    return render_template('video.html', name=video,file=videofile,pic=pic)

@catalogue_app.route('/cat_page')
def cat_page():
    url = "http://128.0.0.7/myflix/videos"
    headers = {}
    payload = json.dumps({ })

    response = requests.get(url)
    #print (response)
    # exit if status code is not ok
    print (response)
    print (response.status_code)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])
    jResp = response.json()

    url = "http://128.0.0.4"
    port = 80
    params = {2}  # Adjust the parameter as needed

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((url, port))

    # Listen for incoming connections
    server_socket.listen()

    print(f"Listening on {url}:{port}")

    
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    # Send a response back to the client
    response = "2"
    data1 = client_socket.send(response.encode('utf-8'))

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received: {data}")
    print(f"Received: {data1}")


    # Close the connection
    client_socket.close()


    rec = response.json()

    # Construct the HTML string
    html = "<h1>List of Movies</h1>"
    html += "<ul>"
    
    # Loop through movies and add list items to HTML string
    for movie in rec:
        html += f"<li>{data}</li>"

    html += "</ul>"
    html=html+"<h2> Your Videos</h2>"
    for index in jResp:
       #print (json.dumps(index))
       print ("----------------")
       for key in index:

           if (key !="_id"):
              print (index[key])
              for key2 in index[key]:
                  print (key2,index[key][key2])
                  if (key2=="Name"):
                      name=index[key][key2]
                  if (key2=="thumb"):
                      thumb=index[key][key2]
                  if (key2=="uuid"):
                      uuid=index[key][key2]
              html=html+'<h3>'+name+'</h3>'
              ServerIP=request.host.split(':')[0]
              html = html + '<a href="' + url_for('video_page', video=uuid) + '">'
              html=html+'<img src="http://35.246.124.242/pics/'+thumb+'">'
              html=html+"</a>"
              print("=======================")

    return html


if __name__ == '__main__':
    catalogue_app.run(host='0.0.0.0',port="5000")
