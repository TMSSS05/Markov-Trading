"""
Markov Trading - Agent IA d'Analyse de Marchés Financiers
"""

__version__ = "1.0.0"
__author__ = "Thomas Cogné"

from .fetch.tradingview import get_market_signals, screen_stocks
from .analyze.fundamental import analyze_company, calculate_dcf
from .analyze.macro import get_market_regime

__all__ = [
    "get_market_signals",
    "screen_stocks",
    "analyze_company",
    "calculate_dcf",
    "get_market_regime",
]
