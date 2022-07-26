from cv2 import inRange
import pandas as pd
from datetime import datetime
import base64
from flask import Flask, request
app = Flask(__name__)

#Tabel 0 - Detail Nosi
detail_kiriman = 0
column_Detail = 0
column_vDetail = 1
#Tabel 1 - Foto dan Ttd
foto_ttd = 1
#Tabel 2 - history
history = 2
column_date  = 0
column_desc = 1

array_date_history = []
array_desc_history = []

@app.route("/lacak",methods=['POST'])

def createapi():
    # a Python object (dict):
    #Data about Cricket World cup

    message = request.form["connote"]
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    connote = base64_bytes.decode('ascii')
    print(connote)
    URL = "https://pid.posindonesia.co.id/lacak/admin/detail_lacak_banyak.php?id="+connote+"%3D"
    tables = pd.read_html(URL)
    df = tables[detail_kiriman]
    df2 = tables[history]
    df.head()
    
    xas =0

    data=""
    for xas in range(len(df[column_Detail])):
        if xas == 0: 
            data = '{}"{}":"{}"'.format(data,df[column_Detail][xas],str(df[column_vDetail][xas]))
        else :
            data = '{} ,"{}":"{}"'.format(data,df[column_Detail][xas],str(df[column_vDetail][xas]))
        #data = data + df[column_Detail][xas]  + " : "  + str(df[column_vDetail][xas])  +" , "
        xas=xas+1

    xas =0    
    datahisto=""
    for xas in range(len(df2[column_date])):
        if xas == 0: 
            datahisto = '{}"{}":"{}"'.format(datahisto,df2[column_date][xas],str(df2[column_desc][xas]))
        else :
            datahisto = '{} ,"{}":"{}"'.format(datahisto,df2[column_date][xas],str(df2[column_desc][xas]))
        #data = data + df[column_Detail][xas]  + " : "  + str(df[column_vDetail][xas])  +" , "
        xas=xas+1
    #x = {data}
    #print(x)
    #data = '{' + data +'}'
    #print(data)
    datahisto = '{' + datahisto +'}'
    print(datahisto)

    x = '{' + data + ',"riwayat":' + datahisto +'}'
    return x,200


@app.route("/",methods=['get'])
def cek():
    return "sip"

if __name__ == "__main__":
    app.run(debug=True, port=5000)