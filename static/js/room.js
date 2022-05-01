function scrollToBottom() {
    let objDiv = document.getElementById("chat-messages");
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();

const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    console.log('onmessage');

    const data = JSON.parse(e.data);
    if (data.message) {
        if (data.username == userName) {
            document.querySelector('#chat-messages').innerHTML += (
                '<article class="message is-primary has-text-right" style="width:70%;margin-left:28%"><div class="message-header"><div class="is-size-4" style="display:flex;margin-left:auto;"><strong>' + data.username + '</strong>&nbsp;&nbsp;<div style="background-image: url(\'' + data.image + '\');width: 50px;height: 50px;background-position: center center;background-repeat: no-repeat;border-radius:50%"></div></div></div><div class="message-body"><div class="is-size-5">' + data.message + '</div><div class="is-size-7 is-italic" style="color:rgb(125, 188, 179)">' + data.time + '</div></div></article>'
            )
        } else {
            document.querySelector('#chat-messages').innerHTML += (
                '<article class="message" style="width:70%;"><div class="message-header"><div class="is-size-4" style="display:flex;"><div style="background-image: url(\'' + data.image + '\');width: 50px;height: 50px;background-position: center center;background-repeat: no-repeat;border-radius:50%"></div>&nbsp;&nbsp;<strong>' + data.username + '</strong></div></div><div class="message-body"><div class="is-size-5">' + data.message + '</div><div class="is-size-7 is-italic" style="color:rgb(73, 73, 73)">' + data.time + '</div></div></article>'
            );
        }
    } else {
        alert('The message is empty!');
    }

    scrollToBottom();
};

chatSocket.onclose = function(e) {
    console.log('The socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName
    }));

    messageInputDom.value = '';
};

document.querySelector('#home').onclick = function(e) {
    window.location.replace('/');
};