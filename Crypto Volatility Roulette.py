import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


cryptos = ["Bitcoin", "Ethereum", "Stablecoin"]
start_prices = [30000, 2000, 1]  # starting values

days = 100
crypto_sim = {}

for i, crypto in enumerate(cryptos):
    prices = [start_prices[i]]
    for d in range(1, days):
        if crypto == "Bitcoin":
            daily_return = np.random.normal(0.001, 0.05)  # wild swings
        elif crypto == "Ethereum":
            daily_return = np.random.normal(0.001, 0.03)  # medium swings
        else:
            daily_return = np.random.normal(0.0001, 0.001)  # almost flat
        prices.append(prices[-1] * (1 + daily_return))
    crypto_sim[crypto] = prices
plt.figure(figsize=(12,6))
for crypto in cryptos:
    plt.plot(crypto_sim[crypto], label=crypto)

plt.title("Crypto Volatility Roulette - Price Simulation")
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

for crypto in cryptos:
    print(f"{crypto} Volatility (Std Dev):", np.std(crypto_sim[crypto]))
