"""
Markov Trading - Point d'entrée principal
Usage: python main.py --ticker AAPL --action analyze
"""

import argparse
import json
import logging
from pathlib import Path

from markov import (
    get_market_signals,
    screen_stocks,
    analyze_company,
    calculate_dcf,
    get_market_regime,
)


def setup_logging(level: str = "INFO"):
    """Configure le logging pour l'application."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def cmd_analyze(ticker: str, verbose: bool = False):
    """Analyse complète d'un actif."""
    logger = logging.getLogger("markov.analyze")
    logger.info(f"Analyse de {ticker}...")

    # Signaux techniques
    signals = get_market_signals(ticker)
    
    if verbose:
        print(f"\n📊 Signaux techniques pour {ticker}:")
        print(json.dumps(signals, indent=2))
    else:
        print(f"✅ Analyse {ticker} terminée")

    return signals


def cmd_screen(market: str = "america", limit: int = 20, rsi_max: int = 30):
    """Screen des actifs selon critères."""
    logger = logging.getLogger("markov.screen")
    logger.info(f"Screen {market} - RSI < {rsi_max}...")

    results = screen_stocks(
        filters=[{"field": "RSI", "operator": "less", "value": rsi_max}],
        markets=[market],
        limit=limit,
    )

    print(f"\n🔍 {len(results)} résultats trouvés:")
    for r in results:
        print(f"  - {r.get('name', r.get('ticker'))} | RSI: {r.get('RSI', 'N/A')}")

    return results


def cmd_regime():
    """Analyse du régime de marché."""
    regime = get_market_regime()
    
    print(f"\n📈 Régime de marché actuel: {regime.get('current', 'UNKNOWN')}")
    print(f"   Volatilité: {regime.get('volatility', 'N/A')}")
    
    return regime


def cmd_dcf(ticker: str):
    """Valorisation DCF d'un actif."""
    result = calculate_dcf(ticker)
    
    print(f"\n💰 Valorisation DCF pour {ticker}:")
    print(f"   Fair Value: {result.get('fair_value', 'N/A')}")
    print(f"   Marge: {result.get('margin', 'N/A')}")
    
    return result


def main():
    """Point d'entrée CLI."""
    parser = argparse.ArgumentParser(
        description="Markov Trading - Agent IA d'Analyse de Marchés Financiers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  %(prog)s --ticker AAPL --action analyze
  %(prog)s --action screen --market america --rsi-max 30
  %(prog)s --action regime
  %(prog)s --ticker AAPL --action dcf
        """,
    )

    parser.add_argument("--ticker", "-t", type=str, help="Ticker de l'actif (ex: AAPL)")
    parser.add_argument(
        "--action", "-a",
        type=str,
        choices=["analyze", "screen", "regime", "dcf"],
        default="analyze",
        help="Action à effectuer"
    )
    parser.add_argument("--market", "-m", type=str, default="america", help="Marché cible")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Limite de résultats")
    parser.add_argument("--rsi-max", type=int, default=30, help="RSI max pour screening")
    parser.add_argument("--verbose", "-v", action="store_true", help="Mode verbose")
    parser.add_argument("--log-level", type=str, default="INFO", help="Niveau de log")

    args = parser.parse_args()
    setup_logging(args.log_level)

    # Exécution selon l'action
    if args.action == "analyze" and args.ticker:
        cmd_analyze(args.ticker, args.verbose)
    elif args.action == "screen":
        cmd_screen(args.market, args.limit, args.rsi_max)
    elif args.action == "regime":
        cmd_regime()
    elif args.action == "dcf" and args.ticker:
        cmd_dcf(args.ticker)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
