# Dataset Loading Class

This python class helps you to read various dataset file types including, JSON, CSV, etc. Each function is for a specific type of dataset file. 

## Alternatives

- [pandas](https://pandas.pydata.org/docs/index.html)

## Requirements

This library uses modules below:

- gzip
- json
- csv

## Usage

The code below is an example to load a compressed JSON dataset.

```python
FILENAME = 'Movies_and_TV_5core.json.gz'
USEFUL_KEYS = {'overall', 'vote', 'reviewText', 'summary'}
REQUIRED_KEYS = {'vote', 'reviewText'}
dataset = Dataset(FILENAME).read_json(useful_keys=USEFUL_KEYS, required_keys=REQUIRED_KEYS, is_zip=True)
```

## Functions

### read_json()

For each JSON record, return a dictionary inside a list.

 - **useful_keys** (type: tuple): Keys to return for each dataset record. Pass empty to return all keys.
 - **required_keys** (type: tuple): Required keys for each record. If one of these keys does not exist, this function ignores the dataset record.
 - **is_gzip** (type: boolean): Whether the file is a compressed file or not.
 - **encoding** (type: string): The default is 'utf8'.

### read_csv()

For each CSV row, return a list inside another list and a list of headers.

 - **useful_keys** (type: tuple): Keys to return for each dataset record. Pass empty to return all keys.
 - **required_keys** (type: tuple): Required keys for each record. If one of these keys does not exist, this function ignores the dataset record.
  - **delimiter** (type: string): CSV delimiter
 - **is_gzip** (type: boolean): Whether the file is a compressed file or not.
 - **encoding** (type: string): The default is 'utf8'.
