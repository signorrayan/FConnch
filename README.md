<h3 align="center"><img src="media/logo.png" alt="logo" height="250px"></h3>

<p align="center">
    <b>FConnch</b><br>
    A Fast Connection Checker
    <br>Easily check a large list of domains in seconds
    <br>
</p>

## :blue_book: Starting stage
```bash
$ git clone https://github.com/signorrayan/FConnch.git && cd FConnch
$ python3 -m venv venv && source venv/bin/activate
$ python3 -m pip install -r requirements.txt
```

## :desktop_computer: Example
```bash
$ python3 -m fconnch -h
options:
  -h, --help            show this help message
  -u URLs [URLs ...], --urls URLs [URLs ...]
                        Enter one or more website URLs (seperated by space).
  -f FILE, --input-file FILE
                        Read URLs from a file.
  -a, --asynchronous    Run the connectivity check asynchronously
  -v, --verbose         Shows if any error exists related to the dns resolve
  -n, --no-color        Output without color

$ python3 -m fconnch  -a -v -f domain_list.txt

$ python3 -m fconnch  -a -n -u site1.com site2.org site3.net

# Slow check:
$ python3 -m fconnch -u site1.com site2.org site3.net
```


## :bulb: ToDo
- [ ] Add CDN signatures to detect blocked requests instead of showing status code 403.
- [x] Asynchronous check


## :trident: Contributing
If you have any suggestions/ideas/improvements please consider contributing to this project .\
To contribute you can create an issue or (better) you can **fork & create a pull request**.

Contact email: mo.sarayloo [At] proton [dot] me