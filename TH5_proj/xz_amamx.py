import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.stats.diagnostic import acorr_ljungbox
import warnings
warnings.filterwarnings('ignore')

# Set style for plots
plt.style.use('seaborn')
sns.set_palette("husl")

def load_data():
    """Load and preprocess the unemployment data"""
    df = pd.read_csv('datasets/unemployed_population_1978-12_to_2023-07.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df

def plot_time_series(data, title):
    """Plot the time series with proper formatting"""
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data.values)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate')
    plt.grid(True)
    plt.show()

def test_stationarity(timeseries):
    """Perform Augmented Dickey-Fuller test for stationarity"""
    print('Results of Augmented Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)

def plot_acf_pacf(data):
    """Plot ACF and PACF to determine ARIMA parameters"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    plot_acf(data, ax=ax1)
    plot_pacf(data, ax=ax2)
    plt.tight_layout()
    plt.show()

def main():
    # Load data
    df = load_data()
    
    # Plot original time series
    plot_time_series(df, 'Unemployment Rate Time Series')
    
    # Test for stationarity
    test_stationarity(df)
    
    # Plot ACF and PACF
    plot_acf_pacf(df)
    
    # TODO: Add structural break detection
    # TODO: Add ARIMA modeling
    # TODO: Add model diagnostics

if __name__ == "__main__":
    main()
