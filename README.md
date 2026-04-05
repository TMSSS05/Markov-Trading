# 🚀 Markov Trading

> **Agent IA d'Analyse de Marchés Financiers** — Analyse technique, macroéconomique, recherche TradingView et backtesting automatisé.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Price](https://img.shields.io/badge/Price-Gratuit-green.svg)]()

---

## ✨ Fonctionnalités

### 📊 Analyse Technique
- **Screeners avancés** — Filtrage multi-critères sur Actions, Forex, Crypto, ETF
- **Indicateurs techniques** — RSI, MACD, SMA, Bollinger, ATR, ADX et plus
- **Patterns de prix** — Détection de crosses dorées/mortes, supports/résistances
- **Alertes personnalisables** — Surveillance en temps réel des conditions de marché

### 🌐 Recherche Macroéconomique
- **Actualités financières** — Veille automatique sur les marchés
- **Sentiment analysis** — Analyse du sentiment des nouvelles par ticker
- **Benchmarks sectoriels** — Comparaison vs pairs du secteur
- **Signaux de marché** — Indicateurs techniques + sentiment combinés

### 📈 Intelligence Artificielle
- **Analyse DCF** — Valorisation par flux de trésorerie actualisés
- **Backtesting** — Test de stratégies sur données historiques
- **Comparables** — Analyse comparative avec pairs du marché
- **Signaux composites** — Agrégation multi-sources pour décisions

### 🛠 Outils Développeur
- **API TradingView** — Accès direct aux données de marché
- **Intégration MCP** — Architecture modulaire et extensible
- **Logs structurés** — Suivi complet des analyses
- **Export flexible** — JSON, CSV, rapports formatés

---

## 🏗 Architecture

```
Markov Trading
├── 📂 analyze/           # Analyses techniques et fondamentales
├── 📂 fetch/             # Fetchers de données (TradingView, web)
├── 📂 screens/           # Screeners de marché
├── 📂 utils/             # Utilitaires communs
├── 📂 config/            # Configuration et credentials
├── 📂 docs/              # Documentation
└── 📄 main.py            # Point d'entrée
```

---

## 🚀 Installation

```bash
# Cloner le repository
git clone https://github.com/TMSSS05/Markov-Trading.git
cd Markov-Trading

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt

# Configurer les credentials
cp config/config.example.json config/config.json
# Éditer config.json avec vos clés API
```

---

## ⚙️ Configuration

### Variables d'environnement

```bash
# TradingView MCP (optionnel)
export TRADINGVIEW_API_KEY="votre_cle_api"

# OpenCode API (pour intégration agent)
export OPENCODE_API_KEY="votre_cle_opencode"
```

### Structure config.json

```json
{
  "tradingview": {
    "enabled": true,
    "mcp_server": "tradingview-mcp"
  },
  "news_api": {
    "enabled": true,
    "api_key": "votre_cle"
  },
  "logging": {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  }
}
```

---

## 📖 Utilisation

### Analyse d'un actif

```python
from fetch.tradingview import get_market_signals
from analyze.fundamental import analyze_company

# Signaux techniques + sentiment
signals = get_market_signals("AAPL")
print(signals)

# Analyse fondamentale
analysis = analyze_company("AAPL")
print(analysis)
```

### Screener personnalisé

```python
from screens.technical import screen_stocks

# Actions avec RSI en zone de survente
results = screen_stocks(
    filters=[{"field": "RSI", "operator": "less", "value": 30}],
    markets=["america"],
    limit=20
)
```

### Analyse macro

```python
from analyze.macro import get_market_regime

# Analyse du régime de marché
regime = get_market_regime()
print(f"Régime actuel: {regime['current']}")
```

---

## 🎯 Cas d'usage

| Use Case | Commande/API | Output |
|----------|--------------|--------|
| **Screen talents** | `screen_stocks(filters=[...])` | Liste d'actions filtrées |
| **Signal d'achat** | `get_market_signals(ticker)` | RSI, MACD, SMA, sentiment |
| **Valorisation** | `calculate_dcf(ticker)` | Fair value, marge de sécurité |
| **Comparables** | `get_comparables(ticker)` | Tableau comparatif pairs |
| **Actualités** | `get_news_sentiment(ticker)` | Score sentiment, tendances |

---

## 🔌 API Reference

### Modules principaux

| Module | Description | Méthodes clés |
|--------|-------------|---------------|
| `fetch/tradingview.py` | Données TradingView | `get_market_signals()`, `screen_stocks()` |
| `fetch/web.py` | Scraping web | `fetch_news()`, `get_article()` |
| `analyze/fundamental.py` | Analyse fondamentale | `analyze_company()`, `calculate_dcf()` |
| `analyze/macro.py` | Analyse macro | `get_market_regime()`, `get_indexes()` |
| `screens/technical.py` | Screeners | `screen_stocks()`, `screen_crypto()` |

---

## 📊 Stack Technique

<div align="center">

| Categorie | Stack |
|-----------|-------|
| **Language** | Python 3.11+ |
| **Data** | Pandas, NumPy |
| **API** | TradingView MCP, REST APIs |
| **HTTP** | aiohttp, httpx |
| **Parsing** | BeautifulSoup, Playwright |
| **Logs** | Python logging |
| **Config** | JSON, dotenv |

</div>

---

## 🤝 Contribution

Les contributions sont les bienvenues ! 

1. **Fork** le projet
2. Créer une branche (`git checkout -b feature/amazing-feature`)
3. **Commit** (`git commit -m 'Add amazing feature'`)
4. **Push** (`git push origin feature/amazing-feature`)
5. Ouvrir une **Pull Request**

---

## 📝 Licence

Ce projet est sous licence MIT — voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👤 Auteur

**Thomas Cogné** — [GitHub](https://github.com/TMSSS05)

---

<div align="center">

⭐ N'hésitez pas à star le projet si vous l'appréciez !

</div>
