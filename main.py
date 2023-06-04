import requests
from bs4 import BeautifulSoup
from time import sleep
import time
import datetime
import json
import random
import schedule

count = 0
def get_type_game():
    all_game_dict = []
    # day_go = 1
    hours_go = 1
    minutes_go = 1
    seconds_go = 5
    for count in range(1, 30):
        # cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # days=day_go,
        today2 = datetime.datetime.today()
        days_up = today2 + datetime.timedelta(hours=hours_go, minutes=minutes_go, seconds=seconds_go)
        time_game = days_up.strftime('%Y-%m-%d %H:%M:%S')
        print("days", days_up.strftime('%Y-%m-%d %H:%M:%S'))

        with open("users.json", encoding='utf-8') as file:
            users_list = json.load(file)

        with open("users2.json", encoding='utf-8') as file:
            users_list2 = json.load(file)


        my_list2 = [
            {"1v1": 2},
            {"2v2": 4},
            {"3v3": 6},
            {"4v4": 8},
            {"5v5": 10},
            {"1v1 x 4 T": 4},
            {"1v1 x 8 T": 8},
            {"1v1 x 16 T": 16},
            {"2v2 x 4 T": 8},
            {"2v2 x 8 T": 16},
            {"2v2 x 16 T": 32},
            {"3v3 x 4 T": 12},
            {"3v3 x 8 T": 24},
            {"3v3 x 16 T": 48},
            {"4v4 x 4 T": 16},
            {"4v4 x 8 T": 32},
            {"4v4 x 16 T": 64},
            {"5v5 x 4 T": 20},
            {"5v5 x 8 T": 40},
            {"5v5 x 16 T": 80}
            ]
        entry_fee = [5, 10, 20, 30, 50, 60, 80, 100, 200]

        random_integer_test = random.choice(my_list2)
        type_game_k = list(random_integer_test.keys())
        type_game_v = str(list(random_integer_test.values())).replace("[", "").replace("]", "")


        game_type = ''.join(type_game_k)
        players_count = int(type_game_v)

        random_entry_fee = random.choice(entry_fee)

        percent_prize_pool = int(random_entry_fee) * players_count / 100 * 12
        prize_pool = int(random_entry_fee) * players_count - percent_prize_pool

        random_users_list = ""
        random_users_list2 = ""
        team1_users = ""
        team2_users = ""
        if players_count == 2:
            random_users_list = random.choice(users_list)
            random_users_list2 = random.choice(users_list2)
        else:
            total_players = players_count / 2
            team1_users = random.sample(users_list, int(total_players))
            team2_users = random.sample(users_list2, int(total_players))
            random_users_list = random.choice(team1_users)
            random_users_list2 = random.choice(team2_users)


        prizepool = int(prize_pool)
        game = "CS:GO"
        server = "GLOB"
        entryfee = int(random_entry_fee)
        player1 = str(random_users_list)
        rating_p1 = random.randint(1000, 3000)
        rating_p2 = random.randint(1000, 3000)
        player2 = str(random_users_list2)

        match_type_list = ["Best of 3", "Single game"]
        match_type = random.choice(match_type_list)

        tournaments = ""

        game_score_list = ["1:0", "0:1"]
        random_game_score = random.choice(game_score_list)
        game_score = random_game_score
        # score1 = random.randint(0, 2)
        # score2 = random.randint(0, 2)
        # game_score = f"{score1} : {score2}"
        rounds_game = 1

        maps_list = ["Monastery", "Shoots", "Assault", "Backalley", "Insertion", "Italy", "Militia",
                     "Office", "Rush", "Workout", "Aztec", "Bank", "Bazaar", "Blackgold", "Cache",
                     "Castle", "Cbble", "Dust2", "Dust", "Facade", "Inferno", "Lake", "Marquis",
                     "Mirage", "Mist", "Nuke", "Overgrown", "Overpass", "Safehouse", "Season", "Shorttrain",
                     "Stmarc", "Sugarcane", "Train", "Vertigo", "Aim King", "AWP India", "Aim Crazy Jump"]
        maps_csgo = random.choice(maps_list)

        print(f"{game} | {prizepool} YMZ | {match_type}, {game_type}")
        title = f"{game} | {prizepool} YMZ | {match_type}, {game_type}"

        all_game_dict.append(
            {
                "game": game,
                "title": title,
                "server": server,
                "entry_fee": entryfee,
                "prize_pool": prizepool,
                "game_type": game_type,
                "players_count": players_count,
                "match_type": match_type,
                "maps": maps_csgo,
                "time_game": time_game,
                "tournaments": tournaments,
                "game_score": game_score,
                "rounds_game": rounds_game,
                "player1": player1,
                "rating_p1": rating_p1,
                "player2": player2,
                "rating_p2": rating_p2,
                "team1_users": team1_users,
                "team2_users": team2_users
            }
        )
        # day_go += 1
        hours_rand = random.randint(5, 10)
        hours_go += hours_rand
        min_rand = random.randint(10, 30)
        minutes_go += min_rand
        seconds_go += 5
        print(f"# Итерация {count} записана...")
        count += 1
        sleep(random.randrange(2, 4))
    # print(all_game_dict)
    with open("all_game_csgo.json", "w", encoding='utf-8') as file:
        json.dump(all_game_dict, file, indent=4, ensure_ascii=False)

    iteration_count = int(len(all_game_dict))
    print(f"Всего статей (ссылок): {iteration_count}")


def main():
    # start_time = time.time()
    # all_categories_data()
    # article_info()
    get_type_game()

    # schedule.every(3).seconds.do(job)
    # schedule.every(3).minutes.do(job)
    # schedule.every(3).hours.do(job)
    # schedule.every(3).days.do(job)
    # schedule.every(1).minutes.do(get_type_game)
    # print(schedule.get_jobs())
    # while True:
    #     schedule.run_pending()
    #     time.sleep(5)


    # finish_time = time.time() - start_time
    # print(f"Worked time: {finish_time}")


if __name__ == '__main__':
    main()
