import requests

city_name=str(input("enter the city/state name to check: "))
API_key='7063e7845322e30c270f822da6b82a74'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response=requests.get(url)
if response.status_code==200:  
    data = response.json()
    print('weather is :',data['weather'][0]['description'])
    print("Current temperature is:",data['main']['temp'])
    print("Current temperature feels like is:",data['main']['feels_like'])
    print("Current humidity is:",data['main']['humidity'])
else:
    print (f"enter the correct city/state name , {city_name} is not found 🚩")
   
