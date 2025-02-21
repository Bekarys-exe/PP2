import json
import os

print(os.getcwd())

file_name = r'C:\Users\Acer\Documents\PP2\Lab_4\json\sample_data.json'

with open(file_name, 'r') as f:
    json_file = json.load(f)

print(type(json_file))


print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("{:-<50} {:-<20} {:-<10} {:-<10}".format("", "", "", ""))

for item in json_file["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    print("{:<50} {:<20} {:<10} {:<10}".format(dn, descr, speed, mtu))

