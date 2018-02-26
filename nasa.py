from pymongo import MongoClient
import requests

'''
 Team heySui
 Shannon Lau and Jen Yu
 SoftDev pd7
 K #05: Import/Export Bank
 2018-02-15
'''

c = MongoClient("lisa.stuy.edu")
nasa = c["heySui"]["nasa"]

json = "https://data.nasa.gov/resource/2vr3-k9wn.json"

def retrieve_data(url):
    data = requests.get(url)
    d = data.json()
    # print d
    return d

#finds all with hmag <= mag
def from_hmag(mag):
    qd = { "h_mag" : {"$lte" : mag }}
    return nasa.find(qd)

#finds all in specified class
def from_class(class):
    qd = { "orbit_class" : class}
    return nasa.find(qd)

#all in a specified orbit class with period <= iperiod
def from_class_period(class, iperiod):
    qd = { "$and" : [ { "orbit_class" : class }, { "period_yr" : {"$lte" : iperiod } } ] } 
    return nasa.find(qd)

#all in a specified orbit class and a moid_au <= imoid
#score must be inputted as int, not a string!
def from_class_moid(zip, score):
    qd = { "$and" : [ { "orbit_class" : class }, { "moid_au" : {"$lte" : imoid } } ] } 
    return nasa.find(qd)

#the "something clever"
#Usually people want to find when something was discovered
def from_discovery(discovery):
    qd = {"discovery_date" : {"$lte" : discovery}}
    return nasa.find(qd)

#modular design ftw
def loop_print(cursor):
    for i in cursor:
        print i

#function calls
def main():
    nasa_dict = retrieve_data(json)
    nasa.insert_many(nasa_dict)
    
#run da main
main()
