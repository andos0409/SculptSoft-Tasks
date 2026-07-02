from db import get_connection
from models import (
    Category,
    Supplier,
    Product,
    Warehouse,
    InventoryStock,
    Customer,
    CustomerOrder,
    CustomerOrderItem,
    StockMovement
)
from datetime import date

connection = get_connection()

# ----------------------------
# CATEGORY
# ----------------------------

category1 = Category(
    1,
    "Electronics",
    "Electronic devices and accessories"
)

category2 = Category(
    2,
    "Stationery",
    "Office and school supplies"
)

category1.new_category(connection)
category2.new_category(connection)


# ----------------------------
# SUPPLIER
# ----------------------------

supplier1 = Supplier(
    1,
    "TechWorld Supplies",
    "contact@techworld.com",
    "0400000001",
    "12 Tech Street, Melbourne"
)

supplier2 = Supplier(
    2,
    "OfficeMart",
    "sales@officemart.com",
    "0400000002",
    "88 Office Road, Melbourne"
)

supplier1.new_supplier(connection)
supplier2.new_supplier(connection)


# ----------------------------
# PRODUCT
# ----------------------------

product1 = Product(
    1,
    "Wireless Mouse",
    "WM-001",
    "Bluetooth wireless mouse",
    29.99,
    15.00,
    10,
    category1.CategoryID,
    supplier1.SupplierID
)

product2 = Product(
    2,
    "Notebook",
    "NB-001",
    "A4 ruled notebook",
    4.99,
    1.50,
    20,
    category2.CategoryID,
    supplier2.SupplierID
)

product1.new_product(connection)
product2.new_product(connection)


# ----------------------------
# WAREHOUSE
# ----------------------------

warehouse1 = Warehouse(
    1,
    "Main Warehouse",
    "100 Storage Avenue",
    "Melbourne",
    "0390000001"
)

warehouse2 = Warehouse(
    2,
    "West Warehouse",
    "45 Industrial Drive",
    "Tarneit",
    "0390000002"
)

warehouse1.new_warehouse(connection)
warehouse2.new_warehouse(connection)


# ----------------------------
# INVENTORY STOCK
# ----------------------------

stock1 = InventoryStock(
    product1.ProductID,
    warehouse1.WarehouseID,
    50,
    date(2026, 7, 2),
    product1,
    warehouse1
)

stock2 = InventoryStock(
    product2.ProductID,
    warehouse1.WarehouseID,
    100,
    date(2026, 7, 2),
    product2,
    warehouse1
)

stock1.new_stock_record(connection)
stock2.new_stock_record(connection)


# ----------------------------
# CUSTOMER
# ----------------------------

customer1 = Customer(
    1,
    "Tom Andrew",
    "tom@example.com",
    "0400000101",
    "22 Customer Street, Melbourne"
)

customer2 = Customer(
    2,
    "John Smith",
    "john@example.com",
    "0400000102",
    "33 Buyer Road, Melbourne"
)

customer1.new_customer(connection)
customer2.new_customer(connection)


# ----------------------------
# CUSTOMER ORDER
# ----------------------------

order1 = CustomerOrder(
    1,
    customer1.CustomerID,
    date(2026, 7, 2),
    "Processing",
    "Paid",
    customer1.CustomerAddress,
    customer1
)

order1.new_order(connection)


# ----------------------------
# CUSTOMER ORDER ITEM
# ----------------------------

order_item1 = CustomerOrderItem(
    order1.OrderID,
    product1.ProductID,
    2,
    product1.SellingPrice,
    order1,
    product1
)

order_item1.new_order_item(connection)


# ----------------------------
# REDUCE INVENTORY STOCK
# ----------------------------

stock1.remove_stock(
    connection,
    order_item1.QuantityOrdered,
    date(2026, 7, 2)
)


# ----------------------------
# STOCK MOVEMENT
# ----------------------------

movement1 = StockMovement(
    1,
    product1.ProductID,
    warehouse1.WarehouseID,
    order1.OrderID,
    "OUT",
    order_item1.QuantityOrdered,
    date(2026, 7, 2),
    "Stock reduced due to customer order",
    product1,
    warehouse1,
    order1
)

movement1.new_movement(connection)


# ----------------------------
# UPDATE ORDER STATUS
# ----------------------------

order1.update_order_status(connection, "Shipped")