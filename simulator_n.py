'''This is console app simulating life. The stuff of the simulator is represented with emojis.'''


from mainc import *
from checkbox import *
from emojis import *
from dashboard import *
import time
import random

emoji = Emoji()
name_D = Dashboard.name_DD

stuff = []#creating of matrix sheet, i.e array. it is the matrix itself, contains land, fence, animals, food and maybe even other stuff.
all_animals = []#the information about animals at the current moment
land_char = emoji.emLand#where animals can moving
fence_char = emoji.emfence#animals can not moving to this

dim = 24#size of matrix(dimention)
ani_number = 2#the number of animals the simulation starts with.
delay = 0.08#delay between animal leaps. if animal goes slower then it skips certain leaps.

#ani is abbreviation of animal
a_ani = {"id": 1, "latitude": 15, "longitude": 0, "symbol": emoji.ema, "birth_time": 0, "tmpv": 0, "velocity": 0, "milige": 0, "strength": 0, "pregnant": False}
b_ani = {"id": 2, "latitude": 3, "longitude": 1, "symbol": emoji.ema2, "birth_time": 0, "tmpv": 0, "velocity": 0, "milige": 0, "strength": 0, "pregnant": False}
c_ani = {"id": 3, "latitude": 2, "longitude": 4, "symbol": emoji.ema3, "birth_time": 0, "tmpv": 0, "velocity": 0, "milige": 0, "strength": 0, "pregnant": False}
d_ani = {"id": 4, "latitude": 17, "longitude": 10, "symbol": emoji.ema4, "birth_time": 0, "tmpv": 0, "velocity": 0, "milige": 0, "strength": 0, "pregnant": False}
e_ani = {"id": 5, "latitude": 16, "longitude": 11, "symbol": emoji.ema5, "birth_time": 0, "tmpv": 0, "velocity": 0, "milige": 0, "strength": 0, "pregnant": False}
foradtoallanis = [a_ani, b_ani, c_ani, d_ani, e_ani]
n_fadtans = 0
for taans in foradtoallanis:
	all_animals.append(taans)
	n_fadtans += 1
	if n_fadtans == ani_number:
		break

checkboxxxx = Checkbox(a_ani, b_ani, c_ani, d_ani, e_ani, ani_number, dim)
#checkboxxxx.check_inputs()

La, Lo = "latitude", "longitude"

matrix = Matrix(dim, stuff, land_char, fence_char, name_D)
sett = Set(stuff, La, Lo, a_ani["symbol"], b_ani["symbol"], c_ani["symbol"], d_ani["symbol"], e_ani["symbol"])

matrix.create()
sett.animals(a_ani, b_ani, c_ani, d_ani, e_ani, ani_number)

s = ""
while s != "ok":
	matrix.display()
	print ("ok?")
	s = input()

move = Move(dim, land_char, La, Lo, stuff, random)
#................................starts the block of code 1


animal = Animal(stuff)
isfirstloop = True
while True:
	for inallanims in all_animals:
		if inallanims["pregnant"] == True:
			animal.create(inallanims, max_id)
			#inallanims["pregnant"] = False
	if isfirstloop != True:
		anis_inloop = [a_ani, b_ani, c_ani, d_ani, e_ani]#foradtoallanis
		countyjh = 0
		for assiabc in anis_inloop:
			minvalueid = min(iani['id'] for iani in all_animals)
			for i in all_animals:
				if i["id"] == minvalueid:
					i["id"] = minvalueid + 90000000000
			for iiwwii in all_animals:
				if iiwwii["id"] == minvalueid:
					assiabc = iiwwii
			countyjh += 1
			if countyjh == ani_number:
				break
		for i in anis_inloop:
			i["id"] -= 90000000000
	isfirstloop = False


	#.............................ends the block of code 1
	got_direction = got_direction_2 = got_direction_3 = got_direction_4 = got_direction_5 = ""

	if ani_number >= 1:
		move.delete_old(a_ani)
	if ani_number >= 2:
		move.delete_old(b_ani)
	if ani_number >= 3:
		move.delete_old(c_ani)
	if ani_number >= 4:
		move.delete_old(d_ani)
	if ani_number >= 5:
		move.delete_old(e_ani)

	while True:
		time.sleep(delay)
		#..........................block 2. checks conditions of animals(if they has die or born), if changes detected then break and go to upper loop.


		max_id = 1#bring out of loop
		for inallanis in all_animals:
			if inallanis["id"] > max_id:
				max_id = inallanis["id"]
			inallanis["milige"] += 1
			if inallanis["milige"] == 20 or inallanis["milige"] == 40 or inallanis["milige"] == 60:
				inallanis["pregnant"] = True
				#break


		#..........................ends of block 2
		xac1, xac2, xac3, xac4, xac5 = b_ani, c_ani, d_ani, e_ani, a_ani

		if ani_number == 1:
			xac1 = a_ani
			ggt = 1
		if ani_number == 2:
			xac2 = a_ani
			ggt = 2
		if ani_number == 3:
			xac3 = a_ani
			ggt = 3
		if ani_number == 4:
			xac4 = a_ani
			ggt = 4
		if ani_number == 5:
			ggt = 5

		new_position, got_direction = move.get_direction(a_ani, got_direction)
		move.update_environment(new_position, cto=a_ani["symbol"])
		matrix.display()
		#print(all_animals)
		move.delete_old(xac1)
		#time.sleep(0.06)
		if ggt == 1:
			continue

		new_position, got_direction_2 = move.get_direction(b_ani, got_direction_2)
		move.update_environment(new_position, cto=b_ani["symbol"])
		matrix.display()
		#print(all_animals)
		move.delete_old(xac2)
		#time.sleep(0.06)
		if ggt == 2:
			continue

		new_position, got_direction_3 = move.get_direction(c_ani, got_direction_3)
		move.update_environment(new_position, cto=c_ani["symbol"])
		matrix.display()
		move.delete_old(xac3)
		#time.sleep(0.06)
		if ggt == 3:
			continue

		new_position, got_direction_4 = move.get_direction(d_ani, got_direction_4)
		move.update_environment(new_position, cto=d_ani["symbol"])
		matrix.display()
		move.delete_old(xac4)
		#time.sleep(0.8)
		if ggt == 4:
			continue

		new_position, got_direction_5 = move.get_direction(e_ani, got_direction_5)
		move.update_environment(new_position, cto=e_ani["symbol"])
		matrix.display()
		move.delete_old(xac5)



		#time.sleep(delay)
