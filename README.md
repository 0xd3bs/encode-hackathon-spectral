

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

This starter kit is written in Python, you are free to use any language you want.
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

This project is designed to help users identify market trends and make informed trading decisions using the following libraries and APIs:
- Data wrangling and indicator generation with `pandas`, `numpy`, `ta`
- Trading API integration with Binance
- Language model API integration with OpenAI's gpt-4o-mini

### Key Functions

- **Data download**: Retrieves historical market data.
- **Calculation of indicators**: Computes various technical indicators.
- **Signal generation**: Identifies buy/sell signals based on indicators.
- **Operations executor**: Executes trades on the Binance exchange.
- **Log function**: Records trading activities.
- **Agent executor**: Runs the trading agent based on predefined schedules.

---
