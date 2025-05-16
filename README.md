# kucoinfutures-python
Python SDK (sync and async) for Kucoinfutures cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/kucoinfutures)
- You can check Kucoinfutures's docs here: [Docs](https://www.google.com/search?q=google+kucoinfutures+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/kucoinfutures-python
- Pypi package: https://pypi.org/project/kucoin-futures-api


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

main()
```

### Async

```Python
import sys
import asyncio
from kucoinfutures import KucoinfuturesAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = KucoinfuturesAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from kucoinfutures import KucoinfuturesWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = KucoinfuturesWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_contract_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `fetch_balance(self, params={})`
- `fetch_bids_asks(self, symbols: Strings = None, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_interval(self, symbol: str, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_leverage(self, symbol: str, params={})`
- `fetch_margin_mode(self, symbol: str, params={})`
- `fetch_mark_price(self, symbol: str, params={})`
- `fetch_market_leverage_tiers(self, symbol: str, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order(self, id: Str, symbol: Str = None, params={})`
- `fetch_orders_by_status(self, status, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions_history(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_status(self, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `add_margin(self, symbol: str, amount: float, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids, symbol: Str = None, params={})`
- `close_position(self, symbol: str, side: OrderSide = None, params={})`
- `describe(self)`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `set_margin_mode(self, marginMode: str, symbol: Str = None, params={})`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`

### REST Raw

- `public_get_currencies(request)`
- `public_get_currencies_currency(request)`
- `public_get_symbols(request)`
- `public_get_market_orderbook_level1(request)`
- `public_get_market_alltickers(request)`
- `public_get_market_stats(request)`
- `public_get_markets(request)`
- `public_get_market_orderbook_level_level_limit(request)`
- `public_get_market_orderbook_level2_20(request)`
- `public_get_market_orderbook_level2_100(request)`
- `public_get_market_histories(request)`
- `public_get_market_candles(request)`
- `public_get_prices(request)`
- `public_get_timestamp(request)`
- `public_get_status(request)`
- `public_get_mark_price_symbol_current(request)`
- `public_get_mark_price_all_symbols(request)`
- `public_get_margin_config(request)`
- `public_get_announcements(request)`
- `public_post_bullet_public(request)`
- `private_get_user_info(request)`
- `private_get_accounts(request)`
- `private_get_accounts_accountid(request)`
- `private_get_accounts_ledgers(request)`
- `private_get_hf_accounts_ledgers(request)`
- `private_get_hf_margin_account_ledgers(request)`
- `private_get_transaction_history(request)`
- `private_get_sub_user(request)`
- `private_get_sub_accounts_subuserid(request)`
- `private_get_sub_accounts(request)`
- `private_get_sub_api_key(request)`
- `private_get_margin_account(request)`
- `private_get_margin_accounts(request)`
- `private_get_isolated_accounts(request)`
- `private_get_deposit_addresses(request)`
- `private_get_deposits(request)`
- `private_get_hist_deposits(request)`
- `private_get_withdrawals(request)`
- `private_get_hist_withdrawals(request)`
- `private_get_withdrawals_quotas(request)`
- `private_get_accounts_transferable(request)`
- `private_get_transfer_list(request)`
- `private_get_base_fee(request)`
- `private_get_trade_fees(request)`
- `private_get_market_orderbook_level_level(request)`
- `private_get_market_orderbook_level2(request)`
- `private_get_market_orderbook_level3(request)`
- `private_get_hf_accounts_opened(request)`
- `private_get_hf_orders_active(request)`
- `private_get_hf_orders_active_symbols(request)`
- `private_get_hf_margin_order_active_symbols(request)`
- `private_get_hf_orders_done(request)`
- `private_get_hf_orders_orderid(request)`
- `private_get_hf_orders_client_order_clientoid(request)`
- `private_get_hf_orders_dead_cancel_all_query(request)`
- `private_get_hf_fills(request)`
- `private_get_orders(request)`
- `private_get_limit_orders(request)`
- `private_get_orders_orderid(request)`
- `private_get_order_client_order_clientoid(request)`
- `private_get_fills(request)`
- `private_get_limit_fills(request)`
- `private_get_stop_order(request)`
- `private_get_stop_order_orderid(request)`
- `private_get_stop_order_queryorderbyclientoid(request)`
- `private_get_oco_order_orderid(request)`
- `private_get_oco_order_details_orderid(request)`
- `private_get_oco_client_order_clientoid(request)`
- `private_get_oco_orders(request)`
- `private_get_hf_margin_orders_active(request)`
- `private_get_hf_margin_orders_done(request)`
- `private_get_hf_margin_orders_orderid(request)`
- `private_get_hf_margin_orders_client_order_clientoid(request)`
- `private_get_hf_margin_fills(request)`
- `private_get_etf_info(request)`
- `private_get_margin_currencies(request)`
- `private_get_risk_limit_strategy(request)`
- `private_get_isolated_symbols(request)`
- `private_get_margin_symbols(request)`
- `private_get_isolated_account_symbol(request)`
- `private_get_margin_borrow(request)`
- `private_get_margin_repay(request)`
- `private_get_margin_interest(request)`
- `private_get_project_list(request)`
- `private_get_project_marketinterestrate(request)`
- `private_get_redeem_orders(request)`
- `private_get_purchase_orders(request)`
- `private_get_broker_api_rebase_download(request)`
- `private_get_migrate_user_account_status(request)`
- `private_get_affiliate_inviter_statistics(request)`
- `private_post_sub_user_created(request)`
- `private_post_sub_api_key(request)`
- `private_post_sub_api_key_update(request)`
- `private_post_deposit_addresses(request)`
- `private_post_withdrawals(request)`
- `private_post_accounts_universal_transfer(request)`
- `private_post_accounts_sub_transfer(request)`
- `private_post_accounts_inner_transfer(request)`
- `private_post_transfer_out(request)`
- `private_post_transfer_in(request)`
- `private_post_hf_orders(request)`
- `private_post_hf_orders_test(request)`
- `private_post_hf_orders_sync(request)`
- `private_post_hf_orders_multi(request)`
- `private_post_hf_orders_multi_sync(request)`
- `private_post_hf_orders_alter(request)`
- `private_post_hf_orders_dead_cancel_all(request)`
- `private_post_orders(request)`
- `private_post_orders_test(request)`
- `private_post_orders_multi(request)`
- `private_post_stop_order(request)`
- `private_post_oco_order(request)`
- `private_post_hf_margin_order(request)`
- `private_post_hf_margin_order_test(request)`
- `private_post_margin_order(request)`
- `private_post_margin_order_test(request)`
- `private_post_margin_borrow(request)`
- `private_post_margin_repay(request)`
- `private_post_purchase(request)`
- `private_post_redeem(request)`
- `private_post_lend_purchase_update(request)`
- `private_post_bullet_private(request)`
- `private_post_position_update_user_leverage(request)`
- `private_post_deposit_address_create(request)`
- `private_delete_sub_api_key(request)`
- `private_delete_withdrawals_withdrawalid(request)`
- `private_delete_hf_orders_orderid(request)`
- `private_delete_hf_orders_sync_orderid(request)`
- `private_delete_hf_orders_client_order_clientoid(request)`
- `private_delete_hf_orders_sync_client_order_clientoid(request)`
- `private_delete_hf_orders_cancel_orderid(request)`
- `private_delete_hf_orders(request)`
- `private_delete_hf_orders_cancelall(request)`
- `private_delete_orders_orderid(request)`
- `private_delete_order_client_order_clientoid(request)`
- `private_delete_orders(request)`
- `private_delete_stop_order_orderid(request)`
- `private_delete_stop_order_cancelorderbyclientoid(request)`
- `private_delete_stop_order_cancel(request)`
- `private_delete_oco_order_orderid(request)`
- `private_delete_oco_client_order_clientoid(request)`
- `private_delete_oco_orders(request)`
- `private_delete_hf_margin_orders_orderid(request)`
- `private_delete_hf_margin_orders_client_order_clientoid(request)`
- `private_delete_hf_margin_orders(request)`
- `futurespublic_get_contracts_active(request)`
- `futurespublic_get_contracts_symbol(request)`
- `futurespublic_get_ticker(request)`
- `futurespublic_get_level2_snapshot(request)`
- `futurespublic_get_level2_depth20(request)`
- `futurespublic_get_level2_depth100(request)`
- `futurespublic_get_trade_history(request)`
- `futurespublic_get_kline_query(request)`
- `futurespublic_get_interest_query(request)`
- `futurespublic_get_index_query(request)`
- `futurespublic_get_mark_price_symbol_current(request)`
- `futurespublic_get_premium_query(request)`
- `futurespublic_get_trade_statistics(request)`
- `futurespublic_get_funding_rate_symbol_current(request)`
- `futurespublic_get_contract_funding_rates(request)`
- `futurespublic_get_timestamp(request)`
- `futurespublic_get_status(request)`
- `futurespublic_get_level2_message_query(request)`
- `futurespublic_get_contracts_risk_limit_symbol(request)`
- `futurespublic_get_alltickers(request)`
- `futurespublic_get_level2_depth_limit(request)`
- `futurespublic_get_level3_message_query(request)`
- `futurespublic_get_level3_snapshot(request)`
- `futurespublic_post_bullet_public(request)`
- `futuresprivate_get_transaction_history(request)`
- `futuresprivate_get_account_overview(request)`
- `futuresprivate_get_account_overview_all(request)`
- `futuresprivate_get_transfer_list(request)`
- `futuresprivate_get_orders(request)`
- `futuresprivate_get_stoporders(request)`
- `futuresprivate_get_recentdoneorders(request)`
- `futuresprivate_get_orders_orderid(request)`
- `futuresprivate_get_orders_byclientoid(request)`
- `futuresprivate_get_fills(request)`
- `futuresprivate_get_recentfills(request)`
- `futuresprivate_get_openorderstatistics(request)`
- `futuresprivate_get_position(request)`
- `futuresprivate_get_positions(request)`
- `futuresprivate_get_margin_maxwithdrawmargin(request)`
- `futuresprivate_get_contracts_risk_limit_symbol(request)`
- `futuresprivate_get_funding_history(request)`
- `futuresprivate_get_deposit_address(request)`
- `futuresprivate_get_deposit_list(request)`
- `futuresprivate_get_withdrawals_quotas(request)`
- `futuresprivate_get_withdrawal_list(request)`
- `futuresprivate_get_sub_api_key(request)`
- `futuresprivate_get_trade_statistics(request)`
- `futuresprivate_get_trade_fees(request)`
- `futuresprivate_get_history_positions(request)`
- `futuresprivate_get_getmaxopensize(request)`
- `futuresprivate_get_getcrossuserleverage(request)`
- `futuresprivate_get_position_getmarginmode(request)`
- `futuresprivate_post_transfer_out(request)`
- `futuresprivate_post_transfer_in(request)`
- `futuresprivate_post_orders(request)`
- `futuresprivate_post_orders_test(request)`
- `futuresprivate_post_orders_multi(request)`
- `futuresprivate_post_position_margin_auto_deposit_status(request)`
- `futuresprivate_post_margin_withdrawmargin(request)`
- `futuresprivate_post_position_margin_deposit_margin(request)`
- `futuresprivate_post_position_risk_limit_level_change(request)`
- `futuresprivate_post_bullet_private(request)`
- `futuresprivate_post_withdrawals(request)`
- `futuresprivate_post_st_orders(request)`
- `futuresprivate_post_sub_api_key(request)`
- `futuresprivate_post_sub_api_key_update(request)`
- `futuresprivate_post_changecrossuserleverage(request)`
- `futuresprivate_post_position_changemarginmode(request)`
- `futuresprivate_delete_orders_orderid(request)`
- `futuresprivate_delete_orders_client_order_clientoid(request)`
- `futuresprivate_delete_orders(request)`
- `futuresprivate_delete_stoporders(request)`
- `futuresprivate_delete_withdrawals_withdrawalid(request)`
- `futuresprivate_delete_cancel_transfer_out(request)`
- `futuresprivate_delete_sub_api_key(request)`
- `futuresprivate_delete_orders_multi_cancel(request)`
- `webexchange_get_currency_currency_chain_info(request)`
- `webexchange_get_contract_symbol_funding_rates(request)`
- `broker_get_broker_nd_info(request)`
- `broker_get_broker_nd_account(request)`
- `broker_get_broker_nd_account_apikey(request)`
- `broker_get_broker_nd_rebase_download(request)`
- `broker_get_asset_ndbroker_deposit_list(request)`
- `broker_get_broker_nd_transfer_detail(request)`
- `broker_get_broker_nd_deposit_detail(request)`
- `broker_get_broker_nd_withdraw_detail(request)`
- `broker_post_broker_nd_transfer(request)`
- `broker_post_broker_nd_account(request)`
- `broker_post_broker_nd_account_apikey(request)`
- `broker_post_broker_nd_account_update_apikey(request)`
- `broker_delete_broker_nd_account_apikey(request)`
- `earn_get_otc_loan_loan(request)`
- `earn_get_otc_loan_accounts(request)`
- `earn_get_earn_redeem_preview(request)`
- `earn_get_earn_saving_products(request)`
- `earn_get_earn_hold_assets(request)`
- `earn_get_earn_promotion_products(request)`
- `earn_get_earn_kcs_staking_products(request)`
- `earn_get_earn_staking_products(request)`
- `earn_get_earn_eth_staking_products(request)`
- `earn_post_earn_orders(request)`
- `earn_delete_earn_orders(request)`

### WS Unified

- `describe(self)`
- `negotiate(self, privateChannel, params={})`
- `negotiate_helper(self, privateChannel, params={})`
- `subscribe(self, url, messageHash, subscriptionHash, subscription, params={})`
- `subscribe_multiple(self, url, messageHashes, topic, subscriptionHashes, subscriptionArgs, params={})`
- `un_subscribe_multiple(self, url, messageHashes, topic, subscriptionHashes, params={}, subscription: dict = None)`
- `watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_bids_asks(self, symbols: Strings = None, params={})`
- `watch_multi_request(self, methodName, channelName: str, symbols: Strings = None, params={})`
- `watch_position(self, symbol: Str = None, params={})`
- `get_current_position(self, symbol)`
- `set_position_cache(self, client: Client, symbol: str)`
- `load_position_snapshot(self, client, messageHash, symbol)`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_trades_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `un_watch_trades(self, symbol: str, params={})`
- `un_watch_trades_for_symbols(self, symbols: List[str], params={})`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `watch_order_book_for_symbols(self, symbols: List[str], limit: Int = None, params={})`
- `un_watch_order_book(self, symbol: str, params={})`
- `un_watch_order_book_for_symbols(self, symbols: List[str], params={})`
- `get_cache_index(self, orderbook, cache)`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_balance(self, params={})`
- `fetch_balance_snapshot(self, client, message)`
- `get_message_hash(self, elementName: str, symbol: Str = None)`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.