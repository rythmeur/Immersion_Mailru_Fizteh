import numpy as np
import scipy.spatial

a = np.array([6, 3, -5])
b = np.array([-1, 0, 7])

print(np.linalg.norm(a, ord=2) - np.linalg.norm(b, ord=2))
print(scipy.spatial.distance.cdist(a[:, np.newaxis], b[:, np.newaxis], metric='euclidean'))
print(scipy.spatial.distance.cdist(a[np.newaxis, :], b[np.newaxis, :], metric='euclidean'))

import requests
from urllib.request import urlopen
from xml.etree.ElementTree import parse
#response = requests.get("http://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=06/08/2019")
#data = response.content
#print(data)


var_url = urlopen('http://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=06/08/2019')
xmldoc = parse(var_url)
print(xmldoc)
print(xmldoc)