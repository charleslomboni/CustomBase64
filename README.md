# CustomBase64

## Goals
Custom base64 with option to pass specific key

## How to use this script?
```
λ python CustomBase64.py -h
usage: key [-h] [-k KEY] strToDecode

positional arguments:
  strToDecode        String to decode from base64

optional arguments:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  Custom base64 key

```

**Example**
```
λ python CustomBase64.py "base64 string" -k "custom key"

```
