import json
from PIL import Image
import streamlit as st
import time
import paho.mqtt.client as paho
values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato se publicó \n")
    pass

def on_message(client, userdata, message):
	@@ -21,28 +21,30 @@ def on_message(client, userdata, message):

broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("MiguelMercadoS")
client1.on_message = on_message



st.title("Miguel's Smart House")
st.subheader("Activa con los botones")
st.write(' ')
st.subheader("Oprime los botones ON u OFF para que las luces se enciendan o se apaguen.")

col1, col2 = st.columns(2)
with col1:

    image = Image.open('turn_on.png')
    st.image(image, width=100)
    if st.button('ON'):
        act1="ON"
        client1= paho.Client("MiguelMercadoS")                           
        client1.on_publish = on_publish                          
        client1.connect(broker,port)  
        message =json.dumps({"Act1":act1})
        ret= client1.publish("Luces", message)

        #client1.subscribe("Sensores")

	@@ -51,37 +53,38 @@ def on_message(client, userdata, message):
        st.write('')

with col2:         
    image = Image.open('turn_off.png')

    st.image(image, width=100)
    if st.button('OFF'):
        act1="OFF"
        client1= paho.Client("MiguelMercadoS")                           
        client1.on_publish = on_publish                          
        client1.connect(broker,port)  
        message =json.dumps({"Act1":act1})
        ret= client1.publish("Luces", message)

    else:
        st.write('')

st.divider()     
image = Image.open('opendoor.png')

st.image(image, width=150)

st.subheader("Puedes deslizar para que la puerta se abra o se cierre.")

values = st.slider('',0.0, 100.0)
st.write('Apertura:', values)

if st.button('Ejecutar acción'):
    client1= paho.Client("MiguelMercadoS")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": float(values)})
    ret= client1.publish("Door", message)


else:
    st.write('')
