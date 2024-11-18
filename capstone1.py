#  yang udah dipelajarin: data collection, conditional statement, looping, regular function
# harus ada 4 fitur utama CRUD
#  VIDEOSiswa dapat menjelaskan tujuan, alur program dan kegunaan blok kode dari program dengan jelas dan terstruktur.
#  buat aplikasi melebihi standar requirement yang sudah ditentukan.
#  VIDEO jelasin, CRUD,Integrasi sistem / efisiensi kode
#  kompleksitas yang dimaksud haruslah tetap sesuai dengan materi yang sudah dipelajari dan juga
#  sesuai dengan petunjuk yang terdapat di dokumentasi ini.
# alt shift f / ctrl s = beautify python fie (extension), ini ngebantu integrasi sistem dan efisiensi kode
# Video penjelasan maksimal berdurasi 10 menit

# saya buat aplikasi toko gitar

# data collection, nampung semua yang di save kesini, anggep aja ini wadah nya
guitars = []
customers = []
transactions = []


# buat generate id pake function
def generate_id(data_list):
    return len(data_list) + 1


# nambah gitar
def add_guitar():
    # Nama gitar gk boleh kosong
    while True:
        name = input("Guitar Name: ")
        if name.strip():  # mastiin gk kosong trus ada break dikasih notif
            break
        else:
            print("Guitar name can't be empty. Please enter a valid name.")

    # Mastiin tipe gitar gk kosong
    while True:
        guitar_type = input("Guitar Type: ")
        if guitar_type.strip() and not any(
            char.isdigit() for char in guitar_type
        ):  # gak boleh ada angka karena pilihannya cuman elektrik atau acoustic, 2 tipe gitar cuman ada ini, sebenernya ada lagi kayak banjo
            break
        else:
            print("Guitar type cant be empty, try again")

    # Mastiin harga keisi dan valid
    while True:
        try:
            price = float(input("Guitar Price: "))
            if price > 0:  # mastiin harganya bener
                # ini dibuat kad
                formatted_price = "{:,.0f}".format(
                    price
                )  # nunjukin ini jadi format rupiah
                print(f"price in rupiah format: {formatted_price}")
                break
            else:
                print("Please enter a valid price.")
        except ValueError:
            print("Invalid price. Enter a valid price.")

    # Gaboleh kosong
    while True:
        try:
            stock = int(input("Guitar Stock: "))
            if stock >= 0:
                break
            else:
                print("Please enter a valid stock number.")
        except ValueError:
            print("Invalid stock. Please enter again")

    # masukin ke dictionary biar jadi data
    guitar = {
        "id": generate_id(guitars),
        "name": name,
        "type": guitar_type,
        "price": price,
        "stock": stock,
    }
    guitars.append(guitar)
    print("The guitar is successfully added :-).")


# ini nunjukin list gitar yang ada, kalo gk ada ngasih tau gk ada
def show_guitars():
    if guitars:
        print("\nGuitar Lists:")
        for guitar in guitars:
            # jadiin format rupiah
            formatted_price = "{:,.0f}".format(guitar["price"])
            # nanti keluarnya jadi format rupiah pas show guitars
            print(
                f"Id: {guitar['id']}, Name: {guitar['name']}, Type: {guitar['type']}, Price: {formatted_price}, Stock: {guitar['stock']}"
            )
    else:
        print("there are no guitars available")


# update gitar
def update_guitar():
    show_guitars()

    # akan ada loop sampe bener input gitarnya
    while True:
        guitar_id = input("Input guitar id to update: ").strip()

        # mastiin gk salah id
        if not guitar_id:
            print("Guitar id can't be empty, enter a valid id.")
            continue

        # kalo isinya kosong
        try:
            guitar_id = int(guitar_id)
        except ValueError:
            print("Invalid input, please enter a valid input for the guitar id.")
            continue

        # mastiinid ada di list gitar
        guitar = next((g for g in guitars if g["id"] == guitar_id), None)

        if guitar:
            break  # kalo id nya bener, loop nya ya berhemti
        else:
            print(f"Guitar with id {guitar_id} not found, enter valid id.")

    # validasi input nama gitar
    while True:
        name = input("New Guitar Name: ")
        if name.strip():  # mastiin gk kosong masukin update gitar
            guitar["name"] = name
            break
        else:
            print("Guitar name cannot be empty, please enter again.")

    # ada validasi input nama gitar
    while True:
        guitar_type = input("New Guitar Type: ")
        if guitar_type.strip() and not any(char.isdigit() for char in guitar_type):
            guitar["type"] = guitar_type
            break
        else:
            print(
                "Guitar type is not valid. cant be empty and no numbers, please enter again."
            )

    # ini validasi input harga gitar pake format rupiah
    while True:
        try:
            price = float(input("New Guitar Price: "))
            # mastiin pricenya lebih dari 0
            if price > 0:
                guitar["price"] = price
                # format bentuk rupiah
                formatted_price = "{:,.0f}".format(price)
                print(f"format bentuk rupiah: {formatted_price}")
                break
            else:
                print("Please enter a valid price.")
        except ValueError:
            print("Invalid price, enter a valid number.")

    # validasi input stok gitar
    while True:
        try:
            stock = int(input("New Guitar Stock: "))
            # mastiin stock lebih besar atau sama dengan nol
            if stock >= 0:
                guitar["stock"] = stock
                break
            else:
                print("please enter a valid stock number.")
        except ValueError:
            print("Invalid stock, enter a valid stock.")

    print("Guitar has been updated.")


# apus gitar
def delete_guitar():
    # guitar di jadiin global biar bisa di modify yang ada di function
    global guitars
    show_guitars()

    # akan ada kejadian loop kalo input id nya ga bener
    while True:
        try:
            guitar_id = input("Input guitar id to delete: ").strip()

            # input bener ga nih? kalo bener di continue ke algoritma berikutnya
            if not guitar_id:
                print("Guitar id can't be empty, enter  correct id please")
                continue

            guitar_id = int(guitar_id)

            # mastiin gitar id di list, kalo udah bener ya akan keluar, kalo menuhin statement if nya
            if any(guitar["id"] == guitar_id for guitar in guitars):
                break
            else:
                print(f"Guitar with ID {guitar_id} not found, please enter valid id.")

        except ValueError:
            print("Invalid input, enter a valid integer for the guitar id.")

    # apus gitar berdasarkan id yang kita pilih
    guitars = [g for g in guitars if g["id"] != guitar_id]
    print("Guitar has been deleted.")


# nambah customer
def add_customer():
    # kejadian loop sampe input nya bene, harus huruf, gk boleh kosong
    while True:
        name = input("Customer Name: ").strip()
        if name and all(
            char.isalpha() or char.isspace() for char in name
        ):  # mastiin nama gk kosogn cuman ada huruf
            break
        else:
            print(
                "Name cannot be empty and must only contain alphabetic characters and spaces (no numbers or special characters)."
            )

    # loop sampe bener
    while True:
        contact = input("Customer Contact: ").strip()
        if contact and contact.isdigit():  # angka doang
            break
        else:
            print("Contact cannot be empty and must only contain numbers.")

    # loop sampe bener
    while True:
        address = input("Customer Address: ").strip()
        # alamat gk kosong
        if address:
            break
        else:
            print("Address cannot be empty.")

    # buat dictionary trus dimasukin ke list
    customer = {
        "id": generate_id(customers),
        "name": name,
        "contact": contact,
        "address": address,
    }

    customers.append(customer)
    print("new customer has been added.")


def show_customers():
    if customers:
        print("\ncustomer List:")
        for customer in customers:
            print(customer)
    else:
        print("There are no customers available right now.")


def update_customer():
    show_customers()

    # akan ada loop sampe user maasukin
    while True:
        try:
            customerId = input("Input customer's id to update: ").strip()
            if not customerId:
                print("customer id can't be empty, please enter again.")
                continue

            customerId = int(customerId)
            customer = next((c for c in customers if c["id"] == customerId), None)

            if customer:
                break  # kalo udh bener, exit loop
            else:
                print("Customer not found, please enter a valid id.")

        except ValueError:
            print(
                "Invalid input, please enter a valid integer for the customer id that are available."
            )

    # validasi input nama lagi
    while True:
        name = input("New Customer Name: ").strip()
        if name and all(char.isalpha() or char.isspace() for char in name):
            customer["name"] = name
            break
        else:
            print("Customer can't be empty and with numbers.")

    # validasi
    while True:
        contact = input("New Customer Contact: ").strip()
        if contact and contact.isdigit():
            customer["contact"] = contact
            break
        else:
            print("contact cant be empty and should only contain numbers.")

    # validasi
    while True:
        address = input("New Customer Address: ").strip()
        if address:
            customer["address"] = address
            break
        else:
            print("Customer address cannot be empty.")

    print("Customer details have been updated.")


def delete_customer():
    global customers  # decalre customer global biar bisa dipake, bukan dalem function
    show_customers()

    # loop sampe bener
    while True:
        try:
            customerId = input("Customer ID to delete: ").strip()

            # pastiin id gk kosong
            if not customerId:
                print("Customer id cant be empty, please enter a valid ID.")
                continue

            customerId = int(customerId)

            # pastiin customer id di list
            customer = next((c for c in customers if c["id"] == customerId), None)

            if customer:
                break  # validasi bener, exit
            else:
                print(f"Customer with ID {customerId} not found, enter valid id.")

        except ValueError:
            print("Invalid input, enter a valid integer for the customer id.")

    customers = [c for c in customers if c["id"] != customerId]
    print("Customer has been deleted.")


# 3. CRUD transaksi
def add_transaction():
    # cek gitar ada atau ga
    if not guitars:
        print("No guitars are available for sell, input guitars first on guitar menu.")
        return

    # customers availabale gak? berdasarkan dari list yang dibuat
    if not customers:
        print("No customers available, please add customers first.")
        return

    show_guitars()

    # Loop sampe bener
    while True:
        try:
            guitar_id = input("Enter guitar id to buy: ").strip()

            # id gk boleh kosong
            if not guitar_id:
                print("Guitar id is empty, pleaseee enter a valid id.")
                continue

            guitar_id = int(guitar_id)  # convert integer

            # ada id nya gk dari list gitarnya?
            guitar = next((g for g in guitars if g["id"] == guitar_id), None)

            if guitar:
                break  # id bener, keluar loop
            else:
                print(f"Guitar with id: {guitar_id} not found, enter a valid id.")

        except ValueError:
            print(
                "Invalid input, enter a valid integer for the guitar id that are already available!."
            )

    # kalo gitar ada dan STOK NYA juga ada, lanjutin prosesnya
    if guitar and guitar["stock"] > 0:
        show_customers()

        # loop sampe id yang available
        while True:
            try:
                customerId = input("enter customer id: ").strip()

                # pastiin id gk kosong
                if not customerId:
                    print("customer id gk boleh kosong, please enter valid id.")
                    continue

                customerId = int(customerId)

                # Ccustomer id ada di list ga? cek dulu
                customer = next((c for c in customers if c["id"] == customerId), None)

                if customer:
                    break  # id valid, exit loop
                else:
                    print(
                        f"Customer with id: {customerId} not found, please enter a valid id."
                    )

            except ValueError:
                print(
                    "Invalid input, please enter a valid integer for the customer id."
                )

        # customer ketyemu, masukin inputnya
        if customer:
            while True:
                try:
                    quantity = int(input("Amount of guitar to buy: "))

                    if quantity <= guitar["stock"]:
                        guitar["stock"] -= quantity
                        transaction = {
                            "id": generate_id(transactions),
                            "guitar_id": guitar_id,
                            "customerId": customerId,
                            "quantity": quantity,
                        }
                        transactions.append(transaction)
                        print("Transaction has been added.")
                        break
                    else:
                        print("Not enough stock! enter a valid quantity.")
                except ValueError:
                    print("invalid quantity, enter a valid number.")
    else:
        print("guitar is not available or probably stock is insufficient.")


def show_transactions():
    if transactions:
        print("\nTransaction list: ")
        for transaction in transactions:
            guitar = next(
                (g for g in guitars if g["id"] == transaction["guitar_id"]), None
            )
            customer = next(
                (c for c in customers if c["id"] == transaction["customerId"]), None
            )
            print(
                {
                    "transaction_id": transaction["id"],
                    "guitar_name": guitar["name"] if guitar else "Unknown",
                    "customer_name": customer["name"] if customer else "Unknown",
                    "quantity": transaction["quantity"],
                }
            )
    else:
        print("there are no transactions available...")


# Menu System


def menu_utama():
    print("\n***** Welcome to Piledriver Guitar Store! *****")
    while True:
        print("\n--- Main Menu ---")
        print("1. Manage Guitar")
        print("2. Manage Customer")
        print("3. Manage Transaction")
        print("4. Exit")

        option = input("Choose Option: ")

        if option == "1":
            guitar_menu()
        elif option == "2":
            customer_menu()
        elif option == "3":
            transaction_menu()
        elif option == "4":
            print("Thank you for using this app.")
            break
        else:
            print("not valid option, try again")


def guitar_menu():
    while True:
        print("\n--- Guitar Menu ---")
        print("1. Add Guitar")
        print("2. View Guitar")
        print("3. Update Guitar")
        print("4. Delete Guitar")
        print("5. Back to Main Menu")

        option = input("Choose Option: ")

        if option == "1":
            add_guitar()
        elif option == "2":
            show_guitars()
        elif option == "3":
            update_guitar()
        elif option == "4":
            delete_guitar()
        elif option == "5":
            break
        else:
            print("not valid option, try again")


def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Add Customer")
        print("2. View Customer")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Go back")

        option = input("Choose Option: ")

        if option == "1":
            add_customer()
        elif option == "2":
            show_customers()
        elif option == "3":
            update_customer()
        elif option == "4":
            delete_customer()
        elif option == "5":
            break
        else:
            print("not valid option, try again")


def transaction_menu():
    while True:
        print("\n--- Transaction Menu ---")
        print("1. Add Transaction")
        print("2. View Transaction")
        print("3. Go Back")

        option = input("Choose Option: ")

        if option == "1":
            add_transaction()
        elif option == "2":
            show_transactions()
        elif option == "3":
            break
        else:
            print("not valid option, try again")


# jalanin aplikasi di awal pas di run
menu_utama()
