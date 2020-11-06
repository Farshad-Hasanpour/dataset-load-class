# Dataset Load Class

This python class helps you to read various dataset file types including, JSON, CSV, etc. Each function is for a specific type of dataset file. 

## Usage

The code below is an example to load a compressed JSON dataset.

```python
FILENAME = 'Movies_and_TV_5core.json.gz'
USEFUL_KEYS = {'overall', 'vote', 'reviewText', 'summary'}
REQUIRED_KEYS = {'vote', 'reviewText'}
obj = Dataset(FILENAME)
dataset = obj.read_json(required_keys=REQUIRED_KEYS, useful_keys=USEFUL_KEYS, is_zip=True)
```

## Function Parameters

### read_json()

 - **required_keys** (type: set or list): Required keys for each record. If one of these keys does not exist, this function ignores the dataset record.
 - **useful_keys** (type: set or list): Keys to return for each dataset record.
 - **is_zip** (type: boolean): Whether the JSON file is inside a compressed file or not.
