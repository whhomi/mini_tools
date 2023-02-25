#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File        :math_kpl.py
@Desc        :
@Date        :2023-02-24 15:30
@Author      :noBody
"""

import json



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

def generate_duel(team_socre:dict):
    play_list = []
    team_dict = {}
    for k,v in team_socre.items():
        teama,teamb = [i.strip() for i in k.split(":")]
        if teama not in team_dict :
            kpl_a = KplTeam(teama)
            team_dict[teama] = kpl_a
        else: 
            kpl_a = team_dict[teama] 
        if teamb not in team_dict :
            kpl_b = KplTeam(teamb)
            team_dict[teamb] = kpl_b
        else :
            kpl_b = team_dict[teamb]
        play_one = [kpl_a, kpl_b, v]
        play_list.append(play_one)
    return play_list,team_dict

def read_json(file_path):
    with open(file_path) as fj:
        res = json.load(fj)
    plays, team_dict = generate_duel(res)
    return plays, team_dict

if __name__ == "__main__":
    plays_args, team_dict = read_json("./play.json")
    for play_args in plays_args:
        if "0:0" in play_args:
            continue
        Play(*play_args)
    socre_list = []
    for _,v in team_dict.items():
        socre_list.append(v.current)
    g =  lambda x:(x['big_win'],x['small_point'])
    socre_list.sort(key=g,reverse=True)
    for socre in socre_list:
        print("队伍: {}\t 大局得分: {} \t小局得分: {} ".format(socre["name"],socre["big_win"],socre["small_point"]))
