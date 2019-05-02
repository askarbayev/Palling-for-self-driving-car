
class POP:

	def __init__(self, init, goal, operators):
		self.init = init
		self.goal = goal
		self.operators = operators
		
	def make_initial_plan(self, init, goal):
		orderings = [[init, goal]]
		casual_links = []
		return orderings, casual_links

	def select_sub_goal(self, plan):
		steps = plan[1]
		if not steps:
			return plan[0][0][1], plan[0][0][1].precond

		i = len(steps) - 1
		while i >= 0:

			temp_links = steps[i]
			link_before = temp_links[0]
			found = False
			for step_next in range(i):
				if link_before == steps[step_next][1]: 
					found = True
					break
			if found == False: return link_before, link_before.precond
			i -= 1
		return None


	def choose_operator(self, plan, operators, S_need, preconds):

		S_add = None			
		for operator in operators:
			found = True
			for precond in preconds:
				if precond not in operator.effect:
					found = False
					break
			if found: 
				S_add = operator
				break
		if S_add is not None:
			plan[0].append([S_add, S_need])
			plan[1].append([S_add, S_need])
		elif self.init.effect == preconds:
			plan[0].append([self.init, S_need])
			plan[1].append([self.init, S_need])

	def is_solution(self, plan):
		casual_links = plan[1]
		if not casual_links:
			return False
		length = len(casual_links) - 1

		for link in casual_links:
			link_before = link[0]
			if link_before.precond is None: continue
			found = False
			for link2 in casual_links:
				if link_before == link2[1]: 
					found = True
					break
			if found == False: return False
		return True

	def resolve_threats(self, plan):

		casual_links = plan[1]
		for link in casual_links:
			for link2 in casual_links:
				if link == link2: continue
				if link[1] == link2[1]:
					#Demotion
					if link[0].effect != link2[1].precond:
						plan[0].append([link[0], link2[0]])

					elif link2[0].effect != link[1].precond:
						plan[0].append([link2[0], link[0]])


	def pop(self):

		plan = self.make_initial_plan(self.init, self.goal)
		while True:
			if self.is_solution(plan): return plan
			S_need, preconds = self.select_sub_goal(plan)
			self.choose_operator(plan, self.operators, S_need, preconds)
			self.resolve_threats(plan)

		return plan

	





		

	
		