from datetime import date
from decimal import Decimal
from sqlalchemy import String, ForeignKey, Numeric, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "Category"

    CategoryID: Mapped[int] = mapped_column(primary_key=True)
    CategoryName: Mapped[str] = mapped_column(String(100), nullable=False)
    CategoryDescription: Mapped[str | None] = mapped_column(String(255))


class Supplier(Base):
    __tablename__ = "Supplier"

    SupplierID: Mapped[int] = mapped_column(primary_key=True)
    SupplierName: Mapped[str] = mapped_column(String(100), nullable=False)
    SupplierEmail: Mapped[str | None] = mapped_column(String(100))
    SupplierPhone: Mapped[str | None] = mapped_column(String(20))
    SupplierAddress: Mapped[str | None] = mapped_column(String(255))


class Product(Base):
    __tablename__ = "Product"

    ProductID: Mapped[int] = mapped_column(primary_key=True)
    ProductName: Mapped[str] = mapped_column(String(100), nullable=False)
    SKU: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    ProductDescription: Mapped[str | None] = mapped_column(String(255))

    SellingPrice: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    CostPrice: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    ReorderLevel: Mapped[int] = mapped_column(nullable=False)

    CategoryID: Mapped[int] = mapped_column(
        ForeignKey("Category.CategoryID"),
        nullable=False
    )

    SupplierID: Mapped[int] = mapped_column(
        ForeignKey("Supplier.SupplierID"),
        nullable=False
    )


class Warehouse(Base):
    __tablename__ = "Warehouse"

    WarehouseID: Mapped[int] = mapped_column(primary_key=True)
    WarehouseName: Mapped[str] = mapped_column(String(100), nullable=False)
    WarehouseAddress: Mapped[str | None] = mapped_column(String(255))
    WarehouseCity: Mapped[str | None] = mapped_column(String(100))
    WarehousePhone: Mapped[str | None] = mapped_column(String(20))


class InventoryStock(Base):
    __tablename__ = "InventoryStock"

    ProductID: Mapped[int] = mapped_column(
        ForeignKey("Product.ProductID"),
        primary_key=True
    )

    WarehouseID: Mapped[int] = mapped_column(
        ForeignKey("Warehouse.WarehouseID"),
        primary_key=True
    )

    QuantityAvailable: Mapped[int] = mapped_column(nullable=False)
    LastStockUpdateDate: Mapped[date | None] = mapped_column(Date)


class Customer(Base):
    __tablename__ = "Customer"

    CustomerID: Mapped[int] = mapped_column(primary_key=True)
    CustomerName: Mapped[str] = mapped_column(String(100), nullable=False)
    CustomerEmail: Mapped[str | None] = mapped_column(String(100), unique=True)
    CustomerPhone: Mapped[str | None] = mapped_column(String(20))
    CustomerAddress: Mapped[str | None] = mapped_column(String(255))


class CustomerOrder(Base):
    __tablename__ = "CustomerOrder"

    OrderID: Mapped[int] = mapped_column(primary_key=True)

    CustomerID: Mapped[int] = mapped_column(
        ForeignKey("Customer.CustomerID"),
        nullable=False
    )

    OrderDate: Mapped[date] = mapped_column(Date, nullable=False)
    OrderStatus: Mapped[str] = mapped_column(String(50), nullable=False)
    PaymentStatus: Mapped[str] = mapped_column(String(50), nullable=False)
    ShippingAddress: Mapped[str | None] = mapped_column(String(255))


class CustomerOrderItem(Base):
    __tablename__ = "CustomerOrderItem"

    OrderID: Mapped[int] = mapped_column(
        ForeignKey("CustomerOrder.OrderID"),
        primary_key=True
    )

    ProductID: Mapped[int] = mapped_column(
        ForeignKey("Product.ProductID"),
        primary_key=True
    )

    QuantityOrdered: Mapped[int] = mapped_column(nullable=False)
    UnitSalePrice: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)


class StockMovement(Base):
    __tablename__ = "StockMovement"

    MovementID: Mapped[int] = mapped_column(primary_key=True)

    ProductID: Mapped[int] = mapped_column(
        ForeignKey("Product.ProductID"),
        nullable=False
    )

    WarehouseID: Mapped[int] = mapped_column(
        ForeignKey("Warehouse.WarehouseID"),
        nullable=False
    )

    OrderID: Mapped[int | None] = mapped_column(
        ForeignKey("CustomerOrder.OrderID"),
        nullable=True
    )

    MovementType: Mapped[str] = mapped_column(String(50), nullable=False)
    MovementQuantity: Mapped[int] = mapped_column(nullable=False)
    MovementDate: Mapped[date] = mapped_column(Date, nullable=False)
    MovementNotes: Mapped[str | None] = mapped_column(String(255))
     
            