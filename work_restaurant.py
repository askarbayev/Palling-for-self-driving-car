from POP import POP

# Bindings
work = "WORK"
restaurant = "RESTAURANT"
sm = "Summer Street"
av = "Atlantic Avenue"
ct = "Central Street"


class InitState:
	action = "Start"
	precond = None
	effect = [["At", work]]

	def __repr__(self):
		return '(' + self.action + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class GoalState:
	def __init__(self):
		self.action = "Finish"
		self.precond = [["At", restaurant]]
		self.effect = None

	def __repr__(self):
		return '(' + self.action + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'


class ActionQ:
	action = ["TurnFromTo", work, sm]
	precond = [["At", work]]
	effect = [[False, "At", work], ["At", sm]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class ActionW:
	action = ["DriveTo", av]
	precond = [["At", sm]]
	effect = [["AtCorner", sm, av], [False, "At", sm]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class ActionR:
	action = ["DriveTo", ct]
	precond = [["At", av]]
	effect = [["AtCorner", av, ct], [False, "At", av]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class ActionT:
	action = ["DriveTo", restaurant]
	precond = [["At", ct]]
	effect = [["At", restaurant], [False, "At", ct]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class ActionE:
	action = ["TurnFromTo", sm, av]
	precond = [["AtCorner", sm, av]]
	effect = [[False, "AtCorner", sm, av], ["At", av]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

class ActionY:
	action = ["TurnFromTo", av, ct]
	precond = [["AtCorner", av, ct]]
	effect = [[False, "AtCorner", av, ct], ["At", ct]]

	def __repr__(self):
		return '(Action: ' + str(self.action) + ', Precond: '+ str(self.precond) +', Effect: '+ str(self.effect) + ')'

init = InitState()
goal = GoalState()
operators = [ActionQ(), ActionE(), ActionW(), ActionT(), ActionR(), ActionY()]

def total_order(casual_links, current_step, result):

	next_step = None
	for link in casual_links:
		if link[0] == current_step:
			result.append(link[1])
			next_step = link[1]
			break
	if next_step is None: return
	total_order(casual_links, next_step, result)

