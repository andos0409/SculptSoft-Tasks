class Category:

    def __init__(self, CategoryID, CategoryName, CategoryDescription=None):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName
        self.CategoryDescription = CategoryDescription

    def new_category(self, connection):
        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO Category
            (CategoryID, CategoryName, CategoryDescription)
        VALUES
            (%s, %s, %s)
        """,
        (self.CategoryID, self.CategoryName, self.CategoryDescription)
        )

        connection.commit()



class Supplier:

    def __init__(self, SupplierID, SupplierName, SupplierEmail,
                 SupplierPhone, SupplierAddress):
        self.SupplierID = SupplierID
        self.SupplierName = SupplierName
        self.SupplierEmail = SupplierEmail
        self.SupplierPhone = SupplierPhone
        self.SupplierAddress = SupplierAddress

    def new_supplier(self, connection):
        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO Supplier
            (SupplierID, SupplierName, SupplierEmail, SupplierPhone, SupplierAddress)
        VALUES
            (%s, %s, %s, %s, %s)
        """,
        (self.SupplierID, self.SupplierName, self.SupplierEmail,
         self.SupplierPhone, self.SupplierAddress)
        )

        connection.commit()



class Product:

    def __init__(self, ProductID, ProductName, SKU, ProductDescription,
                 SellingPrice, CostPrice, ReorderLevel, CategoryID, SupplierID):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.SKU = SKU
        self.ProductDescription = ProductDescription
        self.SellingPrice = SellingPrice
        self.CostPrice = CostPrice
        self.ReorderLevel = ReorderLevel
        self.CategoryID = CategoryID
        self.SupplierID = SupplierID

    def new_product(self, connection):
        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO Product
            (ProductID, ProductName, SKU, ProductDescription,
             SellingPrice, CostPrice, ReorderLevel, CategoryID, SupplierID)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (self.ProductID, self.ProductName, self.SKU, self.ProductDescription,
         self.SellingPrice, self.CostPrice, self.ReorderLevel,
         self.CategoryID, self.SupplierID)
        )

        connection.commit()

    def update_price(self, connection, new_selling_price):
        self.SellingPrice = new_selling_price

        cursor = connection.cursor()

        cursor.execute(
        """
        UPDATE Product
        SET SellingPrice = %s
        WHERE ProductID = %s
        """,
        (self.SellingPrice, self.ProductID)
        )

        connection.commit()



class Warehouse:

    def __init__(self, WarehouseID, WarehouseName, WarehouseAddress,
                 WarehouseCity, WarehousePhone):
        self.WarehouseID = WarehouseID
        self.WarehouseName = WarehouseName
        self.WarehouseAddress = WarehouseAddress
        self.WarehouseCity = WarehouseCity
        self.WarehousePhone = WarehousePhone

    def new_warehouse(self, connection):
        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO Warehouse
            (WarehouseID, WarehouseName, WarehouseAddress,
             WarehouseCity, WarehousePhone)
        VALUES
            (%s, %s, %s, %s, %s)
        """,
        (self.WarehouseID, self.WarehouseName, self.WarehouseAddress,
         self.WarehouseCity, self.WarehousePhone)
        )

        connection.commit()



class InventoryStock:

    def __init__(self, ProductID, WarehouseID, QuantityAvailable,
                 LastStockUpdateDate, product=None, warehouse=None):
        self.ProductID = ProductID
        self.WarehouseID = WarehouseID
        self.QuantityAvailable = QuantityAvailable
        self.LastStockUpdateDate = LastStockUpdateDate
        self.product = product
        self.warehouse = warehouse

    def new_stock_record(self, connection):
        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO InventoryStock
            (ProductID, WarehouseID, QuantityAvailable, LastStockUpdateDate)
        VALUES
            (%s, %s, %s, %s)
        """,
        (self.ProductID, self.WarehouseID,
         self.QuantityAvailable, self.LastStockUpdateDate)
        )

        connection.commit()

    def add_stock(self, connection, quantity, update_date):
        self.QuantityAvailable += quantity
        self.LastStockUpdateDate = update_date

        cursor = connection.cursor()

        cursor.execute(
        """
        UPDATE InventoryStock
        SET QuantityAvailable = %s,
            LastStockUpdateDate = %s
        WHERE ProductID = %s AND WarehouseID = %s
        """,
        (self.QuantityAvailable, self.LastStockUpdateDate,
         self.ProductID, self.WarehouseID)
        )

        connection.commit()

    def remove_stock(self, connection, quantity, update_date):
        if quantity > self.QuantityAvailable:
            raise ValueError("Not enough stock available")

        self.QuantityAvailable -= quantity
        self.LastStockUpdateDate = update_date

        cursor = connection.cursor()

        cursor.execute(
        """
        UPDATE InventoryStock
        SET QuantityAvailable = %s,
            LastStockUpdateDate = %s
        WHERE ProductID = %s AND WarehouseID = %s
        """,
        (self.QuantityAvailable, self.LastStockUpdateDate,
         self.ProductID, self.WarehouseID)
        )

        connection.commit()



class Customer:

    def __init__(self, CustomerID, CustomerName, CustomerEmail,
                 CustomerPhone, CustomerAddress):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.CustomerEmail = CustomerEmail
        self.CustomerPhone = CustomerPhone
        self.CustomerAddress = CustomerAddress

    def new_customer(self, connection):
        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO Customer
            (CustomerID, CustomerName, CustomerEmail,
             CustomerPhone, CustomerAddress)
        VALUES
            (%s, %s, %s, %s, %s)
        """,
        (self.CustomerID, self.CustomerName, self.CustomerEmail,
         self.CustomerPhone, self.CustomerAddress)
        )

        connection.commit()



class CustomerOrder:

    def __init__(self, OrderID, CustomerID, OrderDate, OrderStatus,
                 PaymentStatus, ShippingAddress, customer=None):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.OrderDate = OrderDate
        self.OrderStatus = OrderStatus
        self.PaymentStatus = PaymentStatus
        self.ShippingAddress = ShippingAddress
        self.customer = customer

    def new_order(self, connection):
        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO CustomerOrder
            (OrderID, CustomerID, OrderDate, OrderStatus,
             PaymentStatus, ShippingAddress)
        VALUES
            (%s, %s, %s, %s, %s, %s)
        """,
        (self.OrderID, self.CustomerID, self.OrderDate,
         self.OrderStatus, self.PaymentStatus, self.ShippingAddress)
        )

        connection.commit()

    def update_order_status(self, connection, new_status):
        self.OrderStatus = new_status

        cursor = connection.cursor()

        cursor.execute(
        """
        UPDATE CustomerOrder
        SET OrderStatus = %s
        WHERE OrderID = %s
        """,
        (self.OrderStatus, self.OrderID)
        )

        connection.commit()

    def update_payment_status(self, connection, new_payment_status):
        self.PaymentStatus = new_payment_status

        cursor = connection.cursor()

        cursor.execute(
        """
        UPDATE CustomerOrder
        SET PaymentStatus = %s
        WHERE OrderID = %s
        """,
        (self.PaymentStatus, self.OrderID)
        )

        connection.commit()



class CustomerOrderItem:

    def __init__(self, OrderID, ProductID, QuantityOrdered,
                 UnitSalePrice, order=None, product=None):
        self.OrderID = OrderID
        self.ProductID = ProductID
        self.QuantityOrdered = QuantityOrdered
        self.UnitSalePrice = UnitSalePrice
        self.order = order
        self.product = product

    def new_order_item(self, connection):
        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO CustomerOrderItem
            (OrderID, ProductID, QuantityOrdered, UnitSalePrice)
        VALUES
            (%s, %s, %s, %s)
        """,
        (self.OrderID, self.ProductID,
         self.QuantityOrdered, self.UnitSalePrice)
        )

        connection.commit()



class StockMovement:

    def __init__(self, MovementID, ProductID, WarehouseID, OrderID,
                 MovementType, MovementQuantity, MovementDate,
                 MovementNotes=None, product=None, warehouse=None, order=None):
        self.MovementID = MovementID
        self.ProductID = ProductID
        self.WarehouseID = WarehouseID
        self.OrderID = OrderID
        self.MovementType = MovementType
        self.MovementQuantity = MovementQuantity
        self.MovementDate = MovementDate
        self.MovementNotes = MovementNotes
        self.product = product
        self.warehouse = warehouse
        self.order = order

    def new_movement(self, connection):
        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO StockMovement
            (MovementID, ProductID, WarehouseID, OrderID,
             MovementType, MovementQuantity, MovementDate, MovementNotes)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (self.MovementID, self.ProductID, self.WarehouseID,
         self.OrderID, self.MovementType, self.MovementQuantity,
         self.MovementDate, self.MovementNotes)
        )

        connection.commit()