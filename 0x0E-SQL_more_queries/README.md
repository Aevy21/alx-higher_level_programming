# 0x0E-SQL_more_queries Readme

## Install MySQL 8.0 on Ubuntu 20.04 LTS

1. Update package list:
   ```
   $ sudo apt update
   ```

2. Install MySQL Server:
   ```
   $ sudo apt install mysql-server
   ```

3. Check MySQL version:
   ```
   $ mysql --version
   mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
   ```

## Connect to your MySQL server

1. Open MySQL monitor:
   ```
   $ sudo mysql
   ```

2. Check connection information:
   ```
   Welcome to the MySQL monitor.  Commands end with ; or \g.
   Your MySQL connection id is 11
   Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)
   ...
   mysql>
   ```

3. Quit MySQL monitor:
   ```
   mysql> quit
   Bye
   ```

## Use "container-on-demand" to run MySQL

1. In the container, credentials are root/root.

2. Ask for a container with Ubuntu 20.04.

3. Connect via SSH or use the Web terminal.

4. Start MySQL in the container:
   ```
   $ service mysql start
   ```

## How to import a SQL dump

1. Create a new database:
   ```
   $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
   ```

2. Import SQL dump:
   ```
   $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
   ```

3. Run a sample query:
   ```
   $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
   ```

## How to create a new MySQL user

- [Guide to creating a new MySQL user](#)

## How to manage privileges for a user to a database or table

- [Guide to managing MySQL user privileges](#)

## What’s a PRIMARY KEY

- [Explanation of PRIMARY KEY in MySQL](#)

## What’s a FOREIGN KEY

- [Explanation of FOREIGN KEY in MySQL](#)

## How to use NOT NULL and UNIQUE constraints

- [Guide to using NOT NULL and UNIQUE constraints](#)

## How to retrieve data from multiple tables in one request

- [Guide to retrieving data from multiple tables](#)

## What are subqueries

- [Explanation of subqueries in MySQL](#)

## What are JOIN and UNION

- [Explanation of JOIN and UNION in MySQL](#)

