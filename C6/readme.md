# Databases and SQL for Data Science with Python

[cheatsheet](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstREIwMjAxRU4tU2tpbGxzTmV0d29yay9sYWJzL0NoZWF0U2hlZXQvU1FMLUNoZWF0LVNoZWV0LUJhc2Npcy5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE3MDA2NzE0MDN9.izyOhNpABkiOSna9NCuCDv6KjobNSOEj-Gn-rAU6jSc)

# install postgres

        sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
        
        wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
        
        sudo apt-get update
        
        sudo apt-get -y install postgresql

access postgres client `sudo -i -u postgres`

exit postgres client `\q`

install `pgadmin` 

        #
        # Setup the repository
        #

        # Install the public key for the repository (if not done previously):
        curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

        # Create the repository configuration file:
        sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

        #
        # Install pgAdmin
        #

        # Install for both desktop and web modes:
        sudo apt install pgadmin4

        # Install for desktop mode only:
        sudo apt install pgadmin4-desktop

        # Install for web mode only: 
        sudo apt install pgadmin4-web 

        # Configure the webserver, if you installed pgadmin4-web:
        sudo /usr/pgadmin4/bin/setup-web.sh

# install mysql

        sudo apt update
        sudo apt install mysql-server

check mysql `sudo systemctl status mysql.service`
start mysql `sudo systemctl start mysql.service`

install [mysql-workbench](https://dev.mysql.com/downloads/workbench/) `sudo snap install mysql-workbench-community`

install `phpmyadmin` 

    sudo apt update
    sudo apt-get install apache2
    sudo apt install php
    sudo apt install phpmyadmin
    sudo phpenmod mbdstring
    sudo systemctl restart apache2

# install mongodb

[Download MongoDB](https://www.mongodb.com/try/download/community)

- install mongodb `sudo dpkg -i mongodb-org-server_7.0.6_amd64.deb`

- check mongod `sudo systemctl status mongod`
- start mongo deamon `sudo systemctl start mongod`
# references

[exercises](https://www.w3schools.com/sql/sql_exercises.asp)

[practices](https://www.hackerrank.com/domains/sql)

[How To Install PostgreSQL on Ubuntu 22.04](https://www.postgresql.org/download/linux/ubuntu/)

[ How To Install MySQL on Ubuntu 22.04 LTS (Linux) ](https://www.youtube.com/watch?v=zRfI79BHf3k)

[ How to install MongoDB 6 on Ubuntu 22.04 LTS Linux ](https://www.youtube.com/watch?v=HSIh8UswVVY)

[ How To Install PostgreSQL on Ubuntu 22.04 LTS (Linux) ](https://www.youtube.com/watch?v=tducLYZzElo)