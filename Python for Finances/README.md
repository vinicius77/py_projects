## Python For Finances - Cheat Sheet

### Anaconda (software package that contains Python and Jupyter)

- Jupyter Notebook (server client application) => extension \*.ipynb (Ipython Notebook)
- Download at [anaconda website](www.anaconda.com)
- Installing Tutorial at [id root website](www.idroot.us/install-anaconda-ubuntu-20-04)

## Activating Environment

```
$ conda activate
```

## Installing packages

```
$ pip install name_of_package
```

## Command Line

- Lists all the packages installed with Anaconda

```
$ conda list
```

- Starts a new instance of Jupyter Notebook

```
$ jupyter notebook
```

- Starts a previously created instance of Jupyter Notebook

```
$ jupyter notebook exercises.ipynb
```

## Shortcut Commands

- Runs the code and **opens a new cell**

```
shift + Enter
```

- Runs the code **without openning a new cell**

```
ctrl + Enter
```

- **Cuts** the select cell

```
x
```

- **Copies** the select cell

```
c
```

- **Deletes** the Cell

```
d pressed twice
```

- **Paste** the copied / cut cell

```
v
```

- Creates a **empty** cell **above**

```
e
```

- Creates a **empty** cell **below**

```
b
```

- Creates a new **markdown** cell

```
m
```

- Creates a new **code** cell

```
y
```

## Using Numpy package
```python
import numpy as np

a = np.array([1,2,3,4],[5,6,7,8])

print(a)

a.shape
# (2l, 4L) meaning having two lines and four columns

a[1,3] 
# renders 8

a[1,3] = 9 
# replaces 8 for 9

a[1] = [5,6,7,8]

```

# Generating Random Number (Simulation)

```python
import random

probability = random.random()
print(probability)

# Throwing a die
number = random.randint(1,6)
print(number)

import numpy as np

np.random.randint(1,6, (4,6))
# throws a die (1,6), in 4 rounds of 6 tries (4,6)

```

## Importing and Organizing Your Data - Part I

```python
import numpy as np
import pandas as pd

# series are single Column Data
# 0 0.65
# 1 0.64
# 2 0.77
# 3 0.92
# 4 0.00
# name: Column 01, dtype: float64

pandas_serie = pd.Series(np.random.random(5), name = "Column 01")

print(ser)

print(ser[2])
```

### Pandas DataFrames are as series but with several columns

```python
from pandas_datareader import data as web
procter_and_gamble = web.DataReader("PG", data_source="yahoo", start="1995-1-1")
# Parameters
# Stock ticker symbol (e.g. PG, AAPL, MSFT)
# data_source (e.g "yahoo")
# Started date (e.g. "1995-1-1")
print(procter_and_gamble)
```

```python
# Days such holidays and weekdays are not computed since the stock market doesn't operate in those days

print(procter_and_gamble)
# Date | Open | High | Low | Close | Volume | Adj Close |

print(procter_and_gamble.info())
# <class "pandas.core.frame.Dataframe">
# DatetimeIndex: 5595 entries, 1995-01-03 to 2017-03-22
# Data columns (total 6 columns):
# Open      5595 non-full float64
# High      5595 non-full float64
# Low       5595 non-full float64
# Close     5595 non-full float64
# Volume    5595 non-full int64
# Adj Close 5595 non-full float64
# dtypes: float64(5), int64(1)
# memory usage: 306.0 KB

```
### Shows the first 5 results
```python
procter_and_gamble.head()
```

### Shows the last 5 results
```python
procter_and_gamble.tail()
```

### Shows the first n results
```python
procter_and_gamble.head(20)
```

### Shows the last n results
```python
procter_and_gamble.tail(17)
```


### Pandas DataFrames with several tickers
```python
tickers = ["PG", "MSFT", "T", "F", "GE"]

new_data = pd.DataFrame()

for ticker in tickers:
	new_data[ticker] = web.DataReader(ticker, data_source = "yahoo", start="1995-1-1")["Adj Close"]
```                 

### MUST have Python packages

#### Scipy Library (numpy, pandas, matplotlib, random, statsmodels) All included on Anaconda's package
- Numpy: (Multidimensional arrays [matrix])
- Pandas: (PANel DAta Sets) Organizes data in tabular forms and attach descriptive labels to the rows and columns of the table
- Matplotlib: (2D plotting [graphical technique for represent a data set] library designed for visualization of Numpy computations)
- Math: (Mathematical Functions)
- Random: (random number generator)
- Statsmodels: (Descriptive statics, plotting functions, regressions ...)

- Pandas_datareader (need to be installed)
```
$ anaconda activate

$ pip install pandas_datareader
```



