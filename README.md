# tio-tg-perm
## Requirements
* python3
* [pyTenable](https://github.com/tenable/pyTenable)
## Installation
### Python virtual environment
```
$ git clone https://github.com/andrewspearson/tio-tg-perm.git /usr/local/bin/tio-tg-perm
$ python3 -m venv /usr/local/bin/tio-tg-perm/venv
$ . /usr/local/bin/tio-tg-perm/venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
```
## Usage
### Python virtual environment
```
$ cd /usr/local/bin
$ ./venv/bin/python tio-tg-perm.py

Updating System Target Group xxxx Default permission to 'Can Use'
Updating User Target Group xxxx Default permission to 'Can Use'
Updating User Target Group xxxx Default permission to 'Can Use'
Updating User Target Group xxxx Default permission to 'Can Use'
Updating System Target Group xxxx Default permission to 'Can Use'
Updating System Target Group xxxx Default permission to 'Can Use'
Updating System Target Group xxxx Default permission to 'Can Use'
Updating System Target Group xxxx Default permission to 'Can Use'
Updating System Target Group xxxx Default permission to 'Can Use'
Updating System Target Group xxxx Default permission to 'Can Use'

```
## Results

All Tenable.IO Target Groups should now have the Default Permission set to 'Can Use'.
