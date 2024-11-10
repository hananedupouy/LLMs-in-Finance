# filename: apply_momentum_trading.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from momentum_trading_strategy import momentum_trading_strategy

# Fetch NVIDIA historical data for the year 2024
nvidia = yf.download('NVDA', start='2024-01-01', end='2024-11-10')

# Define pairs of moving averages
ma_pairs = [(5, 20), (10, 50), (20, 100), (50, 200)]

# Apply and process each moving average pair
for short_window, long_window in ma_pairs:
    # Apply the trading strategy
    signals = momentum_trading_strategy(nvidia, short_window, long_window)
    
    # Save results in a CSV file
    csv_filename = f'nvidia_trading_strategy_{short_window}_{long_window}.csv'
    signals.to_csv(csv_filename)
    
    # Plot the trading strategy
    plt.figure(figsize=(10, 5))
    plt.plot(signals['price'], label='Price')
    plt.plot(signals['short_mavg'], label=f'Short MA ({short_window})')
    plt.plot(signals['long_mavg'], label=f'Long MA ({long_window})')
    plt.legend()
    plt.title(f'Trading Strategy with MA {short_window} and {long_window}')
    plt.savefig(f'nvidia_trading_strategy_{short_window}_{long_window}.png')
    plt.close()
    
    # Plot buy and sell signals
    buy_signals = signals[signals['positions'] == 1.0]
    sell_signals = signals[signals['positions'] == -1.0]
    
    plt.figure(figsize=(10, 5))
    plt.plot(signals['price'], label='Price')
    plt.scatter(buy_signals.index, buy_signals['price'], marker='^', color='g', label='Buy Signal')
    plt.scatter(sell_signals.index, sell_signals['price'], marker='v', color='r', label='Sell Signal')
    plt.legend()
    plt.title(f'Buy and Sell Signals with MA {short_window} and {long_window}')
    plt.savefig(f'buy_sell_signals_{short_window}_{long_window}.png')
    plt.close()
    
    # Compute final return
    returns = signals['price'].pct_change().fillna(0)
    strategy_returns = returns * signals['signal'].shift(1).fillna(0)
    cumulative_return = (1 + strategy_returns).cumprod()[-1] - 1
    
    print(f'Final return for MA pair ({short_window}, {long_window}): {cumulative_return:.2%}')