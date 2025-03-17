import sqlite3

# Create a connection to the database
conn = sqlite3.connect('electronics_store.db')
cursor = conn.cursor()

# Create the categories table
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories
(id INTEGER PRIMARY KEY, name TEXT)
''')

# Create the suppliers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS suppliers
(id INTEGER PRIMARY KEY, name TEXT, contact_email TEXT)
''')

# Create the products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products
(id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL, stock_quantity INTEGER, category_id INTEGER,
FOREIGN KEY (category_id) REFERENCES categories (id))
''')

# Create the product_suppliers table (many-to-many relationship)
cursor.execute('''
CREATE TABLE IF NOT EXISTS product_suppliers
(product_id INTEGER, supplier_id INTEGER,
FOREIGN KEY (product_id) REFERENCES products (id),
FOREIGN KEY (supplier_id) REFERENCES suppliers (id))
''')

# Create the customers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers
(id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT)
''')

# Create the orders table
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders
(id INTEGER PRIMARY KEY, customer_id INTEGER, order_date DATE, total REAL,
FOREIGN KEY (customer_id) REFERENCES customers (id))
''')

# Create the order_items table
cursor.execute('''
CREATE TABLE IF NOT EXISTS order_items
(id INTEGER PRIMARY KEY, order_id INTEGER, product_id INTEGER, quantity INTEGER,
FOREIGN KEY (order_id) REFERENCES orders (id),
FOREIGN KEY (product_id) REFERENCES products (id))
''')

# Create the product_reviews table
cursor.execute('''
CREATE TABLE IF NOT EXISTS product_reviews
(id INTEGER PRIMARY KEY, product_id INTEGER, customer_id INTEGER, review TEXT, rating INTEGER,
FOREIGN KEY (product_id) REFERENCES products (id),
FOREIGN KEY (customer_id) REFERENCES customers (id))
''')

# Create the employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees
(id INTEGER PRIMARY KEY, name TEXT, position TEXT, email TEXT)
''')

# Create the employee_roles table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee_roles
(id INTEGER PRIMARY KEY, role_name TEXT)
''')

# Create the employee_role_assignments table (many-to-many relationship)
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee_role_assignments
(employee_id INTEGER, role_id INTEGER,
FOREIGN KEY (employee_id) REFERENCES employees (id),
FOREIGN KEY (role_id) REFERENCES employee_roles (id))
''')

# Insert some example data

# Categories
cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('Electronics')")
cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('Accessories')")
cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('Gaming')")
cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('Home Appliances')")

# Suppliers
cursor.execute("INSERT OR IGNORE INTO suppliers (name, contact_email) VALUES ('Supplier A', 'supplierA@example.com')")
cursor.execute("INSERT OR IGNORE INTO suppliers (name, contact_email) VALUES ('Supplier B', 'supplierB@example.com')")
cursor.execute("INSERT OR IGNORE INTO suppliers (name, contact_email) VALUES ('Supplier C', 'supplierC@example.com')")
cursor.execute("INSERT OR IGNORE INTO suppliers (name, contact_email) VALUES ('Supplier D', 'supplierD@example.com')")

# Products
cursor.execute("INSERT OR IGNORE INTO products (name, description, price, stock_quantity, category_id) VALUES ('Smartphone X', 'High-end smartphone with advanced camera', 999.99, 100, 1)")
cursor.execute("INSERT OR IGNORE INTO products (name, description, price, stock_quantity, category_id) VALUES ('Laptop Y', 'Powerful laptop for gaming and video editing', 1999.99, 50, 1)")
cursor.execute("INSERT OR IGNORE INTO products (name, description, price, stock_quantity, category_id) VALUES ('Smartwatch Z', 'Advanced smartwatch with fitness tracking', 299.99, 50, 2)")
cursor.execute("INSERT OR IGNORE INTO products (name, description, price, stock_quantity, category_id) VALUES ('Gaming Mouse', 'High-precision gaming mouse', 99.99, 200, 3)")
cursor.execute("INSERT OR IGNORE INTO products (name, description, price, stock_quantity, category_id) VALUES ('Wireless Headphones', 'Premium wireless headphones with long battery life', 149.99, 150, 2)")
cursor.execute("INSERT OR IGNORE INTO products (name, description, price, stock_quantity, category_id) VALUES ('Refrigerator', 'Energy-efficient refrigerator with advanced features', 999.99, 20, 4)")
cursor.execute("INSERT OR IGNORE INTO products (name, description, price, stock_quantity, category_id) VALUES ('Washing Machine', 'High-capacity washing machine with multiple cycles', 499.99, 30, 4)")

# Product Suppliers
cursor.execute("INSERT OR IGNORE INTO product_suppliers (product_id, supplier_id) VALUES (1, 1)")
cursor.execute("INSERT OR IGNORE INTO product_suppliers (product_id, supplier_id) VALUES (2, 2)")
cursor.execute("INSERT OR IGNORE INTO product_suppliers (product_id, supplier_id) VALUES (3, 1)")
cursor.execute("INSERT OR IGNORE INTO product_suppliers (product_id, supplier_id) VALUES (4, 3)")
cursor.execute("INSERT OR IGNORE INTO product_suppliers (product_id, supplier_id) VALUES (5, 2)")
cursor.execute("INSERT OR IGNORE INTO product_suppliers (product_id, supplier_id) VALUES (6, 4)")
cursor.execute("INSERT OR IGNORE INTO product_suppliers (product_id, supplier_id) VALUES (7, 3)")

# Customers
cursor.execute("INSERT OR IGNORE INTO customers (name, email, phone) VALUES ('John Doe', 'john@example.com', '123-456-7890')")
cursor.execute("INSERT OR IGNORE INTO customers (name, email, phone) VALUES ('Jane Smith', 'jane.smith@example.com', '987-654-3210')")
cursor.execute("INSERT OR IGNORE INTO customers (name, email, phone) VALUES ('Michael Brown', 'michael.brown@example.com', '555-123-4567')")
cursor.execute("INSERT OR IGNORE INTO customers (name, email, phone) VALUES ('Emily Johnson', 'emily.johnson@example.com', '111-222-3333')")
cursor.execute("INSERT OR IGNORE INTO customers (name, email, phone) VALUES ('David Lee', 'david.lee@example.com', '444-555-6666')")

# Orders
cursor.execute("INSERT OR IGNORE INTO orders (customer_id, order_date, total) VALUES (1, '2025-03-01', 999.99)")
cursor.execute("INSERT OR IGNORE INTO orders (customer_id, order_date, total) VALUES (2, '2025-03-15', 299.99)")
cursor.execute("INSERT OR IGNORE INTO orders (customer_id, order_date, total) VALUES (3, '2025-03-20', 99.99)")
cursor.execute("INSERT OR IGNORE INTO orders (customer_id, order_date, total) VALUES (4, '2025-03-25', 149.99)")
cursor.execute("INSERT OR IGNORE INTO orders (customer_id, order_date, total) VALUES (5, '2025-03-30', 499.99)")
cursor.execute("INSERT OR IGNORE INTO orders (customer_id, order_date, total) VALUES (1, '2025-04-01', 1999.99)")
cursor.execute("INSERT OR IGNORE INTO orders (customer_id, order_date, total) VALUES (2, '2025-04-05', 99.99)")
cursor.execute("INSERT OR IGNORE INTO orders (customer_id, order_date, total) VALUES (3, '2025-04-10', 149.99)")
cursor.execute("INSERT OR IGNORE INTO orders (customer_id, order_date, total) VALUES (4, '2025-04-15', 299.99)")

# Order items
cursor.execute("INSERT OR IGNORE INTO order_items (order_id, product_id, quantity) VALUES (1, 1, 1)")
cursor.execute("INSERT OR IGNORE INTO order_items (order_id, product_id, quantity) VALUES (2, 3, 1)")
cursor.execute("INSERT OR IGNORE INTO order_items (order_id, product_id, quantity) VALUES (3, 4, 1)")
cursor.execute("INSERT OR IGNORE INTO order_items (order_id, product_id, quantity) VALUES (4, 5, 1)")
cursor.execute("INSERT OR IGNORE INTO order_items (order_id, product_id, quantity) VALUES (5, 6, 1)")
cursor.execute("INSERT OR IGNORE INTO order_items (order_id, product_id, quantity) VALUES (6, 2, 1)")
cursor.execute("INSERT OR IGNORE INTO order_items (order_id, product_id, quantity) VALUES (7, 4, 1)")
cursor.execute("INSERT OR IGNORE INTO order_items (order_id, product_id, quantity) VALUES (8, 5, 1)")
cursor.execute("INSERT OR IGNORE INTO order_items (order_id, product_id, quantity) VALUES (9, 3, 1)")

# Product Reviews
cursor.execute("INSERT OR IGNORE INTO product_reviews (product_id, customer_id, review, rating) VALUES (1, 1, 'Excellent product!', 5)")
cursor.execute("INSERT OR IGNORE INTO product_reviews (product_id, customer_id, review, rating) VALUES (3, 2, 'Good but not great.', 3)")
cursor.execute("INSERT OR IGNORE INTO product_reviews (product_id, customer_id, review, rating) VALUES (4, 3, 'Perfect for gaming!', 5)")
cursor.execute("INSERT OR IGNORE INTO product_reviews (product_id, customer_id, review, rating) VALUES (5, 4, 'Comfortable headphones.', 4)")
cursor.execute("INSERT OR IGNORE INTO product_reviews (product_id, customer_id, review, rating) VALUES (6, 5, 'Great refrigerator!', 5)")

# Employees
cursor.execute("INSERT OR IGNORE INTO employees (name, position, email) VALUES ('Jane Smith', 'Sales Manager', 'jane.smith@example.com')")
cursor.execute("INSERT OR IGNORE INTO employees (name, position, email) VALUES ('John Doe', 'Support Specialist', 'john.doe@example.com')")
cursor.execute("INSERT OR IGNORE INTO employees (name, position, email) VALUES ('Emily Johnson', 'Marketing Manager', 'emily.johnson@example.com')")
cursor.execute("INSERT OR IGNORE INTO employees (name, position, email) VALUES ('Michael Brown', 'Sales Representative', 'michael.brown@example.com')")

# Employee Roles
cursor.execute("INSERT OR IGNORE INTO employee_roles (role_name) VALUES ('Sales Manager')")
cursor.execute("INSERT OR IGNORE INTO employee_roles (role_name) VALUES ('Support Specialist')")
cursor.execute("INSERT OR IGNORE INTO employee_roles (role_name) VALUES ('Marketing Manager')")
cursor.execute("INSERT OR IGNORE INTO employee_roles (role_name) VALUES ('Sales Representative')")

# Employee Role Assignments
cursor.execute("INSERT OR IGNORE INTO employee_role_assignments (employee_id, role_id) VALUES (1, 1)")
cursor.execute("INSERT OR IGNORE INTO employee_role_assignments (employee_id, role_id) VALUES (2, 2)")
cursor.execute("INSERT OR IGNORE INTO employee_role_assignments (employee_id, role_id) VALUES (3, 3)")
cursor.execute("INSERT OR IGNORE INTO employee_role_assignments (employee_id, role_id) VALUES (4, 4)")

# Commit changes
conn.commit()

# Close
