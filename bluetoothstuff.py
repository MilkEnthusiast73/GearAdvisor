import bluetooth

target_name = "Jabra Elite 3"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address ", target_address)
else:
    print("could not find target bluetooth device nearby")

#print(bluez._get_available_port(bluetooth.RFCOMM))
port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((target_address, port))

sock.send("hello!!")

sock.close()