import requests

# URL API SpaceX
url = 'https://api.spacexdata.com/v4/launches?limit=20'

# Mendapatkan data dari API
response = requests.get(url)
data_list = response.json()[-20:]

# Loop untuk mencetak data pada setiap peluncuran
for data in data_list:
    # Menampilkan data tanggal peluncuran
    launch_date = data['date_utc']

    # Menampilkan nama lengkap launchpad
    launchpad_id = data['launchpad']
    launchpad_url = f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}'
    launchpad_response = requests.get(launchpad_url)
    launchpad_data = launchpad_response.json()
    launchpad_fullname = launchpad_data['full_name']

    # Menampilkan perbedaan dalam km antara hasil geocoding Mapbox untuk launchpad dan posisi SpaceX resmi
    mapbox_url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{launchpad_fullname}.json?access_token=pk.eyJ1IjoiZGFtZXNraXkiLCJhIjoiY2xnMGVrM2huMGdiMjNlcXBodnU3dThydiJ9.7ZrdtOO9JiO40OqGOEKRbQ'
    mapbox_response = requests.get(mapbox_url)
    mapbox_data = mapbox_response.json()
    mapbox_latitude = mapbox_data['features'][0]['center'][1]
    mapbox_longitude = mapbox_data['features'][0]['center'][0]
    spacex_latitude = launchpad_data['latitude']
    spacex_longitude = launchpad_data['longitude']
    diff_latitude_km = abs(mapbox_latitude - spacex_latitude) * 111.32
    diff_longitude_km = abs(mapbox_longitude - spacex_longitude) * 111.32
    print(f'{launch_date}{launchpad_fullname}{diff_latitude_km:.2f} {diff_longitude_km:.2f}')
    