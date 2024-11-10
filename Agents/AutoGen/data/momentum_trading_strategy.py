# filename: momentum_trading_strategy.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def download_data(symbol, start, end):
    """Download historical stock data"""
    df = yf.download(symbol, start=start, end=end)
    return df

def momentum_trading_strategy(df, short_window=40, long_window=100):
    """Implement a simple moving average crossover trading strategy"""
    signals = pd.DataFrame(index=df.index)
    signals['price'] = df['Close']
    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1).mean()
    
    # Using loc to avoid the FutureWarning
    signals.loc[signals.index[short_window:], 'signal'] = np.where(
        signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0
    )
    
    signals['positions'] = signals['signal'].diff()
    return signals

def save_strategy_results(signals, filename='nvidia_trading_strategy.csv'):
    """Save strategy results to CSV"""
    signals.to_csv(filename)

def plot_strategy(signals, filename='nvidia_trading_strategy.png'):
    """Plot the price and trading signals"""
    plt.figure(figsize=(12, 8))
    plt.plot(signals['price'], label='Stock Price')
    plt.plot(signals['short_mavg'], label='Short-term MAV')
    plt.plot(signals['long_mavg'], label='Long-term MAV')
    plt.plot(signals.loc[signals.positions == 1.0].index, 
             signals.short_mavg[signals.positions == 1.0],
             '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(signals.loc[signals.positions == -1.0].index, 
             signals.short_mavg[signals.positions == -1.0],
             'v', markersize=10, color='r', label='Sell Signal')
    plt.title('NVIDIA Trading Strategy')
    plt.legend()
    plt.savefig(filename)

def compute_final_return(signals, filename='final_return.png'):
    """Compute and plot the final cumulative return of the trading strategy"""
    signals['strategy_returns'] = signals['positions'].shift(1) * (signals['price'].pct_change())
    signals['cumulative_strategy_return'] = (signals['strategy_returns'] + 1).cumprod()
    
    plt.figure(figsize=(12, 8))
    plt.plot(signals['cumulative_strategy_return'], label='Cumulative Strategy Return')
    plt.title('Final Return of the Trading Strategy')
    plt.legend()
    plt.savefig(filename)

def main():
    start_date = '2023-01-01'
    end_date = '2023-10-31'
    symbol = 'NVDA'
    
    # Step 2: Download the historical data
    df = download_data(symbol, start_date, end_date)

    # Step 3: Apply the strategy
    signals = momentum_trading_strategy(df)

    # Step 4: Save the results
    save_strategy_results(signals)

    # Step 5: Plot the strategy
    plot_strategy(signals)

    # Step 7: Compute and plot final return
    compute_final_return(signals)

if __name__ == '__main__':
    main()