import datetime
import csv
import os
from date import get_day


def create_inventory_report():
    try:
        os.remove("inventory.csv")
    except FileNotFoundError:
        pass
    with open("sold.csv", "r") as sold_file:
        sold_item_list = []
        reader = csv.DictReader(sold_file)
        today = int(get_day().strftime("%Y%m%d"))
        for line in reader:
            sell_date = line["sell_date"]
            sell_date_int = int(
                datetime.datetime.strptime(sell_date, "%Y-%m-%d").strftime("%Y%m%d")
            )
            if sell_date_int <= today:
                sold_item_list.append(line["bought_id"])
    with open("bought.csv", "r") as bought_file:
        reader = csv.DictReader(bought_file)
        for line in reader:
            if line["id"] not in sold_item_list:
                bought_date = line["buy_date"]
                bought_date_int = int(
                    datetime.datetime.strptime(bought_date, "%Y-%m-%d").strftime(
                        "%Y%m%d"
                    )
                )
                if bought_date_int <= today:
                    exp_date = line["exp_date"]
                    exp_date_int = int(
                        datetime.datetime.strptime(exp_date, "%Y-%m-%d").strftime(
                            "%Y%m%d"
                        )
                    )
                    if exp_date_int > today:
                        with open("inventory.csv", "a", newline="") as inventory_file:
                            fields = [
                                "id",
                                "product_name",
                                "buy_date",
                                "buy_price",
                                "exp_date",
                            ]
                            writer = csv.DictWriter(inventory_file, fieldnames=fields)
                            writer.writerow(line)


def create_revenue_report():
    with open("sold.csv", "r") as sold_file:
        sold_item_list = []
        day = get_day()
        today = day.strftime("%Y-%m-%d")
        reader = csv.DictReader(sold_file)
        for line in reader:
            if today == line["sell_date"]:
                sold_item_list.append(float(line["sell_price"]))
        revenue = sum(sold_item_list)
        return revenue


def create_profit_report():
    with open("sold.csv", "r") as sold_file:
        sold_item_id_list = []
        day = get_day()
        today = day.strftime("%Y-%m-%d")
        reader = csv.DictReader(sold_file)
        for line in reader:
            if today == line["sell_date"]:
                sold_item_id_list.append(line["bought_id"])
    with open("bought.csv", "r") as bought_file:
        price_list = []
        reader = csv.DictReader(bought_file)
        for line in reader:
            if line["id"] in sold_item_id_list:
                price_list.append(float(line["buy_price"]))
        cost = sum(price_list)
        revenue = create_revenue_report()
        profit = revenue - cost
        return round(profit, 2)
