from rs_controller import RuneScapeData, PlayerProfile
from rs_model import RunescapeDB

def run_job() -> None:
    controller = RuneScapeData()
    db = RunescapeDB()

    player_profiles: list[PlayerProfile] = controller.get_all_data()
    player_names: list[str] = controller.rs_users
    skill_names: list[str] = controller.skills

    db.insert_skills(skills=skill_names)
    db.insert_players(players=player_names)

    for profile in player_profiles:
        name = profile.name
        for profile in profile.skills:
            for skill,level in profile.items():
                db.insert_levels(player_name=name, skill_name=skill,level=level)
    #close db connection
    db.close()
run_job()