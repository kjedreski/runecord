from OSRSBytes import Hiscores
import typing
import random
from prettytable import PrettyTable
import datetime
import csv
import requests
from rs_model import RunescapeDB 


class PlayerProfile:

    def __init__(self,name:str) -> None:
        self.name: str = name
        self.skills: list[object] = []

    def add_skill(self, skill: object) -> None:
        self.skills.append(skill)


class RuneScapeData:

    def __init__(self) -> None:
        self.skills: list = ['Attack', 'Defense', 'Strength', 'Hitpoints', 'Ranged', 'Prayer', 'Magic', 'Cooking', 'Woodcutting', 'Fletching', 'Fishing', 'Firemaking', 'Crafting', 'Smithing', 'Mining', 'Herblore']
        self.dimension: set(str) = {"level","rank"}
        self.combat_skills: list = ['Attack', 'Defense', 'Strength', 'Hitpoints', 'Ranged', 'Magic', 'Prayer']
        self.rs_users: set(str) = self._read_users_file()
        self.processed_users: list[object] = self._init_data_objects( users = self.rs_users)

    def _is_rs_player(self,player_name: str) -> bool:
        url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={player_name}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            print(f"Failed to retrieve data for {player_name}. Status code: {response.status_code}")
            return False

    def _read_users_file(self) -> list[str]:
        filename: str = "users.csv"
        data: list = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            try:
                for row in reader:
                    for value in row:
                        if self._is_rs_player(player_name = value):
                            data.append(value)
                        else:
                            pass
            except FileNotFoundError:
                print(f"Error: file {filename} not found")
        #kill dupes conversion to set
        data = set(data)
        return data

    def _init_data_objects(self, users: set) -> list[object]:
        tmp_processed_users: list[object] = []
        for i,user in enumerate(users):
            user_data: object = {}
            try:
                user_data["runescape_stats"] = Hiscores(user)
            except:
                print("name not found, skipping")
            user_data["name"] = user
            tmp_processed_users.append(user_data)
        return tmp_processed_users
    
    def get_all_data(self) -> list:
        ret_payload: list[object] = []
        for user in self.processed_users:
            player_profile: PlayerProfile = PlayerProfile(name=user["name"])
            for i,skillstring in enumerate(self.skills):
                rs_stat = user["runescape_stats"].skill(skillstring,"level")
                player_profile.add_skill(skill={skillstring:rs_stat})
            ret_payload.append(player_profile)
        return ret_payload

    def get_delta(self) -> str:
        #row: list = [str]
        t: PrettyTable = PrettyTable(['Player','Skill','Delta'])
        db: RunescapeDB = RunescapeDB()
        db_results: list[tuple] = db.get_delta()
        for row in db_results:
            row = list(row)
            row[2] = "+" + str(row[2])
            t.add_row(row)
        return t.get_string()



    def get_rs_combat_data(self) -> str:
        row: list = [str]
        t: PrettyTable = PrettyTable(['Skill'] + list(self.rs_users))
        for i,skillstring in enumerate(self.combat_skills):
            row = []
            row.append(skillstring)
            for user in self.processed_users:
                row.append(user["runescape_stats"].skill(skillstring,"level"))
            t.add_row(row)
        return t.get_string()
    
    def get_rs_basic_data(self,is_random: bool=False) -> list[str]:
        chosen_skill: str = "Firemaking"

        if is_random:
            chosen_skill = self.skills[random.randint(0, len(self.skills)-1)]

        output_stream: list[str] = []
        for user in self.processed_users:
        # rs_stats_payload: object = {
        #     "name" : user["name"],
        #      "attack"
        # }
            output_stream.append(f":arrow_right: {user['name']}: {chosen_skill} Level of {user['runescape_stats'].skill(chosen_skill,'level')}")

        return output_stream