CREATE TABLE employees (
	first_name varchar(100) not NULL,
	last_name varchar(100) not NULL,
	title varchar(100) not NULL,
	birth_date date,
	notes text,
	employee_id smallserial PRIMARY KEY
);
CREATE TABLE customers (
	customer_id varchar(50) PRIMARY KEY,
	company_name varchar(100) not NULL,
	contact_name varchar(100) not NULL	
);
CREATE TABLE orders (
	order_id serial PRIMARY KEY,
	customer_id varchar(50) REFERENCES customers(customer_id) not NULL,
	employee_id int REFERENCES employees(employee_id) not NULL,
	order_date date,
	ship_city varchar(100) not NULL	
);