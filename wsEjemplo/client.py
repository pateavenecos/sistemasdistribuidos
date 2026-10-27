from urllib import response
import requests

#response = requests.get("http://localhost:5000/empdb/employee")
#response= requests.get("http://localhost:5000/empdb/employee", data={"id":"101"})
dat={"id":"111111","name":"Pedro Perez P", "title":"engineer"}
response= requests.post("http://142.44.246.12:5000/empdb/employee", json=dat)
print(response.json())

