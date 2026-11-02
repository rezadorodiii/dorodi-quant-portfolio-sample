DORODI QUANT - OFFLINE PYTHON ANALYTICS SAMPLE

A small extract from a personal Python research project, packaged with AI assistance for portfolio review.

WHAT IT DEMONSTRATES
Functions, lists, dictionaries, filtering, counting and a simple percentage calculation. The demo summarises invented completed-trade records. It needs only the Python standard library.

RUN
python demo.py

EXPECTED RESULT
3 completed trades; 1 winner; 1 loser; 33.33% win rate.
Exit counts: SIGNAL 1, STOP_LOSS 1, END_OF_DATA 1.
The break-even trade counts as completed but as neither a winner nor a loser.

FILES
trade_analytics.py: unchanged extract from strategies/trade_analytics.py.
demo.py: newly prepared demonstration using synthetic data.
README.txt: explanation prepared for this sample.

LIMITATIONS
This historical helper counts only SELL records as completed trades. It does not model short-position exits. Empty input returns a win rate of 0, so callers must also inspect the trade count to distinguish no observations from a zero-percent observed rate. Other or missing exit reasons are not included in the three exit-reason buckets. Inputs are assumed to be correctly formed dictionaries with numeric profit_loss values.

This is an offline code sample, not the complete research system or evidence of financial performance. It contains no real account data, network integration or order execution. No professional engineering or machine-learning experience is claimed.
