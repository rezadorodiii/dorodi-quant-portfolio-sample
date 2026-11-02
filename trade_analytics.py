def get_closed_trades(trade_history):
    """
    Return only completed SELL trades.
    """

    if not trade_history:
        return []

    return [
        trade
        for trade in trade_history
        if trade.get("type") == "SELL"
    ]


def count_trades(trade_history):
    """
    Count completed trades.
    """

    return len(
        get_closed_trades(trade_history)
    )


def count_winning_trades(trade_history):
    """
    Count completed trades with positive profit/loss.
    """

    trades = get_closed_trades(trade_history)

    return sum(
        1
        for trade in trades
        if trade.get("profit_loss", 0) > 0
    )


def count_losing_trades(trade_history):
    """
    Count completed trades with negative profit/loss.
    """

    trades = get_closed_trades(trade_history)

    return sum(
        1
        for trade in trades
        if trade.get("profit_loss", 0) < 0
    )


def calculate_trade_win_rate(trade_history):
    """
    Calculate win rate of completed trades.

    Returns percentage.
    """

    total_trades = count_trades(
        trade_history
    )

    if total_trades <= 0:
        return 0

    winning_trades = count_winning_trades(
        trade_history
    )

    return (
        winning_trades
        / total_trades
    ) * 100


def count_signal_exits(trade_history):
    """
    Count completed trades exited by signal.
    """

    trades = get_closed_trades(trade_history)

    return sum(
        1
        for trade in trades
        if trade.get("exit_reason") == "SIGNAL"
    )


def count_stop_loss_exits(trade_history):
    """
    Count completed trades exited by stop loss.
    """

    trades = get_closed_trades(trade_history)

    return sum(
        1
        for trade in trades
        if trade.get("exit_reason") == "STOP_LOSS"
    )


def count_end_of_data_exits(trade_history):
    """
    Count completed trades exited at the end of the data.
    """

    trades = get_closed_trades(trade_history)

    return sum(
        1
        for trade in trades
        if trade.get("exit_reason") == "END_OF_DATA"
    )


def calculate_exit_reason_distribution(trade_history):
    """
    Return the number of completed trades for each exit reason.
    """

    return {
        "SIGNAL": count_signal_exits(trade_history),
        "STOP_LOSS": count_stop_loss_exits(trade_history),
        "END_OF_DATA": count_end_of_data_exits(trade_history),
    }
