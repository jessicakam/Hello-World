#!/usr/bin/env python

def main():
	'''
	4/4/15 - split bill and add tax and tip
	*solved 5/7/15 - 2 extra "("
	first one: simple calc
	second one: more complex
	'''
# starting question
	type_of_meal = str(raw_input("Is the cost different per person?\nType Y or N\n"))
	if type_of_meal == "Y" or "y":
		diff_cost()
	else:
		same_cost()

def diff_cost():
# if everyone's meal cost a different amount
	
	#ask for total cost of bill
	bill_total = float(raw_input ("How much is the total bill, including tax?\n"))
	
	#ask for total number of people
	people_total = int(raw_input("How many people are splitting the bill?\n"))
	
	#ask and store names of people
	person = 1
	person_list = []	#make empty list
	while person <= people_total:
		 temporary_name = raw_input("What is the name of person " + str(person) + "?\n")
		 person_list.append(temporary_name)
		 person += 1

	#ask for costs of each person's meal
	meal_number = 1
	cost_list = []
	while meal_number <= people_total:
		temporary_meal = float(raw_input("What is the cost of" + person_list[meal_number - 1] + "\'s meal?\n"))
		cost_list.append(temporary_meal)
		meal_number += 1

	#ask for amount of tax listed
	tax_number = 1
	tax_list = []
	total_tax = float(raw_input("What is the tax amount listed on the bill?\n"))
	while tax_number <= people_total:
		tax_list.append(total_tax * cost_list[tax_number - 1] / bill_total)
		tax_number += 1

	#store totals
	place = 1
	final_cost = []
	for index, item in enumerate(cost_list):
		if people_total >= 10.00:
			final_cost.append(item * 1.18 + tax_list[place - 1])
			place += 1 #why error here!! - extra (right before it!)
		else:
			final_cost.append(item * 1.15 + tax_list[place -1])
			place += 1

	#print out name and totals owed
	person = 1
	for index, item in enumerate(person_list):
		print str(person_list[person - 1]) + "owes $" + str(final_cost[person - 1])
		person += 1

def same_cost():
	# if everyone's meal cost the same amount
	
	#ask for total cost of bill
	bill_total = float(raw_input ("How much is the total bill, including tax?\n"))
	
	#ask for total number of people
	people_total = float(raw_input ("How many people are splitting the bill?\n"))
	
	#split and add tax accordingly
	if people_total >= 10.00:
		print "Each person pays $" + str(bill_total * 1.18 / people_total)
	else:
		print "Each person pays $" + str(bill_total * 1.15 / people_total)



if __name__ == '__main__':
	main()
