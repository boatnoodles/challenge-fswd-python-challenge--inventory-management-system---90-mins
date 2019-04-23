class Store():
    def __init__(self, owner):
        self.owner = owner
        self.warehouses = []

    def add_warehouse(self, warehouse):
        self.warehouses.append(warehouse)

    def __repr__(self):

        return f"This is owned by {self.owner}"


class Warehouse():
    def __init__(self, address):
        self.address = address
        self.products = []

    def add_product(self, product):
        self.products.append(product.name)

    def check_availability(self, product):
        return product in self.products


class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity += quantity


ttdi_fam_mart = Store("Hiroshi")
damansara_warehouse = Warehouse("1 Jalan Damansara")
ttdi_fam_mart.add_warehouse(damansara_warehouse)
bandar_utama_warehouse = Warehouse("1 Jalan Utama")
ttdi_fam_mart.add_warehouse(bandar_utama_warehouse)
daikon_soup = Product("Daikon soup", 5, 10)
damansara_warehouse.add_product(daikon_soup)

print(ttdi_fam_mart.owner)
print(ttdi_fam_mart.warehouses)
print(damansara_warehouse)
print(damansara_warehouse.products)
print(daikon_soup.name)
print(damansara_warehouse.check_availability("Daikon soup"))
print(ttdi_fam_mart)
