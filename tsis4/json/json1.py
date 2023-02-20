import json

x = open(r'C:\Users\Zhkai\Desktop\pyp\GitHub\pp2-22BD030547\tsis4\json\imdata.json')
y = json.load(x)

print('''=======================================================================================
DN                                                 Description           Speed    MTU" 
-------------------------------------------------- --------------------  ------  ------''')

imdata = y["imdata"]
for i in imdata:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0:51} {1:20} {2:8} {3:6}".format(dn,descr,speed,mtu))