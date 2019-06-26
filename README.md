# BashSmash
A tool for obfuscating bash shell code

## Installation
To install BashSmash, make sure `python3.7` and `python3-pip` are installed on your computer, then run:
```
pip3 install bashsmash
```

BashSmash is now installed!

## Usage
BashSmash can be used in two ways. First, by passing your script as an argument:
```bash
# The result will be sent to stdout
bashsmash "echo Hello, World\!" 
```

Or, by piping through stdin:
```bash
# The result will be sent to stdout
echo "echo Hello, World\!" | bashsmash -
```