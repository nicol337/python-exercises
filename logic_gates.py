class LogicGate:
	def __init__(self,name):
		self.label = name
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGatLogic()
		return self.getOutput