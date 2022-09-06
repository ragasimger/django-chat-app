var ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/')

ws.onopen = function(){
    console.log("WebSocket connection established")
    ws.send(JSON.stringify({
        'message' : "Hello from Client"
    }))
}
ws.onmessage = function(event){
    console.log("Message from server", event)
}

ws.onerror = function(event){
    console.log(event)
}

ws.onclose = function(event){
    console.log(event)
}

ws.send("Messages")