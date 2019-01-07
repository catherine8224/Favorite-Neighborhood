import folium
import pandas as pd

with open("311_Service_Requests_from_2010_to_Present.csv") as f:
    print(f)
    
file = pd.read_csv("311_Service_Requests_from_2010_to_Present.csv")
#ISO-8859-1")
print(file["Complaint Type"])
NYCMap = folium.Map(location=[40.7719,-73.946997], zoom_start=12)

for index,row in file.iterrows():
    if row["Complaint Type"] == "Noise":
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["Complaint Type"]
        newMarker= folium.Marker([lat,lon], popup=name)
        newMarker.add_to(NYCMap)

NYCMap.save("311Map.html")
