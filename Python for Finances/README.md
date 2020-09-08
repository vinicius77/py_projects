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

## Correlation (Measuring the Correlation between Stocks)

### (1) Perfect Positive Correlation Coeficient
- The entire variability of the second variable is explained by the first variable
E.g. (Housing Prices)
- House prices are directly proportionate to the house size
- For every square foot of house size, the price increases by "X"
- In this example, size is the only variable that determines house prices
- It is called PERFECT POSITIVE CORRELATION because when added plus 1 additional square foot the price goes up plus x dollars (it moves in the same direction)

* In reality, several variables have an impact on house prices (location, year of construction and so on)
* In the same way, several variables detrmine share prices: (industry growth, profitability, regulatory environment)

* The more similar the context in which two companies operate, the more correlation there will be between their share prices as they will be influenced by the same or similar facts.

### (0) No Correlation Coeficient
- Variables with 0 correlation are absolutely independent from each others
E.g. Coffee price in Brazil x House prices in London

### (-1) Negative Correlation Coeficient
- Two variables that move in opposite directions
#### Perfect Negative Correlation (-1)
#### Imperfect Negative Correlation (between -1 and 0)

E.g. Ice Cream Producers x Umbrella producers
- People buy more ice cream when the weather is good, the reverse happens with umbrellas
- Exists a negative correlation between the two, in other words, when a company makes more money the other won't.
- This is the example of a situation where the prices of two companies are influenced by the same variable but the variable impacts their business in a different way.

### Considerating the risk of multiple securities in a portfolio

- **Portfolio Variance:** If a portfolio contains two stocks its risk will be a function of the variance of the two stocks and the correlation between them.

(a + b)² => a² + 2ab + b²

* Example of the formula for two stocks:
**(w1σ1 + w2σ2)² = w1²σ²1 + 2w1σ1w2σ2ρ12 + w2²σ²2**

**The Formula Explained:**
- weight1 to the second degree times of the variance of the first stock (w1σ1) plus
- two times the product of weight1, weight2 and the covariance between the two stocks (2w1σ1w2σ2ρ12) plus
- weight2 to the second degree times of the variance of the second stock (w2σ2)

- **σ** = standard deviation (the square root of the Variance)
- **w** = weight
- **ρX,Y** = correlation of variables X and Y
- **Reminder:** The sum of the stocks's weight, in this case w1σ1 + w2σ2, must be 1 or, in other words, 100% of the portfolio of stocks.

```python
import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

tickers = ["PG", "BEI.DE"]

securities_data = pd.DataFrame()

for ticker in tickers:
    securities_data[ticker] = web.DataReader(ticker, data_source="yahoo", start="2007-1-1")["Adj Close"]

# using np.log() because we will analise the data of the securities separately 
securities_return = np.log(securities_data / securities_data.shift(1))

#Equally weighted portfolio (of two stocks)
weights = np.array([0.5, 0.5])

# Diversifiable risk = portfolio variance - weighted annual variances
PG_annual_variance = securities_return["PG"].var() * 250
BEI_annual_variance = securities_return["BEI.DE"].var() * 250

# Portfolio Variance
pfolio_variance = np.dot(weights.T, np.dot(securities_return.cov() * 250, weights))

# Diversifiable Risk
diversifiable_risk = pfolio_variance - (weights[0] ** 2 * PG_annual_variance) - (weights[1] ** 2 * BEI_annual_variance)

# round(diversifiable_risk * 100, 3) in percent

# Non-Diversifiable Risk:
non_diversifiable_risk = pfolio_variance - diversifiable_risk

# or also this formula below must lead to the same result
# non_diversifiable_risk_2 = (weights[0] ** 2 * PG_annual_variance) + (weights[1] ** 2 * BEI_annual_variance)

```

### Understanding Risk
#### Undiversifiable / Systematic
This component depends on the variance of each individual security.
E.g. Recession of the economy, low consumer spending, war, forces of nature etc.

#### Diversifiable risks / Idiosyncratic (Company Specific Risks)
Is driven by company-specific events.
- They can be eliminated if is invested in non-correlated assets, for instance, automotive, construction, energy, technology stocks.

## Regression Analysis (Quantifies the relationship between two variables [dependent and independent/explanatory variables])
- Useful when is needed forecast a future dependent variable with the help of patterns for the historical data.

**E.g.** Houses (The larger a house, the higher its price)
### Variables
- Size (Explanatory Variable) *helps to explain why certains houses cost more.
- Price (Dependent Variable) *as it has been explained

If is known the value of the explanatory variable (size) it can be determined the value of the dependent variable (house's price).

In real-life, size is not the only explanatory variable to determine house prices.
### Simple Regression: Using only one variable (as the example above)
e.g:
y = house price
x = house size

Using a x/y plot each observation we see in the plot indicates that the two variables are connected, in other words, bigger houses higher prices.

**Regression analysis** assumes the existence of a linear relationship between the two variables.

One straight line is the best fit and can help to describe the rapport (a relationship characterized by agreement, mutual understanding, or empathy that makes communication possible or easy) between all the data points we see in the plot. 

### How do we draw the best-fitting line?
- Find a line that minimizes the error observed between itself and actual observations
- **Linear regression** calculates the error observed when using different lines and will determine which one contains the least error.
Each deviation from the line is an **error** because it deviates from the prediction the line would have provided.
- The best fitting line contains the least amount of estimation error.

### Linear Equation: (The general equation of a straight line)
**y = mx + b** or **y = βx + α**
- m = slope of the line
- b = the y intercept

(The **slope** is a measure of how the line angles away from the horizontal)
(The **Y-Intercept** of a line is the point where a line's graph intersects (crosses) the Y-axis. 
**E.g.** a y-intercept of 3 means that a line's graph intersects the Y-axis at the point (0,3)) 

### Multivariable Regression: Using more than one (explanatory) variable

## How to distinguish good and bad regressions
**E.g.** Houses
- More than one variable determines house prices (location, neighborhood, year of construction and so on)
- A simple regression will omit some importatnt factors, which will result in an estimation error. (It is useful but not perfect)
- The **regression model** can be written as **Y = βx + α + error**
- **error => residuals** (A residual is the vertical distance between a data point and the regression line)
- The best fitting line minimizes the sum of the squared residuals
- The coefficients found with this technique are called **Ordinary Least Squared (OLS) Estimates**

### Are all regressions created equal?
- Certain variables are better at predicting than other variables
- House size is on of the better indicators of house prices (makes sense explore the relationship between the two variables through a regression.)
- Owner's age in house prices is not a good indicator so doesn't make sense use this variable calculating a regression. (buyers will not be influenced for the age of the people who sells a house)
- **Some regressions have higher explanatory power than others.**

### Good vs Bad Regressions (Using the R square)

How can we measure data dispersion and variability?
- We use variance to measure the variability of data:
**e.g:** s² = ∑(X - ẍ)²
		      _________
			    N - 1

- **Total Sum of Squares (TSS):**
Provides a sense of the variability of data
**e.g:** TSS = ∑(X - ẍ)²

### R Formula
- R square varies between 0% and 100%. The higher it is, the more predictive power the model has
**Formula:** R² = 1 - SSR / TSS

**(SSR)** => The Sum of Squared Residuals 
**(TSS)** => Total Sum of Squares

## (Harry) Markowitz Theory
- Proves the existence of an efficient set of portfolios 
- Investors should understand the relationship between the securities in their PORTFOLIO.
- The combination of securities with LITTLE correlation allows investors to optimize their return without assuming additional risks
- Diversified portfolio => Higher returns and no additional risks
- Investors are risk averse (Investor is an investor who prefers lower returns with known risks rather than higher returns with unknown risks.)

## Calculating the Standard Deviation for Porfolio 1 (EXPLAINED [Excel File]):

```
Weight A ^ 2 [100% ^ 2]
* variance of security A ^ 2 (standard deviation [5% ^ 2])
+ Weight B ^ 2 [0% ^ 2]
* variance of security B ^ 2 (standard deviation [8% ^ 2])
+ 2 * the correlation coefficient between stocks A and B [2 * 30%]
* the weights of the two stocks [100% * 0%]
* the standard deviation of two stocks [5% * 8%]
```

**(w1σ1 + w2σ2)² = w1²σ²1 + 2w1σ1w2σ2ρ12 + w2²σ²2**
 
w1²σ²1 = **100% ^ 2 * 5% ^ 2**
+
2w1σ1w2σ2ρ12 = **2 * 30% * 100% * 0% * 5% * 8%**
+
w2²σ²2 = **0% ^ 2 * 8% ^ 2**

**(w1σ1 + w2σ2)²** = 

- This is the diversifiable component of the portfolio
- The lower the correlation coefficient the greater the diversification effect at the combination of two stocks will have
- To obtain the standard deviation of the portfolio we need the square root of the number ^ (1/2).

(Plots in a two axis chart where the **horizontal axis contains the risk of the portfolio** the and the **vertical axis contains its expected return**

We obtained the typical **shape of Markowitz Frontier** [Efficient Frontier])


### Obtaining The Efficient Frontier Part I, II, III
- Explained in the Jupyter Notebook of the same name.

## The Capital Asset Pricing Model (CAPM)
(Risk-averse, prefer hogher returns, willing to buy the optimal portfolio)

**Market Portfolio** - A combination of all the possible investments in the world (both bonds and stocks)

- The only risk faced is the systematic one.
- the CAPM assumes the existence of a risk-free asset
- It has a lower expected rate of return because investors are only compensate for the added risk they are willing to bear.
- Investors will allocate their money between the risk-free and the market portfolio.
- The line that connects the risk-free rate and its tangent to the efficient frontier is called **the Capital Market Line**.
- The point where the Capital Market Line intersects the efficient frontier is the market portfolio.
- Depending on their risk preferences, they will choose to buy more of the risk-free asset or more of the market portfolio.

### Beta (One of the main pillars of the CAPM)

It helps us to quantify the relationship between a security and the overall market portfolio.

**Safer Stocks** will earn **less** than the market portfolio when the economy grows.
**Riskier Stocks** will earn **more** than the market portfolio when the economy grows.

### Measuring Beta

β = Cov(rx,rm) / σ²m

- It can be calculated as the covariance between the stock and the market, divided by the variance of the market.
- The riskier is the stock, the higher is its Beta and vice-versa.
- Measures the market risk that cannot be avoided through diversification.
- β = 0 (No Relationship) | β < 1 (Defensive) | β > 1 (Offensive)
- **Example:** Walmart β = 0.09 | Ford β = 1.1
- **Beta is a measurement that shows how risky an individual security is, regarding the rest of the market**

### The Capital Asset Pricing Model
ri = rf + βim(rm-rf)

**Legend:**
- rf = risk free
- βim = Beta between the stock and the market
- rm = market return

#### Applying the CAPM in practice**
Calculating P&G's expected rate of return

* Risk-free
Approximate with 10 year US government bond yield: 2.5%

* Beta
Approximate the market portfolio with the S&P 500: 0.62
(The best proxy for market portfolio is a wide index traded in the home country of the security)

* Equity Risk Premium
Historically, it has been between 4,5% and 5.5%

ri = rf + βim(rm-rf)
r(i) = 2.5% + 0.62 * 5%
r(i) = 5.6% 

**Conclusion:** When an investor buys P&G's shares he would expect to earn 5.6% to be compensate for the risk he is taken. 

### Sharpe Ratio

**A rational investor considers both risk and return**

sharpe_ratio = ri - rf / σi

**Legends:**
- rf = risk-free rate
- ri = rate of return of the stock "i"
- σi = standard deviation of the stock "i"

The sharpe ratio allow us to compare:
- Stock A vs Stock B
- Investment Portfolio A vs Investment Portfolio B

















































