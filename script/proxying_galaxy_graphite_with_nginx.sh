# https://docs.galaxyproject.org/en/master/admin/special_topics/nginx.html
## http://graphite.readthedocs.io/en/latest/config-webapp.html

# edit nginx config file
sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bk
sudo cp config/nginx.conf /etc/nginx/nginx.conf
sudo nginx -s reload

# reload the galaxy daemon
./galaxy/run.sh --reload
