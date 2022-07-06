<h3 align="center"><img src="media/logo.png" alt="logo" height="250px"></h3>

<p align="center">
    <b>FConnch</b><br>
    A Fast Connection Checker
    <br>Easily check a large list of domains in seconds
    <br>
</p>

### :blue_book: Starting stage
```bash
$ git clone https://github.com/signorrayan/FConnch.git && cd FConnch
$ python3 -m venv venv && source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 -m fconnch -h
```

### Example
```bash
$ python3 -m fconnch  -a -v -f domain_list.txt
$ python3 -m fconnch  -a -n -u site1.com site2.org site3.net
# Slow check:
$ python3 -m fconnch -n -u site1.com site2.org site3.net
```


### :bulb: ToDo
- [ ] Add CDN signatures to detect blocked requests instead of showing status code 403.
- [x] Asynchronous check
