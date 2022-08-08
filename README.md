# provable-test

This code provides a list of PNT transactions for a specific address inside a time interval.

## Example
Request:
```
curl -X POST -H 'content-type: application/json' -d '{\"address\":\"0xb47ce3a95c5062d9f5894862dcc44df7a660dfba\", \"from\":\"1659880849\", \"to\":\"1659884449\"}' http://localhost:3000/transfers
```

Response:
```
{"txid":"0x042c9a26eeef8b38959498322f5fb0ad4941e0513719e874d51ec883565269c3","sender":"0xea8ddc2f50626f1f8f8c11242d1876710d65ff44","receiver":"0xb47ce3a95c5062d9f5894862dcc44df7a660dfba","amount":"1390358030612096524776"}
{"txid":"0x042c9a26eeef8b38959498322f5fb0ad4941e0513719e874d51ec883565269c3","sender":"0xe30835d2f659fc5100b5a588d0c42199638f7220","receiver":"0xb47ce3a95c5062d9f5894862dcc44df7a660dfba","amount":"2039205316296639102736"}
{"txid":"0xada1a12851ec394bb853c581bf20738e6f692dc264aa400a0a9c52732281ffab","sender":"0xabfd88db78d2503af372cb9c21cdc2f181232b4f","receiver":"0xb47ce3a95c5062d9f5894862dcc44df7a660dfba","amount":"3241000000000000000000"}
{"txid":"0xd79b157002995f3205eb8f003f3a53696cc6b904b535423353d88c350c794ec6","sender":"0xb47ce3a95c5062d9f5894862dcc44df7a660dfba","receiver":"0x35596efadd677a83ca34f2b361a42704dabe7b91","amount":"6673961747703344548856"}
{"txid":"0xd79b157002995f3205eb8f003f3a53696cc6b904b535423353d88c350c794ec6","sender":"0x35596efadd677a83ca34f2b361a42704dabe7b91","receiver":"0xb47ce3a95c5062d9f5894862dcc44df7a660dfba","amount":"33369808738518079512"}
```

## Server start
In order to start the server:

```
python3 main.py
```

This command starts a server listening on port 3000. The cache on the server will retain data for 30 seconds and all the queries to the Ethereum blockchain will be sent to https://aged-wispy-sun.quiknode.pro/a9c866c62d28d63303de21fd44e95f747f725857

## Server configuration
Use following paramaters to configure the server:

- port / p <port number>
- cache-time / ct <time retention>
- node-url / nu <url>

It is possible to change the port, the Ethereum node url or the cache retention time using the previously enumerated parameters.

### Config example
```
python3 main.py p 3002 ct 100 nu 'https://wild-divinemoon.quiknode.pro/9a2fc33e00169e941e01396b0b5a31cf8bc3ab16/'
```
