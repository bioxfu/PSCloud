# Installing From Pip
# http://graphite.readthedocs.io/en/latest/install-pip.html
sudo apt-get install -y python-dev libcairo2-dev libffi-dev build-essential python-setuptools 
export PYTHONPATH="/opt/graphite/lib/:/opt/graphite/webapp/"
sudo -H pip install --no-binary=:all: https://github.com/graphite-project/whisper/tarball/master
sudo -H pip install --no-binary=:all: https://github.com/graphite-project/carbon/tarball/master
sudo -H pip install --no-binary=:all: https://github.com/graphite-project/graphite-web/tarball/master

# Webapp Database Setup
# http://graphite.readthedocs.io/en/latest/config-database-setup.html
# To set up a new database and create the initial schema, run:
sudo PYTHONPATH=/opt/graphite/webapp django-admin.py migrate --settings=graphite.settings --run-syncdb

# Configuring The Webapp
# http://graphite.readthedocs.io/en/latest/config-webapp.html
# nginx + gunicorn
sudo apt install -y gunicorn
# use dedicated log files for nginx when serving Graphite:
sudo touch /var/log/nginx/graphite.access.log
sudo touch /var/log/nginx/graphite.error.log
sudo chmod 640 /var/log/nginx/graphite.*
sudo chown www-data:www-data /var/log/nginx/graphite.*

#sudo cp graphite /etc/nginx/sites-available/graphite
#sudo ln -s /etc/nginx/sites-available/graphite /etc/nginx/sites-enabled
#sudo rm -f /etc/nginx/sites-enabled/default
#sudo service nginx reload

# Administering The Webapp
# http://graphite.readthedocs.io/en/latest/admin-webapp.html
# start Gunicorn
cd /opt/graphite/conf
sudo cp dashboard.conf.example dashboard.conf
sudo cp graphTemplates.conf.example graphTemplates.conf
sudo PYTHONPATH=/opt/graphite/webapp gunicorn wsgi --workers=4 --bind=127.0.0.1:9090 --log-file=/var/log/gunicorn.log --preload --pythonpath=/opt/graphite/webapp/graphite &

# Configuring Carbon
# http://graphite.readthedocs.io/en/latest/config-carbon.html
cd /opt/graphite/conf
sudo cp carbon.conf.example carbon.conf
sudo cp storage-schemas.conf.example storage-schemas.conf

# Administering Carbon
# http://graphite.readthedocs.io/en/latest/admin-carbon.html
# start Carbon
sudo /opt/graphite/bin/carbon-cache.py start

echo "local.random.diceroll 4 `date +%s`" | nc -q0 localhost 2003

