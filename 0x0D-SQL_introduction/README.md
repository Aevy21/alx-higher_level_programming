
# 0x0D SQL - Introduction
``` markdown
## Installation Guide
### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

## Connecting to MySQL Server
```bash
$ sudo mysql
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

## Container-on-Demand
### Using a Container with Ubuntu 20.04
- Connect via SSH or Web terminal
- Start MySQL in the container:
```bash
$ service mysql start
 * Starting MySQL database server mysqld 
```

### Running MySQL Queries in the Container
```bash
$ cat 0-list_databases.sql | mysql -uroot -p
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
```

## General Information
### What’s a database?
A **database** is a structured collection of data organized for efficient retrieval and management. In the context of MySQL, a database can be created using the following SQL command:
```sql
CREATE DATABASE mydatabase;
```
Here, `mydatabase` is the name of the new database.

### What’s a relational database?
A **relational database** organizes data into tables with rows and columns. Tables can be related, allowing for efficient data retrieval. For example, consider a scenario where you have an "employees" table and a "departments" table linked by a common attribute such as department ID.

### What does SQL stand for?
**SQL** stands for **Structured Query Language**. It is a domain-specific language for managing and manipulating relational databases. A simple SQL query to retrieve all data from an "employees" table could look like this:
```sql
SELECT * FROM employees;
```

### What’s MySQL?
**MySQL** is an open-source relational database management system. In the context of this guide, it is used to store and manage data efficiently. For instance, you can use MySQL to create tables within a database and insert data into those tables.

### How to create a database in MySQL?
To create a database in MySQL, you can use the `CREATE DATABASE` statement, as shown earlier. Additionally, you can specify character sets and collations for the database.

### What does DDL and DML stand for?
**DDL** stands for **Data Definition Language**, which includes commands like `CREATE` and `ALTER` for defining and modifying database structures. On the other hand, **DML** stands for **Data Manipulation Language**, covering operations such as `INSERT`, `UPDATE`, and `DELETE` for managing data within the database.

### How to CREATE or ALTER a table?
The `CREATE TABLE` statement is used to create a new table in MySQL. For example:
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10, 2)
);
```
This creates an "employees" table with columns for ID, name, and salary.

### How to SELECT data from a table?
The `SELECT` statement retrieves data from one or more tables. An example to retrieve all employee names and salaries:
```sql
SELECT name, salary FROM employees;
```

### How to INSERT, UPDATE, or DELETE data?
- **INSERT:** Adds new records to a table.
  ```sql
  INSERT INTO employees (name, salary) VALUES ('John Doe', 50000);
  ```
- **UPDATE:** Modifies existing records in a table.
  ```sql
  UPDATE employees SET salary = 55000 WHERE name = 'John Doe';
  ```
- **DELETE:** Removes records from a table.
  ```sql
  DELETE FROM employees WHERE name = 'John Doe';
  ```

### What are subqueries?
**Subqueries** are queries nested within other queries. They can be used to retrieve data that will be used in the main query. An example:
```sql
SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
```

### How to use MySQL functions?
MySQL provides various built-in functions to perform operations on data. An example using the `COUNT` function to count the number of employees:
```sql
SELECT COUNT(*) FROM employees;
```

## Repository Overview
This repository provides comprehensive materials and guides for understanding and working with MySQL. Explore installation steps, connection methods, and fundamental SQL concepts. Gain hands-on experience using a container with Ubuntu 20.04 and delve into essential database and SQL terminology and operations. Whether you are a beginner or looking to refresh your skills, this repository aims to be a valuable resource for your SQL journey.
```
