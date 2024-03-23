## Manually Testing WebSockets
<a href="https://adequatica.medium.com/how-to-manually-test-websocket-apis-855393911d1a">Source</a>

### On a web browser console, do the following

1. Open the WS Connection

```javascript
const ws = new WebSocket('wss://polkadot.webapi.subscan.io/socket');
```

2. Configure WS Logging

```javascript
ws.onmessage = (e) => console.log(`Name: ${e.data}`);
```

3. Send Messages to Server

```javascript
ws.send(JSON.stringify(<object>));
```

4. Close WS Connection

```javascript
ws.close();
```