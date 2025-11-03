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
TYPE_INGREDIENT = 0
TYPE_WORKER = 1
TYPE_RECIPE = 2
game_data: dict = {
    "day" : 0,
    "money" : 125000,
    "option" : {
        "satuan" : KG
    },
    "worker" : {
        "chef#1" : {
            "description" : "Teman terbaikmu sejauh ini.",
            "speed" : 1,
            "status" : WORKER_STATUS_SLEEPING
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
        "chef" : {
            "display_name" : "Chef",
            "cost" : 250000,
            "type" : TYPE_WORKER
        },
        "cashier" : {
            "display_name" : "Kasir",
            "cost" : 500000,
            "type" : TYPE_WORKER
        },
        "chicken_recipe" : {
            "display_name" : "Resep Nasi Ayam",
            "cost" : 100000,
            "type" : TYPE_RECIPE
        },
        "chicken" : {
            "display_name" : "Ayam",
            "amount" : 1,
            "capacity_type" : "quantity",
            "cost" : 10000,
            "type" : TYPE_INGREDIENT
        }
    }
}
turn = -1


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


# Function definiton ^_^
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
    while True:
        print(
f"""
Turn: {"FREE" if turn == -1 else turn}/24
Money: {money_format(game_data["money"])}
1 - {"Mulai hari" if turn == -1 else "Tunggu(-1 TURN)"}
2 - Meja Kasir
3 - Cek Pekerja
4 - Market
5 - Stok
6 - Main menu"""
        )
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 6)
        if pilihan == 1:
            pass
        elif pilihan == 3:
            worker()
        elif pilihan == 4:
            market()
        elif pilihan == 5:
            stock()
        elif pilihan == 6:
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
        display_text = f'{market_item["display_name"]} {get_unit_formatted(market_item["amount"], market_item["capacity_type"], False) if (market_item["type"] == TYPE_INGREDIENT and not market_item["capacity_type"] == "quantity") else ""} x{count}'
        length = len(display_text)
        display_cost = f'Harga: {money_format(market_item["cost"] * count)}'
        if len(display_cost) > length:
            length = len(display_cost)
        print(
f"""
=={"=" * length}==
| {display_text}{" " * (length - len(display_text))} |
| {display_cost}{" " * (length - len(display_cost))} |
=={"=" * length}==
1 - Beli
2 - Ubah Jumlah
3 - Back"""
        )
        pilihan = input_int_in_range("Masukkan pilihan: ", 1, 2)
        if pilihan == 1:
            pass
        elif pilihan == 2:
            count = input_safe_int("Masukkan jumlah: ")
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
Kecepatan Memasak: {game_data["worker"][worker]["speed"]} TURN
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
            if not len(game_data["worker"].keys()) > 1:
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
    