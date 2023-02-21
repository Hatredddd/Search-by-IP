import requests
import folium


def get_info_by_ip(ip):
    try:
        response=requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data={
            '[IP]':response.get('query'),
            '[INT prov]':response.get('isp'),
            '[Org]':response.get('org'),
            '[Country]':response.get('country'),
            '[Region name]':response.get('regionName'),
            '[City]':response.get('city'),
            '[ZIP]':response.get('zip'),
            '[LAT]':response.get('lat'),
            '[LON]':response.get('lon')
        }
        for k,v in data.items():
            print(f'{k}:{v}')

        area=folium.Map(location=[response.get('lat'),response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('Check connection')

def main():
    ip=input()
    get_info_by_ip(ip=ip)

if __name__=='__main__':
    main()