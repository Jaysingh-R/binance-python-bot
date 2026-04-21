# Binance Futures Testnet Trading Bot

A Python CLI application to place Market and Limit orders on the Binance Futures Testnet.

## Bonus Feature Implemented
* **Enhanced CLI UX**: Utilized `Typer` and `Rich` to provide interactive prompts (if arguments are missing), input validation messages, and cleanly formatted summary tables for API responses.

## Setup Instructions

1. Clone the repository or extract the zip.
2. Create a virtual environment: `python -m venv venv` and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file in the root directory and add your testnet credentials:
   ```text
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_secret_key