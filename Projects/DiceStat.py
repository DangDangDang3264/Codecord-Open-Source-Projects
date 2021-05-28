import random
import os
from tabulate import tabulate
import matplotlib.pyplot as plt

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return True

cls()

roll_log = []

def printRollLog(roll_log = roll_log):
    cls()
    print(tabulate(roll_log, headers = ["Number of Dice","Size of Dice","Modifier","Value"], tablefmt="pretty"))

def parseText(text):
    number = 0
    size = 0
    modifier = 0
    if text.startswith("d"):
        text1 = text.strip("d")
        if "+" in text:
            text2 = text1.split("+")
            number = 1
            size = int(text2[0])
            modifier = int(text2[1])
        elif "-" in text:
            text2 = text1.split("-")
            number = 1
            size = int(text2[0])
            modifier = -1 * int(text2[1])
        else:
            number = 1
            size = int(text1)
    else:
        text1 = text.split("d")
        if "+" in text1[1]:
            text2 = text1[1].split("+")
            number = int(text1[0])
            size = int(text2[0])
            modifier = int(text2[1])
        elif "-" in text1[1]:
            text2 = text1[1].split("-")
            number = int(text1[0])
            size = int(text2[0])
            modifier = -1 * int(text2[1])
        else:
            number = int(text1[0])
            size = int(text1[1])
    return {"number":number, "size":size, "modifier":modifier}

def rollDice(number, size, modifier):
    value = 0
    for n in range(number):
        value += random.randint(1,size)
    value += modifier
    roll_log.append([number,size,modifier,value])
    return value

def rollDice2(number, size, modifier):
    value = 0
    for n in range(number):
        value += random.randint(1,size)
    value += modifier
    return value

#Depreciated
def getProbabilities(input_list):
    return_dict = dict()
    items = set(input_list)
    for n in items:
        return_dict[n] = input_list.count(n) / len(input_list)
    return return_dict

#Depreciated
def iterateRoll(size, roll):
    new_list = roll
    length = len(new_list) - 1
    check_slot = 0
    run = True
    while run:
        if new_list[check_slot] < size:
            new_list[check_slot] += 1
            run = False
            return new_list
        elif new_list[check_slot] == size and check_slot < length:
            if new_list[check_slot + 1] + 1 > size:
                check_slot += 1
            else:
                new_list[check_slot + 1] += 1
                for i in range(check_slot + 1):
                    new_list[i] = 1
                run = False
                return new_list
        else:
            run = False
            return False

#Depreciated
def rollStat(number, size, modifier=0):
    sums = dict()
    current_roll = [1 for i in range(number)]
    current_sum = sum(current_roll) + modifier
    sums[current_sum] = 1
    run = True
    while run:
        current_roll = iterateRoll(size, current_roll)
        if current_roll == False:
            run = False
        else:
            current_sum = sum(current_roll) + modifier
            if current_sum not in sums:
                sums[current_sum] = 1
            else:
                sums[current_sum] += 1
    sums = dict(sorted(sums.items()))
    total_sum = 0
    for item in sums:
        total_sum += sums[item]
    stats = dict()
    for item in sums:
        stats[item] = sums[item] / total_sum
    return stats

def iterateSumRoll(size, sums):
    new_sums = dict()
    for a in sums:
        for b in [i for i in range(1,size + 1)]:
            if a + b in new_sums:
                new_sums[a + b] += sums[a]
            else:
                new_sums[a + b] = sums[a]
    return new_sums

def rollStat2(number, size, modifier=0):
    sums = dict()
    for i in [i for i in range(1, size + 1)]:
        sums[i] = 1
    for i in range(number - 1):
        sums = iterateSumRoll(size, sums)
    sums = dict(sorted(sums.items()))
    total_sum = 0
    for item in sums:
        total_sum += sums[item]
    stats = dict()
    for item in sums:
        stats[item] = sums[item] / total_sum
    new_stats = dict()
    for item in stats:
        new_stats[item + modifier] = stats[item]
    return new_stats

def rollStatRand(number, size, modifier=0, sample_size=10000):
    sums = dict()
    for i in range(sample_size):
        roll = rollDice2(number, size, modifier)
        if roll in sums:
            sums[roll] += 1
        else:
            sums[roll] = 1
    sums = dict(sorted(sums.items()))
    total_sum = 0
    for item in sums:
        total_sum += sums[item]
    stats = dict()
    for item in sums:
        stats[item] = sums[item] / total_sum
    return stats

def boundsReport(stats, lower_bound, upper_bound=None):
    if upper_bound == None:
        upper_bound = max(stats)
    probability_in_bounds = 0
    for item in stats:
        if item >= lower_bound and item <= upper_bound:
            probability_in_bounds += stats[item]
    probability_out_bounds = 1 - probability_in_bounds
    return {"Probability within bounds":probability_in_bounds, "Probablility without bounds":probability_out_bounds}

def boundsReportQuarters(stats, number, size, modifier):
    bound_low = number + modifier
    bound_high = number * size + modifier
    bound_range = bound_high - bound_low
    bound_Q1 = round(bound_low + (bound_range * (1 / 4)))
    bound_Q2 = round(bound_low + (bound_range * (1 / 2)))
    bound_Q3 = round(bound_low + (bound_range * (3 / 4)))
    prob_below_Q1 = boundsReport(stats, bound_low, bound_Q1)["Probability within bounds"]
    prob_below_Q2 = boundsReport(stats, bound_low, bound_Q2)["Probability within bounds"]
    prob_below_Q3 = boundsReport(stats, bound_low, bound_Q3)["Probability within bounds"]
    prob_above_Q1 = boundsReport(stats, bound_Q1, bound_high)["Probability within bounds"]
    prob_above_Q2 = boundsReport(stats, bound_Q2, bound_high)["Probability within bounds"]
    prob_above_Q3 = boundsReport(stats, bound_Q3, bound_high)["Probability within bounds"]
    prob_between_Q1_Q2 = boundsReport(stats, bound_Q1, bound_Q2)["Probability within bounds"]
    prob_between_Q1_Q3 = boundsReport(stats, bound_Q1, bound_Q3)["Probability within bounds"]
    prob_between_Q2_Q3 = boundsReport(stats, bound_Q2, bound_Q3)["Probability within bounds"]
    return [[bound_low, bound_Q1, bound_Q2, bound_Q3, bound_high],[prob_below_Q1, prob_below_Q2, prob_below_Q3],[prob_above_Q1, prob_above_Q2, prob_above_Q3],[prob_between_Q1_Q2, prob_between_Q1_Q3, prob_between_Q2_Q3]]

def simpleTextUI():
    cls()
    run = True
    while run:
        user_input = input(">>> ")
        if user_input == "exit":
            run = False
        elif user_input == "clear":
            cls()
        elif user_input in ["log","logs"]:
            printRollLog()
        elif user_input.startswith("rollstat rand"):
            text = input("Enter the roll to be analyzed: ")
            sample_size = input("Enter the sample size: ")
            parsed_text = parseText(text)
            stats = rollStatRand(parsed_text["number"], parsed_text["size"], parsed_text["modifier"], int(sample_size))
            for item in stats:
                print(f"{item} - {stats[item] * 100}%")
            brq = boundsReportQuarters(stats, parsed_text["number"], parsed_text["size"], parsed_text["modifier"])
            bound_low, boundQ1, boundQ2, boundQ3, bound_high = brq[0]
            belowQ1, belowQ2, belowQ3 = brq[1]
            aboveQ1, aboveQ2, aboveQ3 = brq[2]
            betweenQ12, betweenQ13, betweenQ23 = brq[3]
            tbl0 = [bound_low, 0, 100]
            tblQ1 = [boundQ1, belowQ1 * 100, aboveQ1 * 100]
            tblQ2 = [boundQ2, belowQ2 * 100, aboveQ2 * 100]
            tblQ3 = [boundQ3, belowQ3 * 100, aboveQ3 * 100]
            tbl1 = [bound_high, 100, 0]
            print(tabulate([tbl0,tblQ1,tblQ2,tblQ3,tbl1], headers=["Bound", "Percent Below", "Percent Above"], tablefmt="pretty"))
            tblQ12 = [boundQ1, boundQ2, betweenQ12 * 100]
            tblQ13 = [boundQ1, boundQ3, betweenQ13 * 100]
            tblQ23 = [boundQ2, boundQ3, betweenQ23 * 100]
            print(tabulate([tblQ12,tblQ13,tblQ23], headers=["Lower Bound", "Upper Bound", "Percent Between"], tablefmt="pretty"))
            xvars = []
            yvars = []
            for i in stats:
                xvars.append(i)
                yvars.append(stats[i] * 100)
            plt.plot(xvars,yvars,'r.')
            plt.show()
        elif user_input.startswith("rollstat"):
            text = input("Enter the roll to be analyzed: ")
            parsed_text = parseText(text)
            stats = rollStat2(parsed_text["number"], parsed_text["size"], parsed_text["modifier"])
            for item in stats:
                print(f"{item} - {stats[item] * 100}%")
            brq = boundsReportQuarters(stats, parsed_text["number"], parsed_text["size"], parsed_text["modifier"])
            bound_low, boundQ1, boundQ2, boundQ3, bound_high = brq[0]
            belowQ1, belowQ2, belowQ3 = brq[1]
            aboveQ1, aboveQ2, aboveQ3 = brq[2]
            betweenQ12, betweenQ13, betweenQ23 = brq[3]
            tbl0 = [bound_low, 0, 100]
            tblQ1 = [boundQ1, belowQ1 * 100, aboveQ1 * 100]
            tblQ2 = [boundQ2, belowQ2 * 100, aboveQ2 * 100]
            tblQ3 = [boundQ3, belowQ3 * 100, aboveQ3 * 100]
            tbl1 = [bound_high, 100, 0]
            print(tabulate([tbl0,tblQ1,tblQ2,tblQ3,tbl1], headers=["Bound", "Percent Below", "Percent Above"], tablefmt="pretty"))
            tblQ12 = [boundQ1, boundQ2, betweenQ12 * 100]
            tblQ13 = [boundQ1, boundQ3, betweenQ13 * 100]
            tblQ23 = [boundQ2, boundQ3, betweenQ23 * 100]
            print(tabulate([tblQ12,tblQ13,tblQ23], headers=["Lower Bound", "Upper Bound", "Percent Between"], tablefmt="pretty"))
            xvars = []
            yvars = []
            for i in stats:
                xvars.append(i)
                yvars.append(stats[i] * 100)
            plt.plot(xvars,yvars,'r.')
            plt.show()
        elif user_input.startswith("roll"):
            text = user_input.strip("roll ")
            parsed_text = parseText(text)
            roll = rollDice(parsed_text["number"],parsed_text["size"],parsed_text["modifier"])
            print(f"Rolled {roll} from {parsed_text['number']}d{parsed_text['size']} + {parsed_text['modifier']}")
        elif user_input in ["help","h"]:
            print("exit - exits the code")
            print("clear - clears the command prompt")
            print("log, logs - prints the roll log")
            print("roll - rolls a dice in the form 'roll [number of dice]d[number of faces][+ or -][modifier]'")
            print("rollstat - runs the rollstat function, optional argument 'rollstat rand' will run a random version of rollstat")
            print("rollstat and rollstat rand use the same 'roll [number of dice]d[number of faces][+ or -][modifier]' structure after executing the command")

simpleTextUI()