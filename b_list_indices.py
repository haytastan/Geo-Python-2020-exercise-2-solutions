# Hayati TAŞTAN
#Creating a list
station_names = ['Helsinki Harmaja', 'Helsinki Kaisaniemi', 'Helsinki Kaivopuisto', 'Helsinki Kumpula']
print(station_names)
type(station_names)

#Index values:
print(station_names[0])
print(station_names[1])

#Number of items in a list:
len(station_names)

#Modifying list values:
station_names[0] ='Ankara'
print(station_names[0])

#Data types in lists:
station_name='Helsinki Kaivopuisto'
station_id=132310
station_lat=60.15
station_lon=24.96
station_type='Mareographs'
station_hel_kaivo = [station_name, station_id, station_lat, station_lon, station_type]
print(station_hel_kaivo)
type(station_hel_kaivo)
type(station_hel_kaivo[0])    # The station name
type(station_hel_kaivo[1])    # The FMISID
type(station_hel_kaivo[2])    # The station latitude

#Adding values to lists:
del station_names[0]
print(station_names)

#Removing values from lists:
station_names.append('Helsinki lighthouse')
station_names.append('Helsinki Malmi airfield')
print(station_names)

# The count method counts the number of occurences of a value:
station_names.count('Helsinki Kumpula')    

# The index method gives the index value of an item in a list:
station_names.index('Helsinki Kumpula')  

#Reversing a list:
station_names.reverse()
print(station_names)

#Sorting a list:
station_names.sort()
print(station_names)
