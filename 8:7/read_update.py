from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Warehouse, Supplier, Product

engine = create_engine("sqlite:///inventory.db")

with Session(engine) as session:
    statement = select(Warehouse).where(Warehouse.WarehouseCity == "Melbourne")

    rows = session.scalars(statement).all()
    for row in rows:
        print(
            row.WarehouseID, '|', row.WarehouseName
        )

    statement2 = select(
                    Supplier.SupplierName, 
                    Product.ProductName
                ).join(Product, Product.SupplierID == Supplier.SupplierID)
    
    rows = session.execute(statement2).all()
    for row in rows:
        print(
            row.SupplierName, '|', row.ProductName
        )

    session.commit()