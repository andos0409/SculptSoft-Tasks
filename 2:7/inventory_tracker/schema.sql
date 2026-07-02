CREATE DATABASE IF NOT EXISTS inventory_db;
USE inventory_db;

-- CATEGORY
CREATE TABLE Category (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL,
    CategoryDescription VARCHAR(255)
);

-- SUPPLIER
CREATE TABLE Supplier (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(100) NOT NULL,
    SupplierEmail VARCHAR(100),
    SupplierPhone VARCHAR(20),
    SupplierAddress VARCHAR(255)
);

-- PRODUCT
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    SKU VARCHAR(50) UNIQUE NOT NULL,
    ProductDescription VARCHAR(255),
    SellingPrice DECIMAL(10, 2) NOT NULL,
    CostPrice DECIMAL(10, 2) NOT NULL,
    ReorderLevel INT NOT NULL,
    CategoryID INT NOT NULL,
    SupplierID INT NOT NULL,

    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
);

-- WAREHOUSE
CREATE TABLE Warehouse (
    WarehouseID INT PRIMARY KEY,
    WarehouseName VARCHAR(100) NOT NULL,
    WarehouseAddress VARCHAR(255),
    WarehouseCity VARCHAR(100),
    WarehousePhone VARCHAR(20)
);

-- INVENTORY STOCK
CREATE TABLE InventoryStock (
    ProductID INT,
    WarehouseID INT,
    QuantityAvailable INT NOT NULL,
    LastStockUpdateDate DATE,

    PRIMARY KEY (ProductID, WarehouseID),

    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID)
);

-- CUSTOMER
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    CustomerEmail VARCHAR(100) UNIQUE,
    CustomerPhone VARCHAR(20),
    CustomerAddress VARCHAR(255)
);

-- CUSTOMER ORDER
CREATE TABLE CustomerOrder (
    OrderID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate DATE NOT NULL,
    OrderStatus VARCHAR(50) NOT NULL,
    PaymentStatus VARCHAR(50) NOT NULL,
    ShippingAddress VARCHAR(255),

    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- CUSTOMER ORDER ITEM
CREATE TABLE CustomerOrderItem (
    OrderID INT,
    ProductID INT,
    QuantityOrdered INT NOT NULL,
    UnitSalePrice DECIMAL(10, 2) NOT NULL,

    PRIMARY KEY (OrderID, ProductID),

    FOREIGN KEY (OrderID) REFERENCES CustomerOrder(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- STOCK MOVEMENT
CREATE TABLE StockMovement (
    MovementID INT PRIMARY KEY,
    ProductID INT NOT NULL,
    WarehouseID INT NOT NULL,
    OrderID INT NULL,
    MovementType VARCHAR(50) NOT NULL,
    MovementQuantity INT NOT NULL,
    MovementDate DATE NOT NULL,
    MovementNotes VARCHAR(255),

    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID),
    FOREIGN KEY (OrderID) REFERENCES CustomerOrder(OrderID)
);