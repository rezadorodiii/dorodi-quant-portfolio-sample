"""Offline demonstration using invented records, not real trading data."""
import json
from trade_analytics import (
    count_trades, count_winning_trades, count_losing_trades,
    calculate_trade_win_rate, calculate_exit_reason_distribution,
)

records = [
    {"type": "BUY"},
    {"type": "SELL", "profit_loss": 12, "exit_reason": "SIGNAL"},
    {"type": "SELL", "profit_loss": -5, "exit_reason": "STOP_LOSS"},
    {"type": "SELL", "profit_loss": 0, "exit_reason": "END_OF_DATA"},
]
summary = {
    "completed_trades": count_trades(records),
    "winning_trades": count_winning_trades(records),
    "losing_trades": count_losing_trades(records),
    "win_rate_percent": round(calculate_trade_win_rate(records), 2),
    "exit_reasons": calculate_exit_reason_distribution(records),
}
assert summary["completed_trades"] == 3
assert summary["winning_trades"] == 1
assert summary["losing_trades"] == 1
assert calculate_trade_win_rate([]) == 0
assert sum(summary["exit_reasons"].values()) == 3
print(json.dumps(summary, indent=2))
