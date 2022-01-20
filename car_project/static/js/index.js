var connectionString = 'ws://' + window.location.host + '/ws/connect/';
var wsSocket = new WebSocket(connectionString);

function connect() {
    wsSocket.onopen = function open() {
        console.log('WebSockets connection created.');
        wsSocket.send(JSON.stringify({
            "event": "START",
            "message": ""
        }));
    };

    wsSocket.onclose = function (e) {
        // Connecting through WS
        console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
        setTimeout(function () {
            connect();
        }, 1000);
    };
    // Sending the info about the room
    wsSocket.onmessage = function (e) {
        let data = JSON.parse(e.data);
        data = data["payload"];
        let event = data["event"];
        switch (event) {
            case "UPDATE":
                console.log("Reload the map!");
                break;
            default:
                console.log("No event");
        }
    };

    if (wsSocket.readyState == WebSocket.OPEN) {
        wsSocket.onopen();
    }
}

connect();


$(function(){
    $('[data-toggle="tooltip"]').tooltip();
    $(".side-nav .collapse").on("hide.bs.collapse", function() {
        $(this).prev().find(".fa").eq(1).removeClass("fa-angle-right").addClass("fa-angle-down");
    });
    $('.side-nav .collapse').on("show.bs.collapse", function() {
        $(this).prev().find(".fa").eq(1).removeClass("fa-angle-down").addClass("fa-angle-right");
    });
});

let downloaded = false;
let ninterval;

function poll_download(){
    let task_id = localStorage.getItem('task_id');
    let city_id = localStorage.getItem('city_id');
    if(task_id && city_id){
        $.fetch(url, {}).then((resp)=>{
            if(resp.data?.filename){
                downloaded = true;
                clearInterval(ninterval);
            }
        })

    }
}
function start_polling(){
    if(!downloaded){
        ninterval = setInterval(poll_download, 1000)
    }
}

start_polling();