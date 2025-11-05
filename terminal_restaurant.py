import json

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
game_data: dict = {
    "day" : 0,
    "money" : 125000,
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
            "amount": "UNLIMITED",
            "capacity_type" : "kecap"
        },
    },
    "recipe" : {
        "nasi" : {
            "display_name" : "Nasi",
            "description" : "Makanan wajib orang Asia.",
            "amount" : 1.5,
            "time" : 2,
            "material" : {
                 "beras" : {
                    "display_name" : "Beras",
                    "amount" : 0.5,
                    "capacity_type" : "rice_capacity"
                }
            },
            "capacity_type" : "cooked_rice_capacity"
        },
        "nasgor" : {
            "display_name" : "Nasi Goreng",
            "description" : "Beras yang direbus, kemudian digoreng.",
            "amount" : 1,
            "time" : 1,
            "material" : {
                "nasi" : {
                    "display_name" : "Nasi",
                    "amount" : 0.1,
                    "capacity_type" : "rice_capacity"
                },
                "rempah" : {
                    "display_name" : "Rempah-Rempah",
                    "amount": 0.05,
                    "capacity_type" : "spice_capacity"
                },
                "kecap" : {
                    "display_name" : "Kecap",
                    "amount": 7,
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
                "material" : {
                    "nasi" : {
                        "display_name" : "Nasi",
                        "amount" : 0.1,
                        "capacity_type" : "rice_capacity"
                    },
                    "rempah" : {
                        "display_name" : "Rempah-Rempah",
                        "amount": 0.01,
                        "capacity_type" : "spice_capacity"
                    },
                    "kecap" : {
                        "display_name" : "Kecap",
                        "amount": 5,
                        "capacity_type" : "kecap"
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
process_action: dict = {

}
customer: dict = {
    
}
turn = -1
kitchen_data: dict = {
    "nasi" : 0,
    "food_ready" : {
        
    }
}
table: dict = {
    
}


# Function declaration >III<
def input_safe_int(text: str) -> int:
    pass
def input_int_in_range(text: str, min: int, max: int) -> int:
    pass
def game() -> None:
    pass
def main_menu() -> None:
    pass
def option() -> None:
    pass
def load_game_data() -> int:
    pass
def worker() -> None:
    pass
def specific_worker(worker: str) -> None:
    pass
def stock() -> None:
    pass
def get_unit_formatted(amount: int, capacity_type: str) -> str:
    pass
def money_format(num: int) -> str:
    pass
def recipe() -> None:
    pass
def market() -> None:
    pass
def market_item_inspect(item: str) -> None:
    pass
def kitchen() -> None:
    pass
def find_in_list(l: list) -> int:
    pass
def furniture() -> None:
    pass
def update_table() -> None:
    pass


# Function definiton ^_^
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


def money_format(num: int) -> str:
    return ("{:,}".format(num)).replace(",", ".")


def game() -> None:
    update_table()
    menu_list: list
    if turn == -1:
        menu_list = ['Meja Kasir', 'Cek Pekerja', 'Furnitur', 'Market', 'Stok', 'Main Menu']
    else:
        menu_list = ['Meja Kasir', 'Dapur', 'Cek Pekerja', 'Market', 'Stok', 'Main Menu']
    while True:
        print(
f"""
Turn: {"FREE" if turn == -1 else turn}/24
Money: {money_format(game_data["money"])}
1 - {"Mulai hari" if turn == -1 else "Tunggu(-1 TURN)"}"""
        )
        for i in range(len(menu_list)):
            print(f"{i + 2} - {menu_list[i]}")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 7)
        if pilihan == 1:
            pass
        elif pilihan == find_in_list(menu_list, "Dapur") + 2:
            kitchen()
        elif pilihan == find_in_list(menu_list, "Cek Pekerja") + 2:
            worker()
        elif pilihan == find_in_list(menu_list, "Market") + 2:
            market()
        elif pilihan == find_in_list(menu_list, "Furnitur") + 2:
            furniture()
        elif pilihan == find_in_list(menu_list, "Stok") + 2:
            stock()
        elif pilihan == find_in_list(menu_list, "Main Menu") + 2:
            return


def update_table() -> str:
    table.clear()
    table_count: int = game_data["furniture"]["table"]
    chair_count: int = game_data["furniture"]["chair"]
    for i in range(game_data["furniture"]["table"]):
        if not chair_count > 0:
            continue
        table_count -= 1
        if not (chair_count - 2) < 0:
            table[f"table{i}"] = {
                "capacity" : 2
            }
            chair_count -= 2
            continue
        table[f"table{i}"] = {
            "capacity" : 1
        }
        chair_count -= 1
    if game_data["furniture"]["table"] == 0 and 0 == game_data["furniture"]["chair"]:
        return "Belum ada meja dan kursi."
    if table_count > chair_count:
        return f"Meja tanpa kursi: {table_count}"
    if table_count < chair_count:
        return f"Kursi tanpa meja: {chair_count}"
    return "Meja dan kursi tertata dengan rapi."


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
            print(f"- Meja#{i + 1}: {table[furnitures[i]]["capacity"]} kursi")
        print(calculation_result)
        print("^" * (len(calculation_result) + 1))
        for i in range(len(menu_list)):
            print(f"{i + 1} - {menu_list[i]}")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 5)
        if pilihan == find_in_list(menu_list, "Tambahkan Meja") + 1:
            print(f"\nMeja di stok: {get_unit_formatted(game_data["stock"]["table"]["amount"], game_data["stock"]["table"]["capacity_type"])}")
            jumlah = min(max(input_safe_int("Masukkan jumlah: "), 0), game_data["stock"]["table"]["amount"])
            game_data["stock"]["table"]["amount"] -= jumlah
            game_data["furniture"]["table"] += jumlah
            if game_data["stock"]["table"]["amount"] <= 0:
                game_data["stock"].pop("table")
        elif pilihan == find_in_list(menu_list, "Tambahkan Kursi") + 1:
            print(f"\nKursi di stok: {get_unit_formatted(game_data["stock"]["chair"]["amount"], game_data["stock"]["chair"]["capacity_type"])}")
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
    1 - Masak
    2 - Suruh Masak
    3 - Cek Makanan
    4 - Back"""
        )
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 4)
        if pilihan == 1:
            pass
        elif pilihan == 4:
            return
    

def market() -> None:
    while True:
        market_items = list(game_data["market"].keys())
        print(
f"""
$$$ MARKET $$$
==============
Money: {money_format(game_data["money"])}"""
        )
        for i in range(len(market_items)):
            item = game_data['market'][market_items[i]]
            item_type = item['type']
            if item_type == TYPE_INGREDIENT:
                print(f"{i + 1} - {item['display_name']} {get_unit_formatted(item['amount'], item['capacity_type'], False)}: {money_format(item['cost'])}")
            elif item_type == TYPE_WORKER or item_type == TYPE_RECIPE:
                print(f"{i + 1} - {item['display_name']}: {money_format(item['cost'])}")
        print(f"{len(market_items) + 1} - Back")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, len(market_items) + 1)
        if pilihan == len(market_items) + 1:
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
        display_cost = f'Harga: {money_format(cost)}'
        if len(display_cost) > length:
            length = len(display_cost)
        print(
f"""
Money: {money_format(game_data["money"])}
=={"=" * length}==
| {display_text}{" " * (length - len(display_text))} |
| {display_cost}{" " * (length - len(display_cost))} |
=={"=" * length}==
1 - Beli"""
        )
        if not market_item["type"] == TYPE_RECIPE:
            print("2 - Ubah Jumlah")
            print("3 - Back")
        else:
            print("2 - Back")
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 3)
        if pilihan == 1:
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
                    game_data["worker"][f"{item}#{game_data[item]}"] = market_item["item_data"]
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
Bahan-Bahan:"""
        )
        for i in recipe_material:
            print(f"- {recipe_material[i]['display_name']}: {get_unit_formatted(recipe_material[i]['amount'], recipe_material[i]['capacity_type'], False)}")
        print(f"Waktu: {selected_recipe['time']}x Kecepatan Memasak")
        input("Enter...")


def get_unit_formatted(amount: int, capacity_type: str, use_ratio: bool = True) -> str:
    if capacity_type == "quantity":
        return f"x{amount}"
    if capacity_type == "kecap" and type(amount) == str:
        return f"UNLIMITED"
    if capacity_type == "kecap":
        return f"{amount}ml"
    if game_data["option"]["satuan"] == G and use_ratio:
        return f"{amount * 1000}g/{game_data[capacity_type] * 1000}g".replace(".", ",")
    if game_data["option"]["satuan"] == KG and use_ratio:
        return f"{amount}Kg/{game_data[capacity_type]}Kg".replace(".", ",")
    if game_data["option"]["satuan"] == G:
        return f"{amount * 1000}g".replace(".", ",")
    if game_data["option"]["satuan"] == KG:
        return f"{amount}Kg".replace(".", ",")
    if game_data["option"]["satuan"] == PERCENT:
        return f"{(float(amount) / game_data[capacity_type]) * 100}%".replace(".", ",")


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
            if not chef_count > 1:
                print("Tidak bisa memecat chef jika chef hanya 1.")
                input("Enter...")
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