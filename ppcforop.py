import numpy as np
import matplotlib.pyplot as plt

STAN_TIME = 8 
OVER_TIME = 11

NURSE = {1:1, 2:1, 3:1, 4:1, 5:1, 8:2, 9:2, 6:3, 7:4}


class Operation:
	def __init__(self, index, optype, oplength):
		self.i = index
		self.t = optype
		self.l = oplength
		self.o = False    #o for over time

class Room:
	def __init__(self, index):
		self.index = index
		self.oplist = []
		self.optypelist = [0] * 10
		self.totaltime = 0
		self.overwork = False

def printroomlist(roomlist):
	for i in range(12):
		print("Room index: {}".format(i))
		print("Operation order: {}".format(roomlist[i].oplist[::-1]))
		print("Operation type sum: {}".format(sum(roomlist[i].optypelist)))
		print("Total work time: {} hours".format(roomlist[i].totaltime))
		print("Over work: {}".format(roomlist[i].overwork))
		print()

def plotroomlist(roomlist, oplist):
	height = 16
	interval = 4
	colors = ["brown", "red", "yellow", "blue", "green"]
	x_label = "time (hours)"

	ax = plt.subplot()
	labels = []
	count = 0
	for i in range(12):
		labels.append("Room " + str(i))
		totaltime = 0
		for j in roomlist[i].oplist[::-1]:
			ax.broken_barh([(totaltime, oplist[j].l)], ((height+interval)*i + \
				interval, height), facecolors=colors[NURSE[oplist[j].t]])
			totaltime += oplist[j].l
	ax.set_ylim(0, (height+interval)*len(labels)+interval)
	ax.set_xlim(0, 11)
	ax.set_xlabel(x_label)
	ax.set_yticks(range(interval+int(height/2), (height+interval)*len(labels), (height+interval))) 
	ax.set_yticklabels(labels)
	plt.show()

def printdebug(roomlist):
	print("time:", [item.totaltime for item in roomlist])
	print("type:", [sum(item.optypelist) for item in roomlist])

def checktypenum(room, operation):
	room.optypelist[operation.t] = 1
	if (sum(room.optypelist) > 3):
		room.optypelist[operation.t] = 0
		return False
	else:
		return True
# Day 1
oplist1 = [Operation(0, 1, 1.75), Operation(1, 1, 1.5), Operation(2, 6, 3.5), Operation(3, 6, 3), Operation(4, 6, 3),
	Operation(5, 6, 2.42), Operation(6, 6, 6), Operation(7, 6, 2), Operation(8, 6, 3.5), Operation(9, 6, 2.75),
	Operation(10, 4, 2.75), Operation(11, 4, 1.83), Operation(12, 4, 5.25), Operation(13, 4, 2.75), Operation(14, 4, 2.75), 
	Operation(15, 4, 1.83), Operation(16, 4, 3.25), Operation(17, 4, 1.83), Operation(18, 5, 4.42), Operation(19, 5, 3), 
	Operation(20, 5, 3.17), Operation(21, 5, 4.25), Operation(22, 5, 4.33), Operation(23, 5, 3.67), Operation(24, 5, 2.92), 
	Operation(25, 5, 2.17), Operation(26, 5, 3.33), Operation(27, 5, 2), Operation(28, 3, 0.67), Operation(29, 7, 4.08), 
	Operation(30, 7, 2.25), Operation(31, 7, 2.25), Operation(32, 8, 5.25), Operation(33, 8, 6), Operation(34, 8, 6),
	Operation(35, 8, 5.5), Operation(36, 8, 4.75), Operation(37, 9, 5)]
# Day 2
# oplist1 = [Operation(0, 1, 1.75), Operation(1, 6, 3.67), Operation(2, 6, 2), Operation(3, 6, 4.5), Operation(4, 6, 3.5), Operation(5, 6, 3.5),
# 	Operation(6, 6, 4.25), Operation(7, 6, 4.5), Operation(8, 6, 3.5), Operation(9, 6, 3.5), Operation(10, 6, 3.5), Operation(11, 4, 3.92), Operation(12, 5, 4.5),
# 	Operation(13, 5, 0.67), Operation(14, 5, 1.5), Operation(15, 5, 4.5), Operation(16, 5, 2.83), Operation(17, 5, 3.17), Operation(18, 5, 4.25), Operation(19, 5, 3.92),
# 	Operation(20, 5, 5), Operation(21, 5, 4.17), Operation(22, 5, 3), Operation(23, 5, 5.75), Operation(24, 5, 3), Operation(25, 3, 0.33), Operation(26, 3, 0.33),
# 	Operation(27, 7, 4.67), Operation(28, 7, 1.92), Operation(29, 7, 2.17), Operation(30, 7, 2.5), Operation(31, 7, 1.92), Operation(32, 8, 9)]
# Day 3
# oplist1 = []
# count = 0
# for i in [2.5, 5, 3.75, 4, 5, 5, 6.67, 1.33, 2.17, 3.5, 2, 3.58, 3.5]:
# 	oplist1.append(Operation(count, 6, i))
# 	count += 1
# for i in [1.75, 2, 2, 1.75, 3.25, 4.5, 1.75, 1.75]:
# 	oplist1.append(Operation(count, 4, i))
# 	count += 1
# for i in [4.25, 4, 3.67, 5.5, 2.42]:
# 	oplist1.append(Operation(count, 5, i))
# 	count += 1
# oplist1.append(Operation(26, 3, 2.5))
# oplist1.append(Operation(27, 3, 0.75))
# oplist1.append(Operation(28, 7, 2.17))
# oplist1.append(Operation(29, 8, 5.75))
# oplist1.append(Operation(30, 8, 4.58))
# oplist1.append(Operation(31, 8, 6))
# oplist1.append(Operation(32, 8, 6.17))
# Day 4
# oplist1 = []
# count = 0
# for i in [1.5, 1.75, 1.75, 4.5, 4, 1.83, 2.76, 2.72, 3]:
# 	oplist1.append(Operation(count, 6, i))
# 	count += 1
# for i in [2, 2, 4.17, 2.25, 3.5, 1.92, 2, 2]:
# 	oplist1.append(Operation(count, 4, i))
# 	count += 1
# for i in [3.17, 5, 2, 3.25, 4.5, 4.33]:
# 	oplist1.append(Operation(count, 5, i))
# 	count += 1
# oplist1.append(Operation(23, 3, 0.75))
# count += 1
# for i in [5, 2, 3.25, 3.25, 5, 2]:
# 	oplist1.append(Operation(count, 7, i))
# 	count += 1
# oplist1.append(Operation(30, 8, 5.17))
# Day 5
# oplist1 = []
# count = 0
# for i in [1.5, 1, 1, 1.75, 2]:
# 	oplist1.append(Operation(count, 1, i))
# 	count += 1
# for i in [4.67, 4.67]:
# 	oplist1.append(Operation(count, 2, i))
# 	count += 1
# for i in [3, 3, 1.92, 1.58]:
# 	oplist1.append(Operation(count, 6, i))
# 	count += 1
# for i in [2]:
# 	oplist1.append(Operation(count, 4, i))
# 	count += 1
# for i in [4.5, 4.83, 1.83, 3.5]:
# 	oplist1.append(Operation(count, 5, i))
# 	count += 1
# oplist1.append(Operation(16, 3, 1.67))
# count += 1
# for i in [2.92, 3, 2.67, 2.67, 5, 2.92, 3, 4.5]:
# 	oplist1.append(Operation(count, 7, i))
# 	count += 1
# oplist1.append(Operation(25, 9, 6))


oplist1_sorted = sorted(oplist1, key=lambda item:item.l, reverse=True)
oplist1_sorted_index = [item.i for item in oplist1_sorted]

roomlist1 = [Room(0), Room(1), Room(2), Room(3), Room(4), Room(5), Room(6), Room(7), Room(8), Room(9), Room(10), Room(11)]
roomlist1_sorted = sorted(roomlist1, key=lambda item:item.totaltime)
roomlist1_sorted_index = [item.index for item in roomlist1_sorted]

prev_index = 0
for i in oplist1_sorted_index:
	if (roomlist1[prev_index].totaltime + oplist1[i].l <= 11 and \
		checktypenum(roomlist1[prev_index], oplist1[i])):
		roomlist1[prev_index].oplist.append(i)
		roomlist1[prev_index].totaltime += oplist1[i].l
		roomlist1[prev_index].optypelist[oplist1[i].t] = 1

		roomlist1_sorted = sorted(roomlist1, key=lambda item:item.totaltime, reverse=True)
		roomlist1_sorted_index = [item.index for item in roomlist1_sorted]

	else:
		strat_index = 0
		for _ in range(12):
			if (roomlist1[roomlist1_sorted_index[strat_index]].optypelist[oplist1[i].t] == 0):
				roomlist1[roomlist1_sorted_index[strat_index]].optypelist[oplist1[i].t] = 1
				prev_zero = True
			else:
				prev_zero = False
			
			if (sum(roomlist1[roomlist1_sorted_index[strat_index]].optypelist) > 3 or \
				roomlist1[roomlist1_sorted_index[strat_index]].totaltime + oplist1[i].l > 11):
			    if (prev_zero):
			    	roomlist1[roomlist1_sorted_index[strat_index]].optypelist[oplist1[i].t] = 0
			    strat_index += 1
			else:
				break
		roomlist1[roomlist1_sorted_index[strat_index]].oplist.append(i)
		roomlist1[roomlist1_sorted_index[strat_index]].totaltime += oplist1[i].l

		roomlist1_sorted = sorted(roomlist1, key=lambda item:item.totaltime, reverse=True)
		roomlist1_sorted_index = [item.index for item in roomlist1_sorted]

		prev_index = roomlist1_sorted_index[strat_index]

	print("step {}".format(i))
	printdebug(roomlist1)

roomlist1[8].oplist = [3, 19, 4, 7]
roomlist1[3].oplist = [12, 35]
roomlist1[10].oplist = [13, 14, 30, 5]

# roomlist1[3].oplist = [25, 26,  30, 3]
# roomlist1[5].oplist = [29, 28, 15]
# roomlist1[6].oplist = [18, 6]
# roomlist1[8].oplist = [19, 11, 2]

# roomlist1[9].oplist = [10, 0, 22, 16]
# roomlist1[3].oplist = [29, 28]

# roomlist1[8].oplist = [17, 8]
# roomlist1[9].oplist = [5, 6, 7]

# roomlist1[2].oplist = [6]
# roomlist1[4].oplist = [24, 15]
# roomlist1[5].oplist = [7, 8]
# roomlist1[8].oplist = [19, 20, 4]
# roomlist1[9].oplist = [11, 9]
# roomlist1[7].oplist = [22, 5]

for i in range(12):
	roomlist1[i].totaltime = 0
	for j in roomlist1[i].oplist:
		roomlist1[i].totaltime += oplist1[j].l
		if (roomlist1[i].totaltime > STAN_TIME):
			oplist1[j].o = True
for i in range(12):
	if (roomlist1[i].totaltime > STAN_TIME):
		roomlist1[i].overwork = True
printroomlist(roomlist1)
plotroomlist(roomlist1, oplist1)
total_delay = 0
for i in range(len(oplist1)):
	if (oplist1[i].o):
		total_delay += 1
print("Total delay num: ", total_delay)