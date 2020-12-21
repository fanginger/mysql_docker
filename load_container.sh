service mysql start
service cron start

set -e
set -x # Print shell command before execute it.  This feature help programmers to track their shell script.

# Start the MySQL daemon in the background.
/usr/sbin/mysqld &
mysql_pid=$!

until mysqladmin ping >/dev/null 2>&1; do
  echo -n "."; sleep 0.2
done
mysql --user=root --password='ginger123'  --execute="CREATE DATABASE testdb;"
mysql --user=root --password='ginger123'  --execute="CREATE USER 'ginger'@'%' IDENTIFIED BY 'ginger123';"
mysql --user=root --password='ginger123'  --execute="GRANT ALL ON testdb.* TO 'ginger'@'%';"

python apiServer.py

bash