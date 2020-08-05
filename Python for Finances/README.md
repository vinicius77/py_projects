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

### Importing and organizing data (PART III)
```
$ pip install quandl
```

```python
import quandl
# https://www.quandl.com/tools/python

# GPD: Gross domestic product

# Gross domestic product is a monetary measure of the market value of all the final goods and services
# produced in a specific time period.

# FRED: Short for Federal Reserve Economic Data, FRED is an online database consisting of hundred of thousands of economic data time series from scores of national, international, public, and private sources.

# For example, to get US GDP from FRED, just do this:
mydata_01 = quandl.get("FRED/GDP")

mydata_01.tail()
mydata_01.head()

# saves the data in .csv format
mydata_01.to_csv("/home/kako77sub/Desktop/example_01.csv")

# reads the .csv file using pandas package
mydata_02 = pd.read_csv("/home/kako77sub/Desktop/example_01.csv")

# saves the data in .xlsx format 
mydata_02.to_excel("/home/kako77sub/Desktop/example_02.xlsx")

# reads the .xlsx file data using pandas package
mydata_03 = pd.read_excel("/home/kako77sub/Desktop/example_02.xlsx")
```

### Finance Calculating and Comparing Rates of Return in Python

Profit x Loss

- Bonds (%3 return rate / low risk / initial investment plus interest)
- Stock (%6 return rate / high fluctuation / price change)

#### SIMPLE RATE RETURN

				 ending price - beginning price
rate of return = _______________________________
 						beginning price

Example: $116 - 105$
		 ___________ => 10.5%
			$105

* Dividends => a reward that a copany gives to its shareholders
* Assets => Something valuable that an entity owns, benefits from or has use of, in generating income.
* Timeframe => given period (daily, weekly, monthly, annually)
- When dealing with multiple assets over the same time frame

```python
PG["simple_return"] = (PG["Adj Close"] / PG["Adj Close"].shift(1)) - 1

PG["simple_return"].plot(figsize=(8, 5))
plt.show()

average_returns_daily = PG["simple_return"].mean()
print(average_returns_daily)

average_returns_annually = PG["simple_return"].mean() * 250
print(average_returns_annually)

print(f"Annual return {round(average_returns_annually, 5) * 100} %")

```

#### LOGARITHMIC RATE RETURN

Example: log $116 
			______ => (log $116 - log $105) = 10%
			 $105

* log 100 = 2 because 10 ** 2 = 100 
- When you make calculations about a single asset over time

INVESTMENTS WITH DIFFERENT HOLDING PERIODS SHOULD NOT BE COMPARED 

```python
PG["logarithm_return"] = np.log(PG["Adj Close"] / PG["Adj Close"].shift(1))
print(PG["logarithm_return"])

PG["logarithm_return"].plot(figsize=(8,5))
plt.show()

daily_logarithm_return = PG["logarithm_return"].mean()
print(daily_logarithm_return)

annualy_logarithm_return = PG["logarithm_return"].mean() * 250
print(annualy_logarithm_return)

print(f"The anually logarithm return from Procter & Gamble is {round(annualy_logarithm_return, 5) * 100} %")

```

### Annual Rate of Return Calculation
[Investopedia](https://www.investopedia.com/terms/a/annual-return.asp)

### Calculating return of multiple investiments (Portfolio of securities)

anually rate of return | weigth | security |     historical rate     | expected rate of return of the portfolio
0,318524			   |   25%  |   Apple  | 25% * 0,318524 = 0,079  |
0,153581			   |   25%  |    IBM   | 25% * 0,153581 = 0,038  | => = 0,178761
0,116717			   |   25%  |    G E   | 25% * 0,116717 = 0,029  |
0,126224			   |   25%  |   FORD   | 25% * 0,126224 = 0,031  |

* Same calculation applies for differently weighted securities

### Market Index
- Provides an idea of how a given stock is performing (overall marketing performance)
- Good proxy (approximation) for the development of the market

### Most Known

#### Standard & Poor's (S&P 500)
- 500 largest listed companies
- Market-cap weighted (if the market-cap of P&G is three times the market-cap of Nike, one porcent change in P&G 
share price will have 3 times the impact of one porcent change in Nike's share price)
- Diverse constituency (Makes the TRUE approximation of the US stock market)

#### Dowjones
- 30 large public stocks
- equally weighted
- Not a true representation of US market since it covers only 30 stocks

#### Nasdaq
- Group securities
- Has most IT companies
- Rate of return of tech stocks

#### Others
- FTSE (UK)
- DAX30 (Germany)
- Nikkei (Japan)
- Shanghai Stock Exchange (CHINA)
- MSCI (Global - includes stocks from all developed markets in the world)

#### Why know about stock indices?

- Stocks indices are an excellent comparator to understand how your own stocks are performing
- They indicate what to expect if you invest in a diversified portfolio

### Calculating the rate of return of indices

```python
import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# ^ indicates the dealing with market index data
# ^GSPC => S&P 500
# ^IXIC => Nasdaq
# ^GDAXI => German DAX
# ^FTSE => London FTSE
tickers = ["^GSPC", "^IXIC", "^GDAXI"]

indicies_data = pd.DataFrame()

for ticker in tickers:
    indicies_data[ticker] = web.DataReader(ticker, data_source="yahoo", start="1997-1-1")["Adj Close"]

indicies_data.info()
indicies_data.head()
indicies_data.tail()

# Normalizing Data

(indicies_data / indicies_data.iloc[0] * 100).plot(figsize=(15,6))
plt.show()

# Calculating Indicies' Simple Returns
indices_simple_return = (indicies_data / indicies_data.shift(1)) - 1
indicies_data.tail()

# Calculating the Annual Return of Marketing Indices

annual_indicies_return = indices_simple_return.mean() * 250
print(annual_indicies_return)

# Putting the adjusted closing price of a company compared with the performance of one of the indicies

# ^DJI => Down Jones
tickers = ["PG", "^GSPC", "^DJI"]

data_2 = pd.DataFrame()

for ticker in tickers:
    data_2[ticker] = web.DataReader(ticker, data_source="yahoo",start="1997-1-1")["Adj Close"]

# Normalizating in Plotting Data

(data_2 / data_2.iloc[0] * 100).plot(figsize=(15,6))
plt.show()

#This is how we can compare the performance of stocks in stock indicies.

#(The first type of analysis that we need to perform when analysing stock market.)

```

## How to measure (and forecast) a security's risk

### Variability - Best measure of risk

#### Statistics Measures (to quantity risks)
- s2 => variance (measures the dispersion of a set of data points around the mean)

**Formula:** the variance (s²) is equal (=) to the sum (∑) of the squares of the difference between a data point X and the mean (Ẍ) divided by N (the number of observations) - 1.

e.g: s² = ∑(X - ẍ)²
		___________
			N - 1

**In practice:**
- if the mean of four data points is 15% (ẍ = 15)
- calculating the dispersion of each of the four points and elevating to the second degree 
(14% - 15%)² = 0.01%
(16% - 15%)² = 0.01%
(13% - 15%)² = 0.04%
(17% - 15%)² = 0.04%
∑ = 0.01% +0.01% +0.04% +0.04%
∑ = 0.1%

s² = 0.1% / (N - 1)
s² = 0.1% / (4 - 1)
s² = 0.033%
s² = 0.00033 (<= the variance result)

- s => standard deviation (the square root of the variance)
(Greater the deviation is mean riskier)
s = √s²
s = √0.00033
s = 1.8%

### Benefits of portfolio diversification
- Favorable macroeconomic conditions facilitate the business of all companies
- In times of recession, consumers spending decreases and business suffer
- Share prices are influenced by the state of the economy
- The state of the economy impacts industries in a different way
- Is better to invest in companies operating in different industries
- There is a relationship between the prices of companies which will help us to optimize investment portfolios

### Calculating the covariance between stocks
(Measuring the relationship between stocks)

**E.g.**(House Pricing) [House sizes and prices]

Formula:
(The correlation coefficient measures the relationship between two variables)
x = house size / y = house price

Pxy = (x - ẍ) * (y - ÿ)
	___________________
			σxσy

House Listing
Size     | Price	| (x - ẍ) * (y - ÿ)	
673 sqft | $772.000 | (673 - 893.2) * (772 - 886600) = 25324.920
785 sqft | $998.000 | (785 - 893.2) * (998 - 886600) = -12053.480
1334 sqft| $999.000 | (1334 - 893.2) * (999 - 886600) = 49545.920
699 sqft | $769.000 | (699 - 893.2) * (769 - 886600) = 22837.920
975 sqft | $895.000 | (975 - 893.2) * (895 - 886600) = 687.120

Average:
Size = 893.2
Prices = 886600

SUM of all (x - ẍ) * (y - ÿ) => 86252.400

Covariance (SUM / N - 1) => 21563.100

- if covariance > 0 => The two variables (x,y) move in the same direction
- if covariance < 0 => The two variables (x,y) move in the opposite direction
- if covariance == 0 => The two variables (x,y) are independent

### Correlation




















