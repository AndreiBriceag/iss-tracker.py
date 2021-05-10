import requests
import time
import sys

r = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
if not r.status_code in (200, 202):
    sys.exit(-1)

# Only if the status code was 200 or 202, will this code be executed.
resp = r.json()
iss_latitude = resp['latitude']
iss_longitude = resp['longitude']
iss_altitude = resp['altitude']
iss_velocity = resp['velocity']

def get_iss_data():
    iss_api = 'https://api.wheretheiss.at/v1/satellites/25544'
    request = requests.get(iss_api).json()

    print(f'''
        ---------------------------
        Real-time ISS Location:
        ---------------------------
        Altitude: {request['altitude']}
        Latitude: {request['latitude']}
        Longitude: {request['longitude']}
        Velocity (KM/H): {request['velocity']}
        Velocity (MPH): {request['velocity'] / 1.60934}
        ---------------------------
        ''')


def iss_current_data():
    for i in range(3):
        get_iss_data()
        time.sleep(3)


iss_current_data()
