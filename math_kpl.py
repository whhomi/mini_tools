
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File        :math_kpl.py
@Desc        :
@Date        :2023-02-24 15:30
@Author      :noBody
"""




class KplTeam :

    def __init__(self, name:str) -> None:
        self._play_big = 5
        self._play_small = 0
        self._lost_big = 0
        self._win_small = 0
        self.__point = 0
        self._small_point = 0
        self.name = name

    def do_win_small(self):
        self._play_small +=1
        self._win_small += 1

    def do_defeat_small(self):
        self._win_small -= 1
        self._play_small +=1

    def new_big_one(self):
        self._win_small = 0
    
    def close_big_one(self):
        if self._win_small > 0:
            self.__point+=1
        else:
            self._lost_big+=1
        self._small_point += self._win_small
        self._play_big -=1

    @property
    def current(self):
        current_info =  {
            "name":self.name,
            "big_win":self.__point,
            "big_lost":self._lost_big,
            "small_point":self._small_point,
            "play_big_surplus":self._play_big,
            "play_small_done":self._play_small
            }
        return current_info

class Play:

    play_method = ['do_win_small','do_defeat_small']
    teams = ['a','b']
    def __init__(self, teama:KplTeam, teamb:KplTeam, socre) -> None:
        self._teama = teama
        self._teamb = teamb
        self.socre = socre
        self._new_one()
        self.play()
        self._close_one()
    
    def play(self):
        socre = [ int(i) for i in self.socre.split(":")]
        for index, v in enumerate(socre):
            method = self.play_method[index]
            self._count(self._teama,v,method)
            self.play_method.reverse()
            method = self.play_method[index]
            self._count(self._teamb,v,method)
            self.play_method.reverse()
    
    def _count(self, team, point:int , method:str):
        done = getattr(team,method)
        [done() for _ in range(point)]

    def _close_one(self):
        for suffix in self.teams:
            obj = getattr(self,f"_team{suffix}")
            obj.close_big_one()

    def _new_one(self):
        for suffix in self.teams:
            obj = getattr(self,f"_team{suffix}")
            obj.new_big_one()

def generate_duel(teama,teamb):
    duel = {}
    for i in teama:
        for j in teamb:
            if i is j:
                continue
            ij_reverse = f'{j.name}:{i.name}'
            if ij_reverse in duel:
                continue
            duel[f'{i.name}:{j.name}']=[i,j]
    return duel

res ={
    "XYG:DYG":"0:0",
    "XYG:HERO":"0:0",
    "XYG:WOLVE":"0:0",
    "XYG:TESA":"0:0",
    "XYG:KSG":"0:0",
    "DYG:HERO":"0:0",
    "DYG:WOLVE":"0:0",
    "DYG:TESA":"0:0",
    "DYG:KSG":"0:0",
    "HERO:WOLVE":"0:0",
    "HERO:TESA":"0:0",
    "HERO:KSG":"0:0",
    "WOLVE:TESA":"0:0",
    "WOLVE:KSG":"0:0",
    "TESA:KSG":"0:0",
}

if __name__ == "__main__":
    XYG = KplTeam("XYG")
    DYG = KplTeam("DYG")
    HERO = KplTeam("HERO")
    WOLVE = KplTeam("WOLVE")
    TESA = KplTeam("TESA")
    KSG = KplTeam("KSG")
    
    team = [XYG,DYG,HERO,WOLVE,TESA,KSG]
    pg = generate_duel(team,team)
    for k,v in pg.items():
        print(k)
        
    Play(XYG,DYG,"0:3")
    Play(XYG,KSG,"2:3")
    Play(XYG,WOLVE,"0:3")
    # Play(XYG,HERO,"3:2")
    # Play(XYG,TESA,"3:2")

    # Play(WOLVE,KSG,"3:0")
    # Play(WOLVE,DYG,"3:0")
    Play(WOLVE,HERO,"3:2")
    # Play(WOLVE,TESA,"3:0")

    # Play(KSG,DYG,"3:0")
    Play(KSG,HERO,"2:3")
    Play(KSG,TESA,"3:1")

    Play(DYG,HERO,"2:3")
    Play(DYG,TESA,"2:3")

    Play(HERO,TESA,"2:3")

    print(XYG.current)
    print(WOLVE.current)
    print(KSG.current)
    print(DYG.current)
    print(HERO.current)
    print(TESA.current)
    
