# Script for search tweets in Twitter

Python script developed under the Social Media Analytics course project where we have to colect data from twitter for further text and sentiment analysis.

### Required libraries

```shell
pip install python-twitter
pib install pandas 
```

### How to use

Put your own twitter consumer and access token keys in the following code
```python
CONSUMER_KEY = 'xxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxx'
```
Replace the searching words
```python
def main():
    search('WorldCup+2018')
```
Execute the script

```bash
python3 sma-tw.py
```