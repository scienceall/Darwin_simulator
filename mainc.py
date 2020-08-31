'''This file(module) contains all vital functions(methods) for ecosystem of the simulator. These methods call from the file simulator.py(simulator_n.py).
But, not excepted that methods can be called from another files.'''


class Matrix:
    """The matrix is like field or land where all avents happen. The matrix contains animals and food represented with certain characters, and also,
    the matrix surronded by fence."""
    def __init__(self, dim, stuff, land_char, fence_char, name_D):
        self.dim = dim
        self.stuff = stuff
        self.land_char = land_char
        self.fence_char = fence_char
        self.name_D = name_D

    def create(self):
        """In this function the matrix is filling by ether(something like ground where all events will happening). The matrix itself creates here."""
        dim, stuff, land_char = self.dim, self.stuff, self.land_char
        for i in range(dim):
            stuff.append([0] * dim)
        for i2 in range(0, dim):
            for ii in range(0, dim):
                stuff[i2][ii] = land_char

    def display(self):
        """This function prints out the matrix on display with all current stuff inside it and also show the fence.
        The function is call in main loop of the program."""
        name_D, fence_char, dim, stuff = self.name_D, self.fence_char, self.dim, self.stuff
        print ("\n"*50)
        print ("This is "+name_D+" simulator.")
        print (fence_char*(dim+2))
        for i in range(0, dim):
            a = ""
            for ii in range(0, dim):
                a = a + str(stuff[i][ii])
            print (fence_char+a+fence_char)
        print (fence_char*(dim+2))


class Animal:
    """Animals are units move across the matrix."""
    def __init__(self, stuff):
        self.stuff = stuff

    def create(self, all_animals, highest_id):
        """This method borns animals. Animal can be born on any one out of eight free position, surrond the parrent. If there is no free positions when
        the time to be born come up, the animal is not borns, and the parrent just continue to live as normal. The animal will make attempt to born a child
        again when the time will come as scheduled in the animal properties. If animal is not borns due to lack of free positions, it is the same if animal
        has born and instantly died. Each new successfully borned animal assigning to identification number. The id is unique, and cannot be repeated. The
        id is the integer number and it has the range from 1 to infinity."""
        stuff = self.stuff

    def terminate():
        """The method calls when an animal is should not longer exists. This can happen by reason if an animal die due to limit of lifspan or an animal has
        been killed in fight, or even, probably by some another reasons."""
        pass

    def modify():
        """The method modifyuing animals, i.e. changes a symbol of animal and change some another data in all_animals list if necessary."""
        pass


class Set:
    """Preset initial positions of animals."""
    def __init__(self, stuff, La, Lo, c1, c2, c3, c4, c5):
        self.stuff = stuff
        self.La = La
        self.Lo = Lo
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5

    def animals(self, a_ani, b_ani, c_ani, d_ani, e_ani, ani_number):
        """Initial position of animals are set here."""
        stuff, La, Lo, c1, c2, c3, c4, c5 = self.stuff, self.La, self.Lo, self.c1, self.c2, self.c3, self.c4, self.c5
        if ani_number >= 1:
            x, y = a_ani[La], a_ani[Lo]
            stuff[x][y] = c1
        if ani_number >= 2:
            x2, y2 = b_ani[La], b_ani[Lo]
            stuff[x2][y2] = c2
        if ani_number >= 3:
            x3, y3 = c_ani[La], c_ani[Lo]
            stuff[x3][y3] = c3
        if ani_number >= 4:
            x4, y4 = d_ani[La], d_ani[Lo]
            stuff[x4][y4] = c4
        if ani_number >= 5:
            x5, y5 = e_ani[La], e_ani[Lo]
            stuff[x5][y5] = c5


class Move:
    """The class moves animals. To move an animal needs to perform three steps: First - decide where to go, north, east, south or west, for this purpose
    the class has method get_direction. Second - put symbol to new position on the matrix, this job do the method update_environment.
    Third - delete the symbol from old position, it is method delete_old."""
    def __init__(self, dim, land_char, La, Lo, stuff, random):
        self.dim = dim
        self.land_char = land_char
        self.La = La
        self.Lo = Lo
        self.stuff = stuff
        self.random = random

    def get_direction(self, x_ani, got_direction):#true and false instead of free and not free
        """The function is to choose direction for animals. Animals can walk vertical or horizontal, but not by diagonal. They cannot return 180 degree,
        except is there are no remain options(an animal only can go left, right and straight, and cannot back, except if an animal has no choice.
        By has no choice means that there is no free directions left, except back. And what is back depends on previous walk).
        If there is no free directions at all, then an animal pass their walk."""
        dim, land_char, La, Lo, stuff, random = self.dim, self.land_char, self.La, self.Lo, self.stuff, self.random
        x, y = x_ani[La], x_ani[Lo]

        def check_free(a, b):
            try:
                if stuff[a][b] == land_char and a != dim+1 and a != -1 and b != dim+1 and b != -1:
                    direction = "free"
                else:
                    direction = "not free"
            except IndexError:#when an animal is going hits the fence.
                direction = "not free"
            return (direction)

        xN, yN, xS, yS = x + 1, y, x - 1, y
        xE, yE, xW, yW = x, y + 1, x, y - 1
        north = sought = east = west = ""
        xLi = [[north, "north", La, xN, yN], [sought, "sought", La, xS, yS], [east, "east", Lo, xE, yE], [west, "west", Lo, xW, yW]]

        v = 1
        while v != 0:

            ca, cb = 0, 1
            while ca < 4:
                if got_direction != xLi[cb][1] or v == 2:
                    xLi[ca][0] = check_free(xLi[ca][3], xLi[ca][4])
                else:
                    xLi[ca][0] = "not free"
                ca, cb = ca + 1, cb - 1

            v += 1

            if v == 3:
                if xLi[0][0] != "free" and xLi[1][0] != "free" and xLi[2][0] != "free" and xLi[3][0] != "free":
                    got_direction_n = "stay there"
                else:
                    got_direction_n = "not stay there"
                break
            elif xLi[0][0] != "free" and xLi[1][0] != "free" and xLi[2][0] != "free" and xLi[3][0] != "free":
                pass
            else:
                v = 0

        if v == 3 and got_direction_n == "stay there":
            got_direction_n = "stay thete"
            return (x_ani, got_direction_n)
        else:
            free_numb = 0
            for check_nsew_free in xLi:
                if check_nsew_free[0] == "free":
                    free_numb += 1
            choice = random.randint(1, free_numb)
            count_to_choose = 0
            for c in xLi:
                if c[0] == "free":
                    count_to_choose += 1
                    if count_to_choose == choice:
                        got_direction_n = c[1]
                        if c[1] == "north" or c[1] == "east":
                            x_ani[c[2]] += 1
                        else:
                            x_ani[c[2]] -= 1

            return (x_ani, got_direction_n)

    def update_environment(self, new_position, cto):
        """The function is part of algorithm move animals."""
        stuff = self.stuff
        a = new_position["latitude"]
        b = new_position["longitude"]
        stuff[a][b] = cto

    def delete_old(self, x_ani):
        """The function is part of algorithm move animals."""
        stuff, land_char = self.stuff, self.land_char
        a = x_ani["latitude"]
        b = x_ani["longitude"]
        stuff[a][b] = land_char
