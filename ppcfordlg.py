import matplotlib.pyplot as plt

STAN_TIME = 8 
OVER_TIME = 11

NURSE = {1:1, 2:1, 3:1, 4:1, 5:1, 8:2, 9:2, 6:3, 7:4}

NURSE1_LIST = [6, 5, 4, 3, 2, 1]
NURSE2_LIST = [9, 8, 7]
NURSE3_LIST = [13, 12, 11, 10]
NURSE4_LIST = [16, 15, 14]
NURSE_LIST = [NURSE1_LIST, NURSE2_LIST, NURSE3_LIST, NURSE4_LIST]

BUF_OP_LIST = [None] * 12
BUF_OP_NUM = [0] * 12


class Operation:
	def __init__(self, index, optype, oplength):
		self.i = index
		self.t = optype
		self.l = oplength
		self.o = False    # o for over time
		self.n = None     # n for nurse of the surgery

class Room:
	def __init__(self, index):
		self.index = index
		self.oplist = []
		self.optypelist = [0] * 10
		self.cumtime = 0
		self.totaltime = 0
		self.overwork = False
		self.finish = False

def mincumtime(roomlist):
	minindex = None
	mincumt = 99
	for i in range(12):
		if (roomlist[i].cumtime < mincumt and roomlist[i].finish == False):
			mincumt = roomlist[i].cumtime
			minindex = i
	return minindex

def printroomlist(roomlist, oplist):
	for i in range(12):
		print("Room index: {}".format(i))
		print("Operation order: ", end="")
		for j in roomlist[i].oplist[::-1]:
			print("{}({}) ".format(j, oplist[j].n), end="")
		print("")
		print("Operation type sum: {}".format(sum(roomlist[i].optypelist)))
		print("Total work time: {} hours".format(roomlist[i].totaltime))
		print("Over work: {}".format(roomlist[i].overwork))
		print("")

def plotroomlist(roomlist, oplist):
	height = 16
	interval = 4
	colors = ["white", "#a6cee3", "#1f78b4", "#33a02c", "#b2df8a", "#fb9a99", "#fdbf6f", "#ff7f00", "#cab2d6", "#e31a1c"]
	x_label = "time (hours)"

	ax = plt.subplot()
	labels = []
	count = 0
	for i in range(12):
		labels.append("Room " + str(i))
		totaltime = 0
		for j in roomlist[i].oplist[::-1]: 
			ax.broken_barh([(totaltime, oplist[j].l)], ((height+interval)*i + \
				interval, height), facecolors=colors[oplist[j].t]) 
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

roomlist1[8].oplist = [3, 19, 4, 7]
roomlist1[3].oplist = [12, 35]
roomlist1[10].oplist = [13, 14, 30, 5]

for i in range(12):
	roomlist1[i].totaltime = 0
	for j in roomlist1[i].oplist:
		roomlist1[i].totaltime += oplist1[j].l
		if (roomlist1[i].totaltime > STAN_TIME):
			oplist1[j].o = True
for i in range(12):
	if (roomlist1[i].totaltime > STAN_TIME):
		roomlist1[i].overwork = True

for i in range(12):
	op_num = BUF_OP_NUM[i]
	BUF_OP_LIST[i] = roomlist1[i].oplist[op_num]
	roomlist1[i].cumtime += oplist1[roomlist1[i].oplist[op_num]].l
count = 0
while (count < len(oplist1)):
	next_i = mincumtime(roomlist1)
	next_n = NURSE_LIST[NURSE[oplist1[BUF_OP_LIST[next_i]].t] - 1].pop()
	NURSE_LIST[NURSE[oplist1[BUF_OP_LIST[next_i]].t] - 1].insert(0, next_n)
	oplist1[BUF_OP_LIST[next_i]].n = next_n
	BUF_OP_NUM[next_i] += 1
	if (BUF_OP_NUM[next_i] >= len(roomlist1[next_i].oplist)):
		roomlist1[next_i].finish = True
		count += 1
		continue
	op_num = BUF_OP_NUM[next_i]
	BUF_OP_LIST[next_i] = roomlist1[next_i].oplist[op_num]
	roomlist1[next_i].cumtime += oplist1[roomlist1[next_i].oplist[op_num]].l
	count += 1

printroomlist(roomlist1, oplist1)
plotroomlist(roomlist1, oplist1)