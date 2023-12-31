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

    host = '128.0.0.4'
    port = 81
    

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        html = "<h1>Movie for you</h1>"
        # Connect to the server
        client_socket.connect((host, port))
        

        # Send data to the server
        message = "2"
        client_socket.sendall(message.encode('utf-8'))

        # Receive data from the server
        
        received_data = b''
        while True:
            partial_data = client_socket.recv(1024)
            if not partial_data:
                break
            received_data += partial_data

        # Decode the received data
        decoded_data = received_data.decode('utf-8')

        # Split the received data based on the colon
        recommended_movie, recommended_tags = decoded_data.strip().split(':')

        # Now you can use the values as needed
        print("Recommended Movie:", recommended_movie)
        for tag in recommended_movie:
            html = html + '<h3>'+recommended_movie[tag]+'<h3>'
        
        client_socket.close()
    except Exception as e:
        client_socket.close()
        print(f"Error: {e}")

    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed")
    # Construct the HTML string
    client_socket.close()
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
