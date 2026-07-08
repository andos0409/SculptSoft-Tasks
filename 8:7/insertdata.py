from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import date
from decimal import Decimal
from models import (
    Category,
    Supplier,
    Product,
    Warehouse,
    InventoryStock,
    Customer,
    CustomerOrder,
    CustomerOrderItem,
    StockMovement,
)

engine = create_engine("sqlite:///inventory.db")

category1 = Category(
    CategoryID=1,
    CategoryName="Electronics",
    CategoryDescription="Electronic devices and accessories"
)

supplier1 = Supplier(
    SupplierID=1,
    SupplierName="TechWorld Supplies",
    SupplierEmail="contact@techworld.com",
    SupplierPhone="0400123456",
    SupplierAddress="45 Collins Street, Melbourne"
)

warehouse1 = Warehouse(
    WarehouseID=1,
    WarehouseName="Main Warehouse",
    WarehouseAddress="12 Industrial Road",
    WarehouseCity="Melbourne",
    WarehousePhone="0399998888"
)

product1 = Product(
    ProductID=1,
    ProductName="Mechanical Keyboard",
    SKU="KEY-001",
    ProductDescription="RGB mechanical keyboard",
    SellingPrice=Decimal("129.99"),
    CostPrice=Decimal("75.00"),
    ReorderLevel=10,
    CategoryID=1,
    SupplierID=1
)

inventory_stock1 = InventoryStock(
    ProductID=1,
    WarehouseID=1,
    QuantityAvailable=50,
    LastStockUpdateDate=date(2026, 7, 8)
)

customer1 = Customer(
    CustomerID=1,
    CustomerName="John Smith",
    CustomerEmail="johnsmith@example.com",
    CustomerPhone="0411222333",
    CustomerAddress="88 Swanston Street, Melbourne"
)

customer_order1 = CustomerOrder(
    OrderID=1,
    CustomerID=1,
    OrderDate=date(2026, 7, 8),
    OrderStatus="Processing",
    PaymentStatus="Paid",
    ShippingAddress="88 Swanston Street, Melbourne"
)

customer_order_item1 = CustomerOrderItem(
    OrderID=1,
    ProductID=1,
    QuantityOrdered=2,
    UnitSalePrice=Decimal("129.99")
)

stock_movement1 = StockMovement(
    MovementID=1,
    ProductID=1,
    WarehouseID=1,
    OrderID=1,
    MovementType="Sale",
    MovementQuantity=-2,
    MovementDate=date(2026, 7, 8),
    MovementNotes="Customer order fulfilled"
)

with Session(engine) as session:
    session.add_all([
        category1,
        supplier1,
        warehouse1,
        product1,
        inventory_stock1,
        customer1,
        customer_order1,
        customer_order_item1,
        stock_movement1
    ])

    session.commit()
    

