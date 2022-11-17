import obd
port = ""
connection = obd.OBD(port)
print("yeet")
variables = ["SPEED", "COOLANT_TEMP", "MAF", "RPM", "FUEL_TYPE"]
# for variable in variables:
#     cmd = obd.commands.variable
#     response = connection.query(cmd)
#     print(variable+": "+response.value)
print("Before command")
cmd = obd.commands.SPEED
print("After command")
response = connection.query(cmd)
print("After response")
print("Speed: " + response.value)

# class OBD_Communication():
#     import obd
#     connection = obd.OBD()

#     def __init__(self, connection_name):
#         self.port = connection_name
#         self.speed = 0
#         self.coolantTemp = 0
#         self.MAF = 0
#         self.RPM = 1
#         self.gear = 0
#         cmd = obd.commands.FUEL_TYPE
#         self.fuelType = (connection.query(obd.commands.FUEL_TYPE)).value

#     def update_speed(self):
#         cmd = obd.commands.SPEED
#         response = connection.query(cmd)
#         return response.value

#     def update_coolantTemp(self):
#         cmd = obd.commands.COOLANT_TEMP
#         response = connection.query(cmd)
#         return response.value

#     def update_MAF(self):
#         cmd = obd.commands.MAF
#         response = connection.query(cmd)
#         return response.value

#     def update_RPM(self):
#         cmd = obd.commands.RPM
#         response = connection.query(cmd)
#         return response.value
    
#     def update_Gear(self):
#         constant = (self.fetch_RPM() / self.fetch_speed())
#         response = connection.query(cmd)
#         return response.value
    

#     def update_fuelType(self):
#         return self.fuelType

