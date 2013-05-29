import ConfigParser

from dop.client import Client

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

def configSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

clientID = configSectionMap("Access")['clientid']
apiKey = configSectionMap("Access")['apikey']

# print "Client ID: %s, API Key: %s" % (clientID, apiKey)
print "Client ID and API key retrieved."

client = Client(clientID, apiKey)
droplets = client.show_active_droplets()

print "Displaying SSH Key Options:"
sshkeys = client.all_ssh_keys()
for sshkey in sshkeys:
	print sshkey.to_json()

def printOptions():
	print ""
        print "Options:"
        print "1) List Active Droplets"
	print "2) List Available Sizes"
	print "3) List Available Images"
	print "4) List Available Regions"
	print "5) Create Drop"
	print "6) Destroy Drop"
	print "10) Create Downpour"
	print "11) Display Downpour"
	print "12) Destroy Downpour"
        print "q) Quit"
	print ""

def listDroplets():
	droplets = client.show_active_droplets()
	print "Active Droplets: \n"
	for droplet in droplets:
		print droplet.to_json()

def listAvailableSizes():
	sizes = client.sizes()
	for size in sizes:
		print size.to_json()	

def listAvailableImages():
	images = client.images()
	for image in images:
		print image.to_json()

def listAvailableRegions():
	regions = client.regions()
	for region in regions:
		print region.to_json()

def createDrop():
	name = raw_input("Name: ")
	size_id = raw_input("Size: ")
	image_id = raw_input("Image ID: ")
	region_id = raw_input("Region ID: ")
	ssh_key_id = [raw_input("SSH Key ID: ")]
	droplet = client.create_droplet(name, size_id, image_id, region_id, ssh_key_id, virtio=True);
	print droplet.to_json()

def createDownpour():
	number = int(raw_input("Number: "))
	name = raw_input("Name: ")
        size_id = raw_input("Size: ")
        image_id = raw_input("Image ID: ")
        region_id = raw_input("Region ID: ")
	ssh_key_id = raw_input("SSH Key ID: ")
        for i in range(0, number):
		droplet = client.create_droplet("%s%03d" % (name, i), size_id, image_id, region_id, ssh_key_id, virtio=True);
        	print "%d : %s" % (i, droplet.to_json())

def displayDownpour():
	name = raw_input("Name: ")
	number = int(raw_input("Number: "))
	droplets = client.show_active_droplets()
        print "Downpour Droplets: \n"
        for droplet in droplets:
		for i in range (0, number):
			dropname = "%s%03d" % (name, i)
			if dropname == droplet.name:
				print droplet.to_json()

def destroyDownpour():
	name = raw_input("Name: ")
        number = int(raw_input("Number: "))
        droplets = client.show_active_droplets()
        print "Active Droplets: \n"
        for droplet in droplets:
                for i in range (0, number):
                        dropname = "%s%03d" % (name, i)
                        if dropname == droplet.name:
                                print "Destroying %s: " % (droplet.to_json())
				client.destroy_droplet(droplet.id)

def destroyDrop():
	id = raw_input("ID: ")
	data = client.destroy_droplet(id)
	print data

choice = 0

while choice != "q":
	printOptions()
	choice = raw_input("Selection: ")
	if choice == "1":
		listDroplets()
	elif choice == "2":
		listAvailableSizes()
	elif choice == "3":
		listAvailableImages()
	elif choice == "4":
		listAvailableRegions()
	elif choice == "5":
		createDrop()
	elif choice == "6":
		destroyDrop()
	elif choice == "10":
		createDownpour()
	elif choice == "11":
		displayDownpour()
	elif choice == "12":
		destroyDownpour()
