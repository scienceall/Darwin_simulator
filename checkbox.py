#the block of code below is for check the input
#initial data, this needs only when the program
#starts. #######################################
import time

class Checkbox:
    def __init__(self, a_ani, b_ani, c_ani, d_ani, e_ani, ani_number, dim):
        self.a_ani = a_ani
        self.b_ani = b_ani
        self.c_ani = c_ani
        self.d_ani = d_ani
        self.e_ani = e_ani
        self.ani_number = ani_number
        self.dim = dim


    def check_inputs(self):
        a_ani, b_ani, c_ani, d_ani, e_ani, ani_number, dim = self.a_ani, self.b_ani, self.c_ani, self.d_ani, self.e_ani, self.ani_number, self.dim
        List_of_anitocheck = [str(a_ani["latitude"])+str(a_ani["longitude"]),str(b_ani["latitude"])+str(b_ani["longitude"]),
                              str(c_ani["latitude"])+str(c_ani["longitude"]),str(d_ani["latitude"])+str(d_ani["longitude"]),
                              str(e_ani["latitude"])+str(e_ani["longitude"])]

        Lengthofanc = len(List_of_anitocheck)
        uniqueAniposi = []
        for iiii in List_of_anitocheck:
        	if iiii not in uniqueAniposi:
        		uniqueAniposi.append(iiii)
        Lenuni = len(uniqueAniposi)

        aaa_ranin=bbb_ranin=ccc_ranin=ddd_ranin=eee_ranin=0
        if ani_number >= 1:
        	aa_ranin = a_ani.values()
        	aaa_ranin = max(aa_ranin)
        if ani_number >= 2:
        	bb_ranin = b_ani.values()
        	bbb_ranin= max(bb_ranin)
        if ani_number >= 3:
        	cc_ranin = c_ani.values()
        	ccc_ranin = max(cc_ranin)
        if ani_number >= 4:
        	dd_ranin = d_ani.values()
        	ddd_ranin = max(dd_ranin)
        if ani_number >= 5:
        	ee_ranin = e_ani.values()
        	eee_ranin= max(ee_ranin)
        xxxx_ranin = [aaa_ranin, bbb_ranin, ccc_ranin, ddd_ranin, eee_ranin]
        xxxxx_ranin = max(xxxx_ranin)

        ccccc = 1
        while ccccc == 1:
        	if ani_number < 1 or ani_number > 5:
        		print ("ani_number must be 1 to 5")
        		time.sleep(10)
        	elif ani_number > dim * dim:
        		print ("ani_number must be less than dim^2")
        		time.sleep(10)
        	elif dim < 1:
        		print ("dim must be grather or equal to 1")
        		time.sleep(10)
        	elif Lenuni < Lengthofanc:
        		print ("duplicated ani coordinates found")
        		time.sleep(10)
        	elif xxxxx_ranin > dim-1:
        		print ("some animals out of matrix")
        		time.sleep(10)
        	else:
        		break

        while True:
        	if isinstance(ani_number, int):
        		break
        	else:
        		print ("ani_number must be integer")
        		time.sleep(10)

        while True:
        	if isinstance(dim, int):
        		break
        	else:
        		print ("dim must be integer")
        		time.sleep(10)
#the check block has ended. ####################
################################################
################################################
