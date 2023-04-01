from OSRSBytes import Hiscores
import typing
import random
from prettytable import PrettyTable






#Zezima, Chairboy
skills: list = ['Attack', 'Defense', 'Strength', 'Hitpoints', 'Ranged', 'Prayer', 'Magic', 'Cooking', 'Woodcutting', 'Fletching', 'Fishing', 'Firemaking', 'Crafting', 'Smithing', 'Mining', 'Herblaw']
dimension: set = {"level","rank"}
combat_skills: list = ['Attack', 'Defense', 'Strength', 'Hitpoints', 'Ranged']
rs_users: set = {"Chairboy","42 DEF MAIN","Libsnowflake"}

#TODO: write extraction loop
#https://docs.google.com/spreadsheets/d/1jljLiuTqcUsTWaNoTxvuS5FhRmXWFj0n5dk9Ac-M43A/edit#gid=0
#create tables, partition by timestamp,
#load to loader table from here
#then execute sql for deltas
def extract_all_dims() -> None:
    for i,dim in enumerate(dimension):
        for skill in skills:
            pass


def _init_data_objects() -> list[object]:
    processed_users: list = []
    for i,user in enumerate(rs_users):
        user_data: object = {}
        user_data["runescape_stats"] = Hiscores(user)
        user_data["name"] = user
        processed_users.append(user_data)
    return processed_users


def get_rs_combat_data() -> str:
    processed_users: list[object] = _init_data_objects()
    row: list = [str]
    t: PrettyTable = PrettyTable(['Skill'] + list(rs_users))
    print(combat_skills)
    for i,skillstring in enumerate(combat_skills):
        row = []
        row.append(skillstring)
        for user in processed_users:
            print(skillstring)
            row.append(user["runescape_stats"].skill(skillstring,"level"))
        t.add_row(row)
    return t.get_string()




def get_rs_basic_data(is_random: bool=False) -> list[str]:
    chosen_skill: str = "Firemaking"
    processed_users: list[object] = _init_data_objects()

    if is_random:
        chosen_skill = skills[random.randint(0, len(skills)-1)]

    output_stream: list[str] = []
    for user in processed_users:
       # rs_stats_payload: object = {
       #     "name" : user["name"],
      #      "attack"
       # }
        output_stream.append(f":arrow_right: {user['name']}: {chosen_skill} Level of {user['runescape_stats'].skill(chosen_skill,'level')}")

    return output_stream

print(get_rs_combat_data())