#!/bin/bash
# NOTE: This is just a script file that Ben uses to quickly get his
# local DB running. It assumes that the following configuration is
# present in DatabaseConnector.py
#   app.config['MYSQL_DATABASE_USER'] = 'root'
#   app.config['MYSQL_DATABASE_PASSWORD'] = ''

mysql.server start
mysql -u root < tables.sql
mysql -u root leagues < sp_User_CreateUser.sql
mysql -u root leagues
