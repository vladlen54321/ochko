import random
from osnova_21 import *


diller = 0
player = 0
player_osn = list()
diller_osn = list()
player_status = str()
nichia = str()

class Players():
    def __init__(self, name1 : int, name2 : int, players_osn1 : list, players_osn2 : list, player_status : str, nichia : str):
        self.players1 = name1
        self.players2 = name2
        self.players_osn1 = players_osn1
        self.players_osn2 = players_osn2
        self.player_status = player_status
        self.nichia = nichia
        
    def rand_razdacha_player(self):
        for _ in range(2):
            rand_val = random.choice(list(my_dict))
            rand_mast = random.choice(list(my_dict[rand_val]))

            self.players1 += my_dict[rand_val][rand_mast]
            self.players_osn1.append(rand_mast)
            self.players_osn1.append(rand_val)
        for _ in range(2):
            rand_val = random.choice(list(my_dict))
            rand_mast = random.choice(list(my_dict[rand_val]))

            self.players2 += my_dict[rand_val][rand_mast]
            self.players_osn2.append(rand_mast)
            self.players_osn2.append(rand_val)

    def ochko(self):
        global pl_ochko
        pl_ochko = 0
        dl_ochko = 0
        for i in self.players_osn1:
            if i == "A":
                pl_ochko += 1
        for i in self.players_osn2:
            if i == "A":
                dl_ochko += 1
        if pl_ochko == 2 and dl_ochko == 2:
            self.players1 = 21
            self. players2 = 21
            self.vivod = "НИЧЬЯ"
            self.player_status = "НИЧЬЯ"
        elif pl_ochko == 2:
            self.players1 = 21
            self.vivod = "WIN"
            self.player_status = "WIN"
        elif dl_ochko == 2:
            self.players2 = 21
            self.vivod = "LOOS"
            self.player_status = "LOOS"
        else:
            pass

    def schet(self):
        self.request = f"Счет игрока :{self.players1}  {self.players_osn1}\nСчет диллера :{self.players2}  {self.players_osn2}\n"
        print(self.request)

    def giv_card_player(self):
        rand_value = random.choice(list(my_dict)) 
        rand_masti = random.choice(list(my_dict[rand_value]))
        self.players1 += my_dict[rand_value][rand_masti]
        self.players_osn1.append(rand_masti)
        self.players_osn1.append(rand_value)

    def giv_card_diller(self):
        while self.players2 < 18:
            rand_value = random.choice(list(my_dict)) 
            rand_masti = random.choice(list(my_dict[rand_value]))
            self.players2 += my_dict[rand_value][rand_masti]
            self.players_osn2.append(rand_masti)
            self.players_osn2.append(rand_value)

    def proverca(self):
        self.vivod = str()
        a = self.players1
        b = self.players2
        if a > 19 and b > 19 and a < 21 and b < 21 and a == b or a == 21 and b == 21:
            self.nichia = "НИЧЬЯ"
            self.vivod = "НИЧЬЯ"
        elif a == 21 and b < 18:
            play.giv_card_diller()
            play.proverca()
        elif b == 21 and a == 20 or a > 21:
            self.player_status = "LOOS"
            self.vivod = "LOOS"
        elif a == 21 and b == 18 or a == 21 and b > 21 or b > 21:
            self.player_status = "WIN"
            self.vivod = "WIN"
        elif b > 18 and a > 18 and b > a and b < 22:
            self.player_status = "LOOS"
            self.vivod = "LOOS"
        elif b >= 18 and a > 18 and a > b and a < 22:
            self.player_status = "WIN"
            self.vivod = "WIN"
        elif b > 18  and b > a and  a == 20:
            self.player_status = "LOOS"
            self.vivod = "LOOS"
        elif b == 18 and a > b and a < 22:
            self.player_status = "WIN"
            self.vivod = "WIN"
        else:
            pass
    def prov(self):
        global diller,player,player_osn,diller_osn,player_status,nichia,play
        if self.player_status == "LOOS" or self.player_status == "WIN" or self.nichia == "НИЧЬЯ":
            self.players2 = 0
            self.players1 = 0
            self.players_osn1 = list()
            self.players_osn2= list()
            self.player_status = str()
            self.nichia = str()
        else:
            pass

play = Players(player, diller, player_osn, diller_osn, player_status, nichia)

