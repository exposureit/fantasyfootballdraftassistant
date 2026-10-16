#!/usr/bin/env python3
"""DraftKings promo math. Fair probability comes from Pinnacle's no-vig number (fetch_dk_lines.py edge table).

  python3 draftkings/promo.py boost --pct 30 --price -110 --fair 0.54 --stake 10
      Profit Boost token: profit is multiplied by (1 + pct/100). Prints EV with and without the token.
  python3 draftkings/promo.py nosweat --price +600 --fair 0.16 --stake 10 [--refund 0.7]
      No Sweat token: a loss is refunded in bonus bets worth about 70 cents on the dollar.
  python3 draftkings/promo.py oddsboost --from -110 --to +120 --fair 0.52 --stake 5
      Daily odds boost: the boosted price replaces the normal one. Plays only if EV is +3 percent or more.
  python3 draftkings/promo.py parlay --legs 0.54,0.52,0.55 --price +600 --stake 10
      Cross-game parlay: joint fair prob (independent legs) vs DK's parlay price.
"""
import sys

def arg(name, default=None, cast=float):
    if name in sys.argv:
        return cast(sys.argv[sys.argv.index(name) + 1])
    if default is None:
        print(f"missing {name}"); sys.exit(2)
    return default
def price_to_profit(price, stake):
    return stake * price / 100 if price > 0 else stake * 100 / -price
def implied(price):
    return 100 / (price + 100) if price > 0 else -price / (-price + 100)
def report(label, fair, stake, profit, loss):
    ev = fair * profit - (1 - fair) * loss
    print(f"{label}: win +${profit:.2f} ({fair*100:.1f}%), lose -${loss:.2f}. EV ${ev:+.2f} per ticket = {ev/stake*100:+.1f}% of stake. Breakeven prob {loss/(profit+loss)*100:.1f}%.")
    return ev

mode = sys.argv[1] if len(sys.argv) > 1 else ""
stake = arg("--stake", 10.0)
if mode == "boost":
    pct, price, fair = arg("--pct"), arg("--price", cast=int), arg("--fair")
    base = price_to_profit(price, stake)
    report("Without token", fair, stake, base, stake)
    report(f"With {pct:g}% Profit Boost", fair, stake, base * (1 + pct / 100), stake)
    print("Rule: put the Profit Boost on the qualifying ticket with the longest price the token allows; boost value scales with profit.")
elif mode == "nosweat":
    price, fair, refund = arg("--price", cast=int), arg("--fair"), arg("--refund", 0.7)
    profit = price_to_profit(price, stake)
    report("Without token", fair, stake, profit, stake)
    report(f"With No Sweat (refund worth {refund:.0%})", fair, stake, profit, stake * (1 - refund))
    print("Rule: put No Sweat on the ticket most likely to lose (the longest parlay); the refund is worth most where the loss probability is highest.")
elif mode == "oddsboost":
    p_from, p_to, fair = arg("--from", cast=int), arg("--to", cast=int), arg("--fair")
    report("Normal price", fair, stake, price_to_profit(p_from, stake), stake)
    ev = report("Boosted price", fair, stake, price_to_profit(p_to, stake), stake)
    print("PLAY (cap $5, game markets only)" if ev / stake >= 0.03 else "PASS: boosted EV is under +3% of stake.")
elif mode == "parlay":
    legs = [float(x) for x in arg("--legs", cast=str).split(",")]
    price = arg("--price", cast=int)
    joint = 1.0
    for l in legs: joint *= l
    print(f"Joint fair prob of {len(legs)} legs: {joint*100:.1f}% (DK implied {implied(price)*100:.1f}%)")
    report("Parlay", joint, stake, price_to_profit(price, stake), stake)
else:
    print(__doc__)
