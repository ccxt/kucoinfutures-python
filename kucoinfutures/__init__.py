import sys
import kucoinfutures.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from kucoinfutures.ccxt import kucoinfutures as KucoinfuturesSync
from kucoinfutures.ccxt.async_support.kucoinfutures import kucoinfutures as KucoinfuturesAsync
from kucoinfutures.ccxt.pro.kucoinfutures import kucoinfutures as KucoinfuturesWs
