import requests
from bs4 import BeautifulSoup
import streamlit as st

def get_availability(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.find(id="ctl06_data1_lblAhuzotIDStat_0").find_all('img')[0]['src']
    if img ==  '/pics/ParkingIcons/meat.png':
        return "Few places"
    elif img == '/pics/ParkingIcons/male.png':
        return "Parking is full"
    elif img == '/pics/ParkingIcons/panui.png':
        return "Parking is available"


st.title("Parking info")

"Assuta: " + get_availability("http://www.ahuzot.co.il/Parking/ParkingDetails/?ID=122")
"Basel: " + get_availability("http://www.ahuzot.co.il/Parking/ParkingDetails/?ID=3")
"Arlozorov 17: " + get_availability("http://www.ahuzot.co.il/Parking/ParkingDetails/?ID=123")
"HaBima: " + get_availability("http://www.ahuzot.co.il/Parking/ParkingDetails/?ID=94")

# print("Assuta: " + get_availability("http://www.ahuzot.co.il/Parking/ParkingDetails/?ID=122"))
# print("Basel: " + get_availability("http://www.ahuzot.co.il/Parking/ParkingDetails/?ID=3"))
# print("Arlozorov 17: " + get_availability("http://www.ahuzot.co.il/Parking/ParkingDetails/?ID=123"))
