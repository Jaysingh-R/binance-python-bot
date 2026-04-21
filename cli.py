import typer
from rich.console import Console
from rich.table import Table
from bot.orders import place_order

app = typer.Typer(help="Binance Futures Testnet Trading Bot")
console = Console()

@app.command()
def trade(
    symbol: str = typer.Option(..., prompt="Enter Trading Symbol (e.g., BTCUSDT)"),
    side: str = typer.Option(..., prompt="Enter Side (BUY/SELL)"),
    order_type: str = typer.Option(..., prompt="Enter Order Type (MARKET/LIMIT)"),
    quantity: float = typer.Option(..., prompt="Enter Quantity"),
    price: float = typer.Option(None, help="Price (Required for LIMIT orders)")
):
    """Place a trade on Binance Futures Testnet."""
    
    if order_type.upper() == 'LIMIT' and price is None:
        price = typer.prompt("Enter Price for LIMIT order", type=float)

    console.print(f"\n[bold yellow]Processing {side.upper()} order for {quantity} {symbol.upper()}...[/bold yellow]")
    
    result = place_order(symbol, side, order_type, quantity, price)
    
    if result["success"]:
        data = result["data"]
        console.print("[bold green]✔ Order Successfully Placed![/bold green]\n")
        
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Order ID", style="dim")
        table.add_column("Symbol")
        table.add_column("Status")
        table.add_column("Executed Qty")
        table.add_column("Avg Price")
        
        table.add_row(
            str(data.get("orderId")),
            data.get("symbol"),
            data.get("status"),
            str(data.get("executedQty")),
            str(data.get("avgPrice", "N/A"))
        )
        console.print(table)
    else:
        console.print(f"[bold red]✘ Order Failed:[/bold red] {result['error']}")

if __name__ == "__main__":
    app()