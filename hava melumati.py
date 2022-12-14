import requests
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Tkinter kitabxanasi vasitesile pencere yaradiriq
window = tk.Tk()

# Penceremize olchu veririk
window.geometry("1000x800+400+100")

# Havasini oyrenmek istediyimiz sheher adlarini ingilisce listde yaziriq
cities = ['Baku, Azerbaijan', 'Ganja, Azerbaijan', 'Imishli, Azerbaijan', 'Agdash, Azerbaijan' , 'Barda, Azerbaijan' , 'Fuzuli, Azerbaijan' ,'Lankaran, Azerbaijan', 'Quba, Azerbaijan', 'Shusha, Azerbaijan' , 'Zangilan, Azerbaijan']

# API den gelen datani elave edeceyimiz bosh bir list yaradiriq
data = []

# Sheherlerin datasini bir-bir almaq uchun for dovrunu yaradiriq
for c in cities:
    params = {
    'access_key': '0fda8b31ca36a543ad82b4d620cf2dbe',
    'query': c,
    }

    # Requests kitabxanasi vasitesile API den istifade ederek sheherlerin hava veziyyetinin datasini aliriq
    api_result = requests.get('http://api.weatherstack.com/current', params)
    
    # Ald;gimiz datani JSON formatina ceviririk
    api_response = api_result.json()

    # data adli bosh listimize json formatinda olan datalari elave edirik
    data.append(api_response)

# Pandas kitabxanasinin json_normalize metodu ile json datamizi DataFrame formatinda cedvele cevirik
df = pd.json_normalize(data)

# Tesvir adli bosh list yaradiriq
tesvir = []

# Havani tesvir eden ifadeni list tipinden string tipe kecirib tesvir listine elave edirik
for desc in df['current.weather_descriptions']:
    # Eger data varsa elave edirik
    try:
        tesvir.append(desc[0])
    # Yoxdursa oldugu kimi saxlayiriq
    except:
        tesvir.append(desc)

# Evvelki hava temperaturunun oldugu sutunu yenisi ile evez edirik
df['current.weather_descriptions'] = tesvir

# Yeni bosh bir DataFrame obyekti yaradiriq 
df_yeni = pd.DataFrame()
# Bize lazim olan melumatlari yeni DataFrame - e elave edirik
df_yeni['Ad'] = df['location.name']
df_yeni['Temperatur(C)'] = df['current.temperature']
df_yeni['Tesvir'] = df['current.weather_descriptions']
df_yeni['Buludluluq'] = df['current.cloudcover']

# Eger data yoxdursa sutunu silmek uchun Pandas kitabxanasinindropna metodundan istifade edirik
df_yeni.dropna(how='all', inplace=True)

# Tkinter kitabxanasindan istifade ederek cedvel elementi yaradiriq
table = ttk.Treeview(window, columns=list(df_yeni.columns), show='headings')

# Cedvelin Sutun bashliqlarini ve Sutunlarini cedvele elave edirik
for col in df_yeni.columns:
    table.heading(col, text=col)
    table.column(col, stretch=False, anchor='center')

# DataFrame melumatlarini cedvele elave edirik
for index, row in df_yeni.iterrows():
    table.insert('', 'end', values=list(row))
    
# Cedveli baglayiriq 
table.pack()

# Cedveli csv formatinda yadda saxlayiriq
df_yeni.to_csv('hava_melumati.csv', index=False)

# penceremizi biz baglayana qeder achiq qalmasi uchun mainloop metodunu yaziriq
window.mainloop()