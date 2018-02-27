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
c.drop_database("heySui")
nasa = c["heySui"]["nasa"]

json = "https://data.nasa.gov/resource/2vr3-k9wn.json"

def retrieve_data(url):
    data = requests.get(url)
    d = data.json()
    # print d
    return d

#finds all with hmag < mag
def from_hmag(mag):
    qd = { "h_mag" : {"$lt" : mag }}
    return nasa.find(qd)

#finds all in specified class
def from_class(oclass):
    qd = { "orbit_class" : oclass}
    return nasa.find(qd)

#all in a specified orbit class with period <= iperiod
def from_class_period(oclass, iperiod):
    try:
        iperiod = int(iperiod)
        qd = { "$and" : [ { "orbit_class" : oclass }, { "period_yr" : {"$lte" : iperiod } } ] }
        return nasa.find(qd)
    except:
        return None

#all in a specified orbit class and a moid_au <= imoid
#score must be inputted as int, not a string!
def from_class_moid(oclass, imoid):
    try:
        imoid = int(imoid)
        qd = { "$and" : [ { "orbit_class" : oclass }, { "moid_au" : {"$lte" : imoid } } ] }
        return nasa.find(qd)
    except:
        return None

#the "something clever"
#Usually people want to find when something was discovered
def from_discovery(discovery):
    qd = {"discovery_date" : {"$lte" : discovery}}
    return nasa.find(qd)

#modular design ftw
def loop_print(cursor):
    for i in cursor:
        print i

def process():
    nasa_dict = retrieve_data(json)
    for i in nasa_dict:
        #print i
        #print repr(i["h_mag"])
        try:
            try:
                i["h_mag"] = float(i["h_mag"])
                print "yay!"
            except:
                pass
            try:
                i["q_au_2"] = float(i["q_au_2"])
            except:
                pass
            try:
                i["period_yr"] = float(i["period_yr"])
            except:
                pass
            i["i_deg"] = float(i["i_deg"])
            i["moid_au"] = float(i["moid_au"])
            i["q_au_1"] = float(i["q_au_1"])
        except:
            pass
    return nasa_dict

# function calls
def main():
    nasa_dict = retrieve_data(json)
    dict = process()
    nasa.insert_many(dict)

    # loop_print(from_hmag(3))
    # loop_print(from_class_moid('Apollo', 2))
    # loop_print(from_class("Apollo"))
    # loop_print(from_class_period("Apollo", 3))
    # #print "3" < "12"

if __name__ == "__main__":
    main()
