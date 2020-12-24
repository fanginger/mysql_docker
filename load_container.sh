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
mysql --user=root  --execute="CREATE DATABASE testdb;"
mysql --user=root  --execute="CREATE USER 'ddt'@'%' IDENTIFIED BY '$password';"
mysql --user=root  --execute="GRANT ALL ON testdb.* TO 'ddt'@'%';"
mysql --user=root   <"init.sql"

# service mysql start &&tail -f /var/log/mysql/error.log
python apiServer.py $password 

# bash