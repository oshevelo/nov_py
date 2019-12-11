class PC:
	def __init__(self,brand,model,serial,description):
		self.brand=brand;
		self.model=model;
		self.serial=serial;
		self.description=description
	def start(self):
		print ('PC is Booting up!')

class Components(PC):
	def __init__(self,brand,model,serial,description):
		super().__init__(brand,model,serial,description)
		
class Hardware(Components):
	def __init__(self,brand,model,serial,description,voltage,status):
		super().__init__(brand,model,serial,description)
		self.voltage=voltage;
		self.status=status
	
class South_Bridge(Hardware):
	def __init__(self,brand,model,serial,description,voltage,status,version):
		super().__init__(brand,model,serial,description,voltage,status)
		self.version=version

class North_Bridge(Hardware):
	def __init__(self,brand,model,serial,description,voltage,status,memory):
		super().__init__(brand,model,serial,description,voltage,status)
		self.memory=memory

class VideoCard(North_Bridge):
	def __init__(self,brand,model,serial,description,voltage,status,memory,driver,glversion):
		super().__init__(brand,model,serial,description,voltage,status)
		self.driver=driver;
		self.glversion=glversion

class Processor(North_Bridge):
	def __init__(self,brand,model,serial,description,voltage,status,memory,frequency,socket):
		super().__init__(brand,model,serial,description,voltage,status)
		self.frequency=frequency;
		self.socket=socket

class SATA(North_Bridge):
	def __init__(self,brand,model,serial,description,voltage,status,memory,isSSD):
		super().__init__(brand,model,serial,description,voltage,status)
		self.isSSD=isSSD

class USB(South_Bridge):
	def __init__(self,brand,model,serial,description,voltage,status,version,memory):
		super().__init__(brand,model,serial,description,voltage,status,version)
		self.memory=memory

class Multicontroller(Hardware):
	def __init__(self,brand,model,serial,description,voltage,status,isOn):
		super().__init__(brand,model,serial,description)
		self.isOn=isOn

class Software(Components):
	def __init__(self,brand,model,serial,description,version):
		super().__init__(brand,model,serial,description)
		self.bersion=version	

class OS(Software):
	def __init__(self,brand,model,serial,description,version,isBooted):
		super().__init__(brand,model,serial,description,version)
		self.isBooted=isBooted
class OtherSoftware(Software):
	def __init__(self,brand,model,serial,description,version,isPresented):
		super().__init__(brand,model,serial,description,version)
		self.isPresented=isPresented


















Videocard=North_Bridge('asus','model','serial','description','voltage','status','2gb')
print(Videocard.brand,Videocard.model,Videocard.memory)

Usb=South_Bridge('brand','model','serial','description','voltage','status','version')
print(Usb.brand,Usb.model,Usb.status)

pc=PC('brand','model','serial','description')

pc.start()
