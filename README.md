# PSCloud (Galaxy of PSC)

## Install virtual enviroment
```
virtualenv galaxy_env
. ./galaxy_env/bin/activate
```
*For Python IDE (Rodeo): http://rodeo.yhat.com/docs/ *
```
pip install jupyter_client ipykernel numpy pandas matplotlib
```
*For interacting with Galaxy API: http://bioblend.readthedocs.io/en/latest/index.html *
```
pip install bioblend 
```
*For Galaxy command tool: https://github.com/galaxy-iuc/parsec/ *
```
pip install galaxy-parsec
sudo apt-get install jq
```
*For building and publishing Galaxy tools using Planemo: http://planemo.readthedocs.io/en/latest/readme.html *
```
pip install planemo
```
*For managing the Galaxy plugin - tools, index data, and workflow: https://ephemeris.readthedocs.io/en/latest/readme.html *
```
pip install ephemeris
```
*Output installed packages in requirements format*
```
pip freeze > requirements.txt
```

## Install Galaxy
```
LR=17.09
git clone -b release_$LR https://github.com/galaxyproject/galaxy 
./galaxy/run.sh

# ......
# serving on http://127.0.0.1:8080
```

## Setup Galaxy configuration file 
- https://www.galaxyproject.org/admin/
- https://www.galaxyproject.org/admin/disk-quotas/
- https://galaxyproject.org/data-libraries/
- https://docs.galaxyproject.org/en/master/admin/special_topics/nginx.html (DO NOT set *cookie_path = /galaxy* !!!)

```
cat galaxy/config/galaxy.ini.sample \
|sed 's/#admin_users = None/admin_users = xfu@sibs.ac.cn/' \
|sed 's/#enable_quotas = False/enable_quotas = True/' \
|sed 's/#allow_path_paste = False/allow_path_paste = True/' \
|sed -r 's/^\[app:main\]$/\[app:main\]\nfilter-with = proxy-prefix\nnginx_x_accel_redirect_base = \/_x_accel_redirect/' \
> galaxy/config/galaxy.ini
./galaxy/run.sh
```

## Generate new API keys
- Go to http://127.0.0.1:8080
- Register/Login
- Admin => User Management => API keys => Generate a new key now

```
API_KEY=[your api key]
```

## Tool Panel Administration
https://www.galaxyproject.org/admin/tool-panel/
- **tool_conf.xml**: XML configuration file of Local Tools 
- **shed_tool_conf.xml**: shed-related tool panel configuration files are automatically changed when you install or uninstall a Tool Shed repository
- **migrated_tools_conf.xml**: the file is reserved to contain the XML tag sets for repositories that contain tools that were once included in the Galaxy distribution but have been moved to the Tool Shed.
```
cp config/tool_conf.xml galaxy/config/
rm galaxy/integrated_tool_panel.xml
./galaxy/run.sh 
```

## Backup Galaxy
```
cp -r galaxy galaxy.bk
```

## Shed tools
- **Install**
```
shed-tools install -t config/installed.yaml -a $API_KEY
```
- **Export installed tools**
```
get-tool-list -o config/installed.bk.yaml
```

## Graphite configuration
- Install graphite
```
graphite/installation.sh
```
- Install graphitesend
```
source galaxy/.venv/bin/activate
pip install graphitesend
```
- Edit **galaxy.ini**
```
graphite_host=localhost
graphite_port=2003
graphite_prefix=galaxy
```

## Purging Unwanted Histories, Libraries and Datasets 
```
source galaxy/.venv/bin/activate
sh galaxy/scripts/cleanup_datasets/delete_userless_histories.sh
sh galaxy/scripts/cleanup_datasets/purge_histories.sh
sh galaxy/scripts/cleanup_datasets/purge_libraries.sh
sh galaxy/scripts/cleanup_datasets/purge_folders.sh
sh galaxy/scripts/cleanup_datasets/purge_datasets.sh
```

## Genome index
Edit the following files and restart Galaxy
- *galaxy/tool-data/toolshed.g2.bx.psu.edu/repos/iuc/hisat2/40e1083a4430/hisat2_indexes.loc*

## PostgreSQL database
- Install postgresql and pgadmin4
https://www.postgresql.org/download/linux/ubuntu/
https://wiki.postgresql.org/wiki/Apt
```
echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' | sudo tee /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update 
sudo apt-get install -y postgresql-9.6
wget https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v2.1/pip/pgadmin4-2.1-py2.py3-none-any.whl
sudo pip install ./pgadmin4-1.3-py2.py3-none-any.whl
rm pgadmin4-2.1-py2.py3-none-any.whl
```

- Create a new database user and new database which the new user is the owner of. 
https://www.postgresql.org/docs/9.6/static/role-attributes.html
```
sudo -u postgres psql
> CREATE ROLE xfu LOGIN CREATEDB CREATEROLE PASSWORD 'galaxypwd';
> DROP ROLE xfu; # if necessary
> \du # meta-command is also useful for listing the existing roles.
> createdb galaxydb
```

- Edit **galaxy.ini**
https://docs.galaxyproject.org/en/latest/admin/production.html
```
database_connection = postgresql:///galaxydb?host=/var/run/postgresql
database_engine_option_server_side_cursors = True
```

## View database
- Start pgAdmin4
```
pgadmin4
```
- Add New Server
- Browser
Servers => localhost => Databases => galaxydb => Schemas => public => Tables => right_click => View/Edit data

## Connecting to a Cluster
https://docs.galaxyproject.org/en/master/admin/cluster.html
Configuration of where to run jobs is performed in the **job_conf.xml**. 

## To fix some bugs
- **HTseq-count installation (pysam)**
```
./galaxy/database/dependencies/_conda/bin/conda create -y --override-channels --channel iuc --channel bioconda --channel conda-forge --channel defaults --channel r --name mulled-v1-9a164b56634e119cdc1c287da2a8663c2bb84f95bde65b82c675c42a4851a9cc htseq=0.6.1.post1 samtools=1.3.1 pysam=0.10
```
- **edgeR**
```
cp ./shed_tools/toolshed.g2.bx.psu.edu/repos/iuc/edger/2a16413ec60d/edger/edger.R ./shed_tools/toolshed.g2.bx.psu.edu/repos/iuc/edger/2a16413ec60d/edger/edger.R.bk
cp edger.R ./shed_tools/toolshed.g2.bx.psu.edu/repos/iuc/edger/2a16413ec60d/edger/edger.R
```
