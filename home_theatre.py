from POP import POP

# Bindings
home = "HOME"
theatre = "THEATRE"
st = "Sant Marys Street"
bc = "Beacon Street"
sm = "Summer Street"



class InitState:
	action = "Start"
	precond = None
	effect = [["At", home]]

	def __repr__(self):
		return '(' + self.action + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class GoalState:
	def __init__(self):
		self.action = "Finish"
		self.precond = [["At", theatre]]
		self.effect = None

	def __repr__(self):
		return '(' + self.action + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'
		

class ActionQ:
	action = ["TurnFromTo", home, st]
	precond = [["At", home]]
	effect = [[False, "At", home], ["At", st]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class ActionW:
	action = ["DriveTo", bc]
	precond = [["At", st]]
	effect = [["AtCorner", st, bc], [False, "At", st]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class ActionY:
	action = ["TurnFromTo", bc, sm]
	precond = [["AtCorner", bc, sm]]
	effect = [[False, "AtCorner", bc, sm], ["At", sm]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'


class ActionR:
	action = ["DriveTo", sm]
	precond = [["At", bc]]
	effect = [["AtCorner", bc, sm], [False, "At", bc]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'


class ActionT:
	action = ["DriveTo", theatre]
	precond = [["At", sm]]
	effect = [["At", theatre], [False, "At", sm]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class ActionE:
	action = ["TurnFromTo", st, bc]
	precond = [["AtCorner", st, bc]]
	effect = [[False, "AtCorner", st, bc], ["At", bc]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'


init = InitState()
goal = GoalState()
operators = [ActionW(), ActionT(), ActionQ(), ActionY(), ActionE(), ActionR()]

def total_order(casual_links, current_step, result):

	next_step = None
	for link in casual_links:
		if link[0] == current_step:
			result.append(link[1])
			next_step = link[1]
			break
	if next_step is None: return
	total_order(casual_links, next_step, result)




