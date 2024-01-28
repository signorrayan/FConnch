<h3 align="center"><img src="media/logo.png" alt="logo" height="200px"></h3>

<h3 align="center">FConnch</h3>
<p align="center">
    A Fast Bulk Subdomain Availability Checker
    <br>In the recon phase, you can quickly check a huge list of domains availability in seconds
    <br>
</p>

## :blue_book: Starting stage

<h3 align="center"><img src="media/usage-exp.gif" alt="logo" height="550"></h3>

```bash
$ python3 -m pip install --upgrade pipx
$ pipx install git+https://github.com/signorrayan/FConnch.git
$ fconnch -h
```

__-- or --__

```bash
$ git clone https://github.com/signorrayan/FConnch.git && cd FConnch
$ python3 -m venv venv && source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 fconnch.py -h
```

## :desktop_computer: Usage example

```bash
$ fconnch -h
usage: fconnch [-h] [-u URLs [URLs ...]] [-f FILE] [-a] [-v] [-n] [-t TIMEOUT]
options:
  -h, --help            show this help message and exit
  -u URLs [URLs ...], --urls URLs [URLs ...]
                        Enter one or more website URLs (separated by space).
  -i FILE, --input-file FILE
                        Read URLs from a file.
  -o FILE, --output-file FILE 
                        Save the results to a file
  -a, --asynchronous    Run the connectivity check asynchronously
  -v, --verbose         Shows if any error exists related to the dns resolve
  -n, --no-color        Output without color
  -t TIMEOUT, --timeout TIMEOUT
                        Set timeout - default is 3s

$ fconnch  -a -v -i domain_list.txt -o results.txt

$ fconnch  -a -n -u site1.com site2.org site3.net

# Slow check:
$ fconnch -u site1.com site2.org site3.net
```

## :bulb: ToDo

- [ ] Add CDN signatures to detect blocked requests instead of showing status code 403.
- [x] Asynchronous check
- [ ] ~~Implement dockerized script~~

## :trident: Contributing

If you have any suggestions/ideas/improvements please consider contributing to this project .\
To contribute you can create an issue or (better) you can **fork & create a pull request**.

Contact email: mo.sarayloo [At] proton [dot] me
