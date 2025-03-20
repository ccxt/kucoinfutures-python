# kucoinfutures-python
Python SDK (sync and async) for Kucoinfutures with Rest and WS capabilities.

You can check Kucoinfutures's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/kucoinfutures)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install kucoin-futures-api
```

## Usage

### Async

```Python
from kucoin_futures_api import KucoinfuturesAsync

async def main():
    instance = KucoinfuturesAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from kucoin_futures_api import KucoinfuturesSync

def main():
    instance = KucoinfuturesSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from kucoin_futures_api import KucoinfuturesWs

async def main():
    instance = KucoinfuturesWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

