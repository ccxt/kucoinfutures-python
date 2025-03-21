# kucoinfutures-python
Python SDK (sync and async) for Kucoinfutures cryptocurrency exchange with Rest and WS capabilities.

You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/kucoinfutures)
You can check Kucoinfutures's docs here: [Docs](https://ccxt.com)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install kucoin-futures-api
```

## Usage

### Sync

```Python
from kucoinfutures import KucoinfuturesSync

def main():
    instance = KucoinfuturesSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)
```

### Async

```Python
import asyncio
from kucoinfutures import KucoinfuturesAsync

async def main():
    instance = KucoinfuturesAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

asyncio.run(main())
```

### Websockets

```Python
from kucoinfutures import KucoinfuturesWs

async def main():
    instance = KucoinfuturesWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")
```

