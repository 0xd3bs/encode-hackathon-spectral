

---

# Encode Hackathon Spectral

## Environment Setup

To run this project locally, you'll need to set up the required environment variables:

1. Copy the environment variables example file:
   
   ```bash
   cp .env.example .env
   ```
   
   Alternatively, you can manually copy the `.env.example` file and rename it to `.env`

2. Open the `.env` file and replace the example values with your own API keys:
   - OPENAI_API_KEY: Your OpenAI API key
   - BINANCE_API_KEY: Your Binance API key
   - BINANCE_API_SECRET: Your Binance API Secret

⚠️ **Important**: 
- Never commit or share your `.env` file containing real API keys
- The `.env` file is included in `.gitignore` to prevent accidental commits
- Keep your API keys secure and never share them publicly

## Setup

This project is written in Python, you are free to use any language you want.
We use OpenAI's GPT-4o model for this example, but you are free to use any model you want.
If you follow the starter kit, you will need an OpenAI API key. 

We recommend using [UV](https://github.com/astral-sh/uv) (An extremely fast Python package and project manager, written in Rust) to manage your project.

If you do not have UV installed, you can install it with:
```
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then set up your virtual environment and install the requirements:
```
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Project Overview

This project is designed to help users who follow a moving average crossover strategy to identify trends. Understanding the complexity of the market in price formation, an agent with the personality of a trader experienced in trend detection is proposed, which based on its expertise in the analysis of technical indicators, complements the user's strategy with a comprehensive analysis of indicators, in such a way that it advises the trader to make a data-driven decision, when establishing or not a purchase/sale order for a certain cryptocurrency. This agent supports users to identify market trends and make informed trading decisions using the following libraries and APIs:
- Data wrangling and indicator generation with `pandas`, `numpy`, `ta`
- Trading API integration with Binance
- Language model API integration with OpenAI's gpt-4o-mini

### Key Functions

- **get_data(ticker,period)**: This function is used to download the historical series of the asset on which the user wants LLM advice. The data is obtained from the binance testnet api. The data obtained is:
 > - Price: Open, High, Low and Close.
 > - Volume: VolumeCurr (volume of cryptocurrency objective), VolumeUSD (volume of USDT),
 > - Trades: Trades of the cryptocurrency by unit time.
- **get_indicators(df)**: Function for calculating technical indicators based on the prices of the cryptocurrency selected by the user:
 > - var_pct: Percentage change in closing price.
 > - SMA: 20 and 50
 > - MA: 20 and 100 
 > - RSI
 > - MACD and MACD signal
 > - log return: Logarithmic returns of closing price.
 > - pup_6std: Price adjusted upwards using 6 standard deviations.
 > - pdown_6std: Price adjusted downwards using 6 standard deviations.
 > - std_dev: Moving standard deviation of closing price over a 20-period window.
 > - upper and lower band: Bands based on the 20-period simple moving average (SMA) and 6 times the standard deviation.
- **get_signal(df)**: Function to identify buy/sell signals of the asset through a moving average crossover strategy (this is the strategy that the user uses, by default).
- **get_chat(system_prompt,user_message)**: LLM query function, based on the system prompt and user prompt structure.
- **run_agent(ticker,period)**: Function to run the agent, on user-defined cryptocurrency (ticker) and at user-defined periodicity (1m/3m/5m/15m/30m/1h/2h/4h).

### Disclaimer

This repository was created as part of a submission for the Future of Blockchain University Encode Club Hackathon and Spectral's Bounty 2024. The code and information provided are intended for educational and demonstration purposes only and should not be considered financial advice (NFA). Any use of this project is at your own risk. We strongly recommend consulting a qualified financial advisor before making any investment decisions

---
