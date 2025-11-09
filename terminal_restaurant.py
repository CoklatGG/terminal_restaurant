import json
from time import sleep, time
from math import floor
from random import randint

G = 0
KG = 1
PERCENT = 2
LOAD_SUCCES = 0
LOAD_FILE_NOT_FOUND = 1
LOAD_CORRUPTED = 2
LOAD_CORRUPT_RESET = 3
WORKER_STATUS_SLEEPING = 0
WORKER_STATUS_WAITING_FOR_COMMAND = 1
WORKER_STATUS_WORKING = 2
WORKER_TYPE_CHEF = 0
WORKER_TYPE_CASHIER = 1
TYPE_INGREDIENT = 0
TYPE_WORKER = 1
TYPE_RECIPE = 2
ACTION_TYPE_CUSTOMER_LEAVE = 0
ACTION_TYPE_FOOD_READY = 1
ACTION_TYPE_CUSTOMER_SERVED = 2
ACTION_TYPE_CUSTOMER_ARRIVE = 3
game_data: dict = {
    "day" : 0,
    "money" : 50000,
    "option" : {
        "satuan" : KG
    },
    "chef" : 1,
    "cashier" : 0,
    "worker" : {
        "chef#1" : {
            "description" : "Teman terbaikmu sejauh ini.",
            "speed" : 1,
            "status" : WORKER_STATUS_SLEEPING,
            "type" : WORKER_TYPE_CHEF
        },
    },
    "cooked_rice_capacity" : 1.5,
    "rice_capacity" : 10,
    "spice_capacity" : 5,
    "kecap" : "UNLIMITED",
    "stock" : {
        "recipe_book" : {
            "display_name" : "Buku Resep",
            "amount" : 1,
            "capacity_type" : "quantity"
        },
        "beras" : {
            "display_name" : "Beras",
            "amount" : 2,
            "capacity_type" : "rice_capacity"
        },
        "rempah" : {
            "display_name" : "Rempah-Rempah",
            "amount": 1,
            "capacity_type" : "spice_capacity"
        },
        "kecap" : {
            "display_name" : "Kecap",
            "amount": 1000000,
            "capacity_type" : "kecap"
        },
        "table" : {
            "display_name" : "Meja",
            "amount": 1,
            "capacity_type" : "quantity"
        },
        "chair" : {
            "display_name" : "Kursi",
            "amount": 1,
            "capacity_type" : "quantity"
        },
    },
    "recipe" : {
        "nasi" : {
            "display_name" : "Nasi",
            "description" : "Makanan wajib orang Asia.",
            "amount" : 1.5,
            "time" : 2,
            "cost" : 1000,
            "material" : {
                 "beras" : {
                    "display_name" : "Beras",
                    "amount" : 0.5,
                    "capacity_type" : "rice_capacity"
                }
            },
            "capacity_type" : "cooked_rice_capacity"
        },
        "nasi_kecap" : {
            "display_name" : "Nasi Kecap",
            "description" : "Makanan favorit di akhir bulan.",
            "amount" : 1,
            "time" : 0,
            "cost" : 2500,
            "material" : {
                "nasi" : {
                    "display_name" : "Nasi",
                    "amount" : 0.1,
                    "capacity_type" : "cooked_rice_capacity"
                },
                "kecap" : {
                    "display_name" : "Kecap",
                    "amount": 20,
                    "capacity_type" : "kecap"
                }
            },
            "capacity_type" : "quantity"
        },
        "nasgor" : {
            "display_name" : "Nasi Goreng",
            "description" : "Beras yang direbus, kemudian digoreng.",
            "amount" : 1,
            "time" : 1,
            "cost" : 10000,
            "material" : {
                "nasi" : {
                    "display_name" : "Nasi",
                    "amount" : 0.1,
                    "capacity_type" : "cooked_rice_capacity"
                },
                "rempah" : {
                    "display_name" : "Rempah-Rempah",
                    "amount": 0.05,
                    "capacity_type" : "spice_capacity"
                },
                "kecap" : {
                    "display_name" : "Kecap",
                    "amount": 10,
                    "capacity_type" : "kecap"
                }
            },
            "capacity_type" : "quantity"
        }
    },
    "market" : {
        "beras" : {
            "display_name" : "Beras",
            "amount" : 1,
            "capacity_type" : "rice_capacity",
            "cost" : 20000,
            "type" : TYPE_INGREDIENT
        },
        "rempah" : {
            "display_name" : "Rempah-Rempah",
            "amount" : 0.1,
            "capacity_type" : "spice_capacity",
            "cost" : 10000,
            "type" : TYPE_INGREDIENT
        },
        "kecap" : {
            "display_name" : "Kecap",
            "amount" : 100,
            "capacity_type" : "kecap",
            "cost" : 5000,
            "type" : TYPE_INGREDIENT
        },
        "table" : {
            "display_name" : "Meja",
            "amount" : 1,
            "capacity_type" : "quantity",
            "cost" : 75000,
            "type" : TYPE_INGREDIENT
        },
        "chair" : {
            "display_name" : "Kursi",
            "amount" : 1,
            "capacity_type" : "quantity",
            "cost" : 50000,
            "type" : TYPE_INGREDIENT
        },
        "chef" : {
            "display_name" : "Chef",
            "cost" : 250000,
            "type" : TYPE_WORKER,
            "item_data" : {
                "description" : "Chef yang kamu beli online.",
                "speed" : 2,
                "status" : WORKER_STATUS_SLEEPING,
                "type" : WORKER_TYPE_CHEF
            }
        },
        "cashier" : {
            "display_name" : "Kasir",
            "cost" : 500000,
            "type" : TYPE_WORKER,
            "item_data" : {
                "description" : "Kasir yang kamu beli online.",
                "speed" : 2,
                "status" : WORKER_STATUS_SLEEPING,
                "type" : WORKER_TYPE_CASHIER
            }
        },
        "chicken_recipe" : {
            "display_name" : "Resep Nasi Ayam Kecap",
            "cost" : 100000,
            "type" : TYPE_RECIPE,
            "item_data" : {
                "display_name" : "Nasi Ayam Kecap",
                "description" : "Nasi ayam yang dikecapkan... atau kecap ayam yang dinasikan?",
                "amount" : 1,
                "time" : 1,
                "cost" : 15000,
                "material" : {
                    "nasi" : {
                        "display_name" : "Nasi",
                        "amount" : 0.1,
                        "capacity_type" : "cooked_rice_capacity"
                    },
                    "rempah" : {
                        "display_name" : "Rempah-Rempah",
                        "amount": 0.1,
                        "capacity_type" : "spice_capacity"
                    },
                    "kecap" : {
                        "display_name" : "Kecap",
                        "amount": 75,
                        "capacity_type" : "kecap"
                    },
                    "chicken" : {
                        "display_name" : "Ayam",
                        "amount": 1,
                        "capacity_type" : "quantity"
                    }
                },
                "capacity_type" : "quantity"
            }
        },
        "chicken" : {
            "display_name" : "Ayam",
            "amount" : 1,
            "capacity_type" : "quantity",
            "cost" : 10000,
            "type" : TYPE_INGREDIENT
        }
    },
    "furniture" : {
        "table" : 0,
        "chair" : 0
    }
}
customer: int = 0
action_timer: dict = {}
turn = -1
kitchen_data: dict = {
    "nasi" : 0,
    "food_ready" : {}
}
table: dict = {}
income: list = []
read_notif: list = []
unread_notif: list = []
customer_line: list = []


# Helper function ^_^
def get_chef() -> list:
    result = []
    for w in game_data["worker"].items():
        if w["type"] == WORKER_TYPE_CHEF:
            result.append(w)
    return result


def find_in_list(l: list, value) -> int:
    if not value in l:
        return -1
    return l.index(value)


def input_safe_int(text: str) -> int:
    while True:
        try:
            return int(input(text))
        except ValueError:
            continue


def input_int_in_range(text: str, min: int, max: int) -> int:
    user_input: int
    while True:
        user_input = input_safe_int(text)
        if user_input < min or user_input > max:
            continue
        else:
            return user_input


def get_unit_formatted(amount: int, capacity_type: str, use_ratio: bool = True) -> str:
    if capacity_type == "quantity":
        return f"x{dot_format(amount)}"
    if capacity_type == "kecap" and type(amount) == str:
        return f"UNLIMITED"
    if capacity_type == "kecap":
        return f"{dot_format(amount)}ml"
    if game_data["option"]["satuan"] == G and use_ratio:
        return f"{round(amount * 1000, 2)}g/{game_data[capacity_type] * 1000}g".replace(".", ",")
    if game_data["option"]["satuan"] == KG and use_ratio:
        return f"{round(amount, 2)}Kg/{game_data[capacity_type]}Kg".replace(".", ",")
    if game_data["option"]["satuan"] == G:
        return f"{round(amount * 1000, 2)}g".replace(".", ",")
    if game_data["option"]["satuan"] == KG:
        return f"{round(amount, 2)}Kg".replace(".", ",")
    if game_data["option"]["satuan"] == PERCENT:
        return f"{round((float(amount) / game_data[capacity_type]) * 100, 2)}%".replace(".", ",")


def dot_format(num: int) -> str:
    return ("{:,}".format(num)).replace(",", ".")


# Back-End shi' right here
def queue_customer(data: dict) -> None:
    if len(customer_line) <= 0:
        customer_line.append(data)
        customer_line[0]["action"] = schedule_action(
            {
                "type" : ACTION_TYPE_CUSTOMER_LEAVE,
                "time" : data["patience"],
                "action_data" : data
            }
        )
        return
    customer_line.append(data)


def dequeue_customer() -> None:
    customer_line.pop(0)
    if len(customer_line) > 0:
        customer_line[0]["action"] = schedule_action(
            {
                "type" : ACTION_TYPE_CUSTOMER_LEAVE,
                "time" : customer_line[0]["patience"],
                "action_data" : data
            }
        )
    


def load_game_data() -> int:
    global game_data
    try:
        with open("game_data.json") as f:
            game_data = json.load(f)
            return LOAD_SUCCES
    except FileNotFoundError:
        with open("game_data.json", "w") as f:
            json.dump(game_data, f,)
            return LOAD_FILE_NOT_FOUND
    except Exception:
        pilihan: str
        print("Error: File Corrupted")
        while True:
            try:
                pilihan = input("Mulai dari awal(y/n)?: ")
            except Exception:
                continue
            if pilihan.lower() == "y":
                with open("game_data.json", "w") as f:
                    json.dump(game_data, f,)
                return LOAD_CORRUPT_RESET
            elif pilihan.lower() == "n":
                return LOAD_CORRUPTED


def decrease_turn(by: int) -> None:
    global turn
    if not by > 0:
        return
    turn -= 1
    if turn <= 0:
        day_end()
        return
    actions = list(action_timer.keys())
    for a in actions:
        action_timer[a]["time"] -= 1
        if not action_timer[a]["time"] <= 0:
            continue
        do_delayed_action(action_timer[a])
        action_timer.pop(a)
    decrease_turn(by - 1)


def do_delayed_action(action: dict) -> None:
    if action["type"] == ACTION_TYPE_FOOD_READY:
        action_data = action["action_data"]
        game_data["worker"][action_data["chef"]]["status"] = WORKER_STATUS_WAITING_FOR_COMMAND
        if action_data["food"] == "nasi":
            kitchen_data["nasi"] = min(game_data["cooked_rice_capacity"], kitchen_data["nasi"] + action_data["food_data"]["amount"])
            unread_notif.append("Nasi siap!")
            return
        if not action_data["food"] in kitchen_data["food_ready"]:
            kitchen_data["food_ready"][action_data["food"]] = {
                "display_name" : action_data["food_data"]["display_name"],
                "amount" : action_data["food_data"]["amount"]
            }
            unread_notif.append(f'{action_data["food_data"]["amount"]} {action_data["food_data"]["display_name"]} siap!')
            return
        unread_notif.append(f'{action_data["food_data"]["amount"]} {action_data["food_data"]["display_name"]} siap!')
        kitchen_data["food_ready"][action_data["food"]]["amount"] += action_data["food_data"]["amount"]
        return
    if action["type"] == ACTION_TYPE_CUSTOMER_ARRIVE:
        next_customer_time_mid = max(6 - floor(5 * (game_data["day"]/100)), 1)  
        schedule_action(
            {
                "type" : ACTION_TYPE_CUSTOMER_ARRIVE,
                "time" : randint(next_customer_time_mid - 1, next_customer_time_mid + 1)
            }
        )
        print("Pelanggan datang!")


def schedule_action(action: dict) -> str:
    action_id = hex(int(time()))
    if action["time"] <= 0:
        do_delayed_action(action)
        return action_id
    action_timer[action_id] = action
    return action_id


def day_start() -> None:
    global turn
    turn = 24
    game_data["day"] += 1
    for w in game_data["worker"]:
        game_data["worker"][w]["status"] = WORKER_STATUS_WAITING_FOR_COMMAND
    schedule_action(
        {
            "type" : ACTION_TYPE_CUSTOMER_ARRIVE,
            "time" : max(6 - floor(5 * (game_data["day"]/100)), 1)
        }
    )


def update_table() -> str:
    table.clear()
    table_count: int = game_data["furniture"]["table"]
    chair_count: int = game_data["furniture"]["chair"]
    for i in range(table_count):
        if not chair_count > 0:
            continue
        table_count -= 1
        if not (chair_count - 2) < 0:
            table[f"table{i}"] = {
                "capacity" : 2,
                "customer" : {}
            }
            chair_count -= 2
            continue
        table[f"table{i}"] = {
            "capacity" : 1,
            "customer" : {}
        }
        chair_count -= 1
    if game_data["furniture"]["table"] == 0 and 0 == game_data["furniture"]["chair"]:
        return "Belum ada meja dan kursi."
    if table_count > chair_count:
        return f"Meja tanpa kursi: {table_count}"
    if table_count < chair_count:
        return f"Kursi tanpa meja: {chair_count}"
    return "Meja dan kursi tertata dengan rapi."


# Gameplay function ^o^
def main_menu() -> None:
    while True:
        print("\n<>TERMINAL RESTAURANT<>")
        print("1 - Start\n2 - Option\n3 - Save & Quit")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 3)
        if pilihan == 1:
            game()
        elif pilihan == 2:
            option()
        elif pilihan == 3:
            with open("game_data.json", "w") as f:
                json.dump(game_data, f)
            break
        

def game() -> None:
    global unread_notif
    update_table()
    while True:
        notif_str = f'Notif{f"({len(unread_notif)})" if len(unread_notif) > 0 else ""}'
        menu_list: list
        if turn == -1:
            menu_list = ['Cek Pekerja', 'Furnitur', 'Market', 'Stok', 'Main Menu']
        else:
            menu_list = ['Meja Kasir', 'Dapur', 'Cek Pekerja', notif_str, 'Market', 'Stok', 'Main Menu']
        print(
f"""
*-====DAY {game_data["day"]}====-*
Turn: {"FREE" if turn == -1 else turn}
Money: {dot_format(game_data["money"])}
1 - {"Mulai hari" if turn == -1 else "Tunggu(-1 TURN)"}"""
        )
        for i in range(len(menu_list)):
            print(f"{i + 2} - {menu_list[i]}")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 7)
        if pilihan == 1:
            if not turn == -1:
                decrease_turn(1)
                continue
            day_start()
        elif pilihan == find_in_list(menu_list, "Dapur") + 2:
            kitchen()
        elif pilihan == find_in_list(menu_list, "Meja Kasir") + 2:
            cashier_desk()
        elif pilihan == find_in_list(menu_list, "Cek Pekerja") + 2:
            worker()
        elif pilihan == find_in_list(menu_list, "Market") + 2:
            market()
        elif pilihan == find_in_list(menu_list, "Furnitur") + 2:
            furniture()
        elif pilihan == find_in_list(menu_list, "Stok") + 2:
            stock()
        elif pilihan == find_in_list(menu_list, notif_str) + 2:
            notification()
        elif pilihan == find_in_list(menu_list, "Main Menu") + 2:
            return


def cashier_desk() -> None:
    while True:
        print(
"""
$> Meja Kasir <$
1 - Layani Pelanggan
2 - Suruh Layani Pelanggan
3 - Pesanan Menunggu
4 - Back
"""
        )
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 4)
        if pilihan == 1:
            pass
        elif pilihan == 4:
            return


def notification() -> None:
    print()
    if len(read_notif) + len(unread_notif) <= 0:
        print("Belum ada notifikasi.")
        input("Enter...")
        return
    for n in read_notif:
        print(f"- {n}")
    for n in unread_notif:
        print(f"+ {n}")
        read_notif.append(n)
    unread_notif.clear()
    print(
"""1 - Clear
2 - Back"""
    )
    pilihan = input_int_in_range("Masukkan pilihan: ", 1, 2)
    if pilihan == 1:
        read_notif.clear()
        return
    elif pilihan == 2:
        return


def day_end() -> None:
    global turn
    action_timer.clear()
    customer_line.clear()
    read_notif.clear()
    unread_notif.clear()
    kitchen_data["food_ready"].clear()
    for w in game_data["worker"]:
        game_data["worker"][w]["status"] = WORKER_STATUS_SLEEPING
    turn = -1
    if len(income) <= 0:
        print("\n-+=====DAY END=====+-")
        sleep(0.5)
        print(
"""
+-------------------+
| Pendapatan: 0 -_- |
+-------------------+
"""
        )
        input("Enter...")
        return
    reveal_delay = 0.3
    total: int = 0
    length = 0
    for i in income:
        length = len(dot_format(i)) if len(dot_format(i)) > length else length
        total += i
    length = len(dot_format(total)) if len(dot_format(total)) > length else length
    print(f'\n-+{"=" * round((5 + length) / 2)}DAY END{"=" * round((5 + length) / 2)}+-')
    sleep(0.5)
    print(
f"""
+-------------{"-" * length}-+
| Pendapatan: {" " * (length - len(dot_format(income[0])))}{dot_format(income[0])} |"""
    )
    for i in range(len(income) - 1):
        sleep(reveal_delay)
        print(f"|             {' ' * (length - len(dot_format(income[i])))}{dot_format(income[i])} |")
    print(f'|             {"-" * length}+|')
    sleep(reveal_delay)
    print(
f"""|             {' ' * (length - len(dot_format(total)))}{dot_format(total)} |
+-------------{"-" * length}-+
"""
    )
    input("Enter...")
    income.clear()


def furniture() -> None:
    while True:
        menu_list: list = []
        if "table" in game_data["stock"]:
            menu_list.append("Tambahkan Meja")
        if "chair" in game_data["stock"]:
            menu_list.append("Tambahkan Kursi")
        if game_data["furniture"]["table"] > 0:
            menu_list.append("Kurangi Meja")
        if game_data["furniture"]["chair"] > 0:
            menu_list.append("Kurangi Kursi")
        menu_list.append("Back")
        calculation_result = update_table()
        furnitures = list(table.keys())
        print("\n_-% Furniture %-_")
        for i in range(len(furnitures)):
            print(f"- Meja#{i + 1}: {table[furnitures[i]]['capacity']} kursi")
        print(calculation_result)
        print("^" * (len(calculation_result) + 1))
        for i in range(len(menu_list)):
            print(f"{i + 1} - {menu_list[i]}")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 5)
        if pilihan == find_in_list(menu_list, "Tambahkan Meja") + 1:
            print(f"\nMeja di stok: {get_unit_formatted(game_data['stock']['table']['amount'], game_data['stock']['table']['capacity_type'])}")
            jumlah = min(max(input_safe_int("Masukkan jumlah: "), 0), game_data["stock"]["table"]["amount"])
            game_data["stock"]["table"]["amount"] -= jumlah
            game_data["furniture"]["table"] += jumlah
            if game_data["stock"]["table"]["amount"] <= 0:
                game_data["stock"].pop("table")
        elif pilihan == find_in_list(menu_list, "Tambahkan Kursi") + 1:
            print(f"\nKursi di stok: {get_unit_formatted(game_data['stock']['chair']['amount'], game_data['stock']['chair']['capacity_type'])}")
            jumlah = min(max(input_safe_int("Masukkan jumlah: "), 0), game_data["stock"]["chair"]["amount"])
            game_data["stock"]["chair"]["amount"] -= jumlah
            game_data["furniture"]["chair"] += jumlah
            if game_data["stock"]["chair"]["amount"] <= 0:
                game_data["stock"].pop("chair")
        elif pilihan == find_in_list(menu_list, "Kurangi Meja") + 1:
            jumlah = min(max(input_safe_int("Masukkan jumlah: "), 0), game_data["furniture"]["table"])
            game_data["furniture"]["table"] -= jumlah
            if not "table" in game_data["stock"]:
                game_data["stock"]["table"] = {
                    "display_name" : "Meja",
                    "amount" : 0,
                    "capacity_type" : "quantity"
                }
            game_data["stock"]["table"]["amount"] += jumlah
        elif pilihan == find_in_list(menu_list, "Kurangi Kursi") + 1:
            jumlah = min(max(input_safe_int("Masukkan jumlah: "), 0), game_data["furniture"]["chair"])
            game_data["furniture"]["chair"] -= jumlah
            if not "chair" in game_data["stock"]:
                game_data["stock"]["chair"] = {
                    "display_name" : "Kursi",
                    "amount" : 0,
                    "capacity_type" : "quantity"
                }
            game_data["stock"]["chair"]["amount"] += jumlah
        elif pilihan == find_in_list(menu_list, "Back") + 1:
            return


def kitchen() -> None:
    while True:
        print(
f"""
/~| Dapur |~\\
Nasi: {get_unit_formatted(kitchen_data["nasi"], "cooked_rice_capacity")}
1 - Masak(TURN LOSS)
2 - Suruh Masak
3 - Batalkan Perintah
4 - Cek Makanan
5 - Back"""
        )
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 5)
        if pilihan == 1:
            cook()
        elif pilihan == 2:
            chef_available: bool = False
            for w in game_data["worker"]:
                if game_data["worker"][w]["type"] == WORKER_TYPE_CHEF and game_data["worker"][w]["status"] == WORKER_STATUS_WAITING_FOR_COMMAND:
                    command_cook(w)
                    chef_available = True
                    break
            if chef_available:
                continue
            print("Semua chef sedang sibuk.")
            input("Enter...")
        elif pilihan == 3:
            cancel_command_cook()
        elif pilihan == 4:
            if len(kitchen_data["food_ready"]) <= 0:
                print("\nBelum ada makanan yang siap.")
                input("Enter...")
                continue
            print("\n~~/Makanan Siap\\~~")
            for m in kitchen_data["food_ready"]:
                print(f"- {kitchen_data['food_ready'][m]['display_name']}: {kitchen_data['food_ready'][m]['amount']}")
            input("Enter...")
        elif pilihan == 5:
            return


def cancel_command_cook() -> None:
    while True:
        cook_commands = []
        for a in action_timer:
            if action_timer[a]["type"] == ACTION_TYPE_FOOD_READY:
                cook_commands.append(a)
        if len(cook_commands) <= 0:
            print("Tidak ada yang sedang masak.")
            input("Enter...")
            return
        print("\n!> Batalkan Perintah Masak <!")
        for c in range(len(cook_commands)):
            print(f'{c + 1} - {action_timer[cook_commands[c]]["action_data"]["chef"].capitalize()}: Memasak {action_timer[cook_commands[c]]["action_data"]["food_data"]["display_name"]}')
        print(f"{len(cook_commands) + 1} - Back")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, len(cook_commands) + 1) 
        if pilihan == len(cook_commands) + 1:
            return
        game_data["worker"][action_timer[cook_commands[pilihan - 1]]["action_data"]["chef"]]["status"] = WORKER_STATUS_WAITING_FOR_COMMAND
        action_timer.pop(cook_commands[pilihan - 1])
        cook_commands.pop(pilihan - 1)
        if len(cook_commands) <= 0:
            return
            



def cook() -> None:
    while True:
        recipes = list(game_data["recipe"].keys())
        print("\n+~Masakan~+")
        for f in range(len(recipes)):
            ingredients: str = ""
            for i in game_data["recipe"][recipes[f]]["material"]:
                ingredients += f"{get_unit_formatted(game_data['recipe'][recipes[f]]['material'][i]['amount'], game_data['recipe'][recipes[f]]['material'][i]['capacity_type'], False)} {game_data['recipe'][recipes[f]]['material'][i]['display_name']}, "
            ingredients += f"{game_data['recipe'][recipes[f]]['time']} TURN"
            print(f"{f + 1} - {game_data['recipe'][recipes[f]]['display_name']}: {ingredients}")
        print(f"{len(recipes) + 1} - Cancel")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, len(recipes) + 1)
        material_available: bool = True
        if pilihan == len(recipes) + 1:
            return
        for m in game_data["recipe"][recipes[pilihan - 1]]["material"]:
            if not m == "nasi":
                if game_data["stock"][m]["amount"] < game_data["recipe"][recipes[pilihan - 1]]["material"][m]["amount"]:
                    print("Bahan-Bahan kurang.")
                    input("Enter...")
                    material_available = False
                    break
                game_data["stock"][m]["amount"] -= game_data["recipe"][recipes[pilihan - 1]]["material"][m]["amount"]
                continue
            if kitchen_data["nasi"] < game_data["recipe"][recipes[pilihan - 1]]["material"][m]["amount"]:
                print("Bahan-Bahan kurang.")
                input("Enter...")
                material_available = False
                break
            kitchen_data["nasi"] = round(kitchen_data["nasi"] - game_data["recipe"][recipes[pilihan - 1]]["material"][m]["amount"], 2)
        if not material_available:
            continue
        decrease_turn(game_data["recipe"][recipes[pilihan - 1]]["time"])
        if recipes[pilihan - 1] == "nasi":
            kitchen_data["nasi"] = min(game_data["cooked_rice_capacity"], kitchen_data["nasi"] + game_data["recipe"][recipes[pilihan - 1]]["amount"])
            return
        if not recipes[pilihan - 1] in kitchen_data["food_ready"]:
            kitchen_data["food_ready"][recipes[pilihan - 1]] = {
                "display_name" : game_data["recipe"][recipes[pilihan - 1]]["display_name"],
                "amount" : game_data["recipe"][recipes[pilihan - 1]]["amount"]
            }
            return
        kitchen_data["food_ready"][recipes[pilihan - 1]]["amount"] += game_data["recipe"][recipes[pilihan - 1]]["amount"]
        return
        


def command_cook(chef: str) -> None:
    while True:
        recipes = list(game_data["recipe"].keys())
        print("\n+~Masakan~+")
        for f in range(len(recipes)):
            ingredients: str = ""
            for i in game_data["recipe"][recipes[f]]["material"]:
                ingredients += f"{get_unit_formatted(game_data['recipe'][recipes[f]]['material'][i]['amount'], game_data['recipe'][recipes[f]]['material'][i]['capacity_type'], False)} {game_data['recipe'][recipes[f]]['material'][i]['display_name']}, "
            ingredients += f"{game_data['recipe'][recipes[f]]['time']} TURN"
            print(f"{f + 1} - {game_data['recipe'][recipes[f]]['display_name']}: {ingredients}")
        print(f"{len(recipes) + 1} - Cancel")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, len(recipes) + 1)
        material_available: bool = True
        if pilihan == len(recipes) + 1:
            return
        for m in game_data["recipe"][recipes[pilihan - 1]]["material"]:
            if not m == "nasi":
                if game_data["stock"][m]["amount"] < game_data["recipe"][recipes[pilihan - 1]]["material"][m]["amount"]:
                    print("Bahan-Bahan kurang.")
                    input("Enter...")
                    material_available = False
                    break
                game_data["stock"][m]["amount"] -= game_data["recipe"][recipes[pilihan - 1]]["material"][m]["amount"]
                continue
            if kitchen_data["nasi"] < game_data["recipe"][recipes[pilihan - 1]]["material"][m]["amount"]:
                print("Bahan-Bahan kurang.")
                input("Enter...")
                material_available = False
                break
            kitchen_data["nasi"] = round(kitchen_data["nasi"] - game_data["recipe"][recipes[pilihan - 1]]["material"][m]["amount"], 2)
        if not material_available:
            continue
        game_data["worker"][chef]["status"] = WORKER_STATUS_WORKING
        game_data["worker"][chef]["action"] = schedule_action(
            {
            "type" : ACTION_TYPE_FOOD_READY,
            "time" : game_data["recipe"][recipes[pilihan - 1]]["time"],
            "action_data" : {
                "chef" : chef,
                "food" : recipes[pilihan - 1],
                "food_data" : {
                    "display_name" : game_data["recipe"][recipes[pilihan - 1]]["display_name"],
                    "amount" : game_data["recipe"][recipes[pilihan - 1]]["amount"]
                    }
                }
            }
        )
        return


def market() -> None:
    while True:
        market_items = list(game_data["market"].keys())
        print(
f"""
$$$ MARKET $$$
==============
Money: {dot_format(game_data["money"])}"""
        )
        for i in range(len(market_items)):
            item = game_data['market'][market_items[i]]
            item_type = item['type']
            if item_type == TYPE_INGREDIENT:
                print(f"{i + 1} - {item['display_name']} {get_unit_formatted(item['amount'], item['capacity_type'], False)}: {dot_format(item['cost'])}")
            elif item_type == TYPE_WORKER or item_type == TYPE_RECIPE:
                print(f"{i + 1} - {item['display_name']}: {dot_format(item['cost'])}")
        print(f"{len(market_items) + 1} - Back")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, len(market_items) + 1)
        if pilihan == len(market_items) + 1:
            return
        elif pilihan == len(market_items) + 2:
            return
        else:
            market_item_inspect(market_items[pilihan - 1])
        

def market_item_inspect(item: str) -> None:
    count: int = 1
    while True:
        market_item = game_data["market"][item]
        cost = market_item["cost"] * count
        display_text = f'{market_item["display_name"]} {get_unit_formatted(market_item["amount"], market_item["capacity_type"], False) if (market_item["type"] == TYPE_INGREDIENT and not market_item["capacity_type"] == "quantity") else ""} x{count}'
        length = len(display_text)
        display_cost = f'Harga: {dot_format(cost)}'
        if len(display_cost) > length:
            length = len(display_cost)
        print(
f"""
Money: {dot_format(game_data["money"])}
=={"=" * length}==
| {display_text}{" " * (length - len(display_text))} |
| {display_cost}{" " * (length - len(display_cost))} |
=={"=" * length}==
1 - {"Beli" if turn == -1 else "Beli(-1 TURN)"}"""
        )
        if not market_item["type"] == TYPE_RECIPE:
            print("2 - Ubah Jumlah")
            print("3 - Back")
        else:
            print("2 - Back")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 3)
        if pilihan == 1:
            if not turn == -1:
                decrease_turn(1)
            if game_data["money"] < cost:
                print("Uang tidak cukup.")
                input("Enter...")
                return
            game_data["money"] -= cost
            if market_item["type"] == TYPE_INGREDIENT:
                if not (item in game_data["stock"].keys()):
                    game_data["stock"][item] = {
                        "display_name" : market_item["display_name"],
                        "amount" : count * market_item["amount"],
                        "capacity_type" : market_item["capacity_type"]
                    }
                    return
                if market_item["capacity_type"] == "kecap":
                    game_data["stock"][item]["amount"] = game_data["stock"][item]["amount"] + (count * market_item["amount"])
                    return
                if market_item["capacity_type"] == "quantity":
                    game_data["stock"][item]["amount"] += count
                    return
                game_data["stock"][item]["amount"] = min(game_data["stock"][item]["amount"] + (count * market_item["amount"]), game_data[market_item["capacity_type"]]) 
                return
            elif market_item["type"] == TYPE_RECIPE:
                game_data["recipe"][item] = market_item["item_data"]
                game_data["market"].pop(item)
                return
            elif market_item["type"] == TYPE_WORKER:
                for i in range(count):
                    game_data[item] += 1
                    game_data["worker"][f"{item}#{game_data[item]}"] = dict(market_item["item_data"])
                    if not turn == -1:
                        game_data["worker"][f"{item}#{game_data[item]}"]["status"] = WORKER_STATUS_WAITING_FOR_COMMAND
                return
        elif pilihan == 2:
            if market_item["type"] == TYPE_RECIPE:
                return
            count = int(max(min(input_safe_int("Masukkan jumlah: "), (game_data["money"] - (game_data["money"] % market_item["cost"])) / market_item["cost"]), 1))
        elif pilihan == 3:
            return


def stock() -> None:
    while True:
        print("\n/||STOCK||\\")
        length: int = 0
        for i in game_data["stock"].keys():
            display_text: str = f"{game_data['stock'][i]['display_name']}: {get_unit_formatted(game_data['stock'][i]['amount'], game_data['stock'][i]['capacity_type'])}" 
            print(display_text)
            if len(display_text) > length:
                length = len(display_text)
        print("-" * (length + 1))
        print(
"""1 - Cek Buku Resep
2 - Back"""
        )
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 2)
        if pilihan == 1:
            recipe()
        elif pilihan == 2:
            return
    

def recipe() -> None:
    while True:
        recipes = list(game_data["recipe"].keys()) 
        print("\n~Buku Resep~")
        for i in range(len(recipes)):
            print(f"{i + 1} - {game_data['recipe'][recipes[i]]['display_name']}")
        print(f"{len(recipes) + 1} - Back")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, len(recipes) + 1)
        if pilihan == len(recipes) + 1:
            return
        selected_recipe: dict = game_data["recipe"][recipes[pilihan - 1]]
        recipe_material: dict = selected_recipe["material"]
        print(
f"""
{selected_recipe["display_name"]}
{"=" * (len(selected_recipe["display_name"]) + 1)}
Deskripsi: {selected_recipe["description"]}
Hasil: {get_unit_formatted(selected_recipe["amount"], selected_recipe["capacity_type"], False)}
Harga: {dot_format(selected_recipe["cost"])}
Bahan-Bahan:"""
        )
        for i in recipe_material:
            print(f"- {recipe_material[i]['display_name']}: {get_unit_formatted(recipe_material[i]['amount'], recipe_material[i]['capacity_type'], False)}")
        print(f"Waktu: {selected_recipe['time']}x Kecepatan Memasak")
        input("Enter...")


def worker() -> None:
    while True:
        print("\n/-Worker-\\")
        workers = list(game_data["worker"].keys())
        for i in range(len(workers)):
            print(f"{i+1} - {workers[i].capitalize()}")
        print(f"{len(workers) + 1} - Back")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, len(workers) + 1)
        if pilihan == len(workers) + 1:
            return
        else:
            specific_worker(workers[pilihan - 1])


def specific_worker(worker: str) -> None:
    print(game_data["worker"][worker])
    while True:
        status = game_data["worker"][worker]["status"]
        print(
f"""
{worker.capitalize()}
{"=" * len(worker) * 2}
Deskripsi: {game_data["worker"][worker]["description"]}
{"Kecepatan Memasak" if game_data["worker"][worker]["type"] == WORKER_TYPE_CHEF else "Kecepatan Melayani"}: {game_data["worker"][worker]["speed"]} TURN
Status: {"Tidur" if status == WORKER_STATUS_SLEEPING else ("Menunggu perintah" if status == WORKER_STATUS_WAITING_FOR_COMMAND else "Memasak")}
{"=" * len(worker) * 2}"""
        )
        print(
"""1 - Pecat
2 - Back"""
        )
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 2)
        if pilihan == 2:
            return
        elif pilihan == 1:
            chef_count: int = 0
            for i in game_data["worker"].keys():
                if game_data["worker"][i]["type"] == WORKER_TYPE_CHEF:
                    chef_count += 1
            if not chef_count > 1 and game_data["worker"][worker]["type"] == WORKER_TYPE_CHEF:
                print("Tidak bisa memecat chef jika chef hanya 1.")
                input("Enter...")
                continue
            if status == WORKER_STATUS_WORKING:
                while True:
                    user_input = input(f'Chef ini sedang memasak {action_timer[game_data["worker"][worker]["action"]]["action_data"]["food_data"]["display_name"]}. Apakah kamu yakin?(y/n): ')
                    if user_input.lower() == "y":
                        action_timer.pop(game_data["worker"][worker]["action"])
                        game_data["worker"].pop(worker)
                        return
                    if user_input.lower() == "n":
                        break
                    continue
                continue
            game_data["worker"].pop(worker)
            return


def option() -> None:
    while True:
        print(
"""
--> OPTION <--
1 - Satuan
2 - Back"""
        )
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 2)
        if pilihan == 1:
            print(
f"""
[Satuan] : Satuan yang dipilih untuk stok
1 - g {"<- Terpilih" if game_data["option"]["satuan"] == G else ""}
2 - Kg {"<- Terpilih" if game_data["option"]["satuan"] == KG else ""}
3 - Persen {"<- Terpilih" if game_data["option"]["satuan"] == PERCENT else ""}"""
        )
            pilihan_satuan = input_int_in_range("Masukkan pilihan: ", 1, 3)
            if pilihan_satuan == 1:
                game_data["option"]["satuan"] = G
            elif pilihan_satuan == 2:
                game_data["option"]["satuan"] = KG
            elif pilihan_satuan == 3:
                game_data["option"]["satuan"] = PERCENT
        if pilihan == 2:
            return


if __name__ == "__main__":
    if not load_game_data() == LOAD_CORRUPTED:
        main_menu()