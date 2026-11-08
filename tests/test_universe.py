from scanner.universe import parse_nasdaqlisted

SAMPLE = """Symbol|Security Name|Market Category|Test Issue|Financial Status|Round Lot Size|ETF|NextShares
AAPL|Apple Inc. - Common Stock|Q|N|N|100|N|N
QQQ|Invesco QQQ Trust, Series 1|G|N|N|100|Y|N
ZZZT|Test Issue Corp|Q|Y|N|100|N|N
ABCDW|Some Acquisition Corp - Warrants|S|N|N|100|N|N
BADF|Distressed Inc - Common Stock|Q|N|D|100|N|N
MSFT|Microsoft Corporation - Common Stock|Q|N|N|100|N|N
File Creation Time: 1107202608:01|||||||"""


def test_parse_filters_etf_test_warrants_and_distressed():
    df = parse_nasdaqlisted(SAMPLE)
    assert df["symbol"].tolist() == ["AAPL", "MSFT"]
