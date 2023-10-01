const host = window.location.host
var socket = io(host + '?c=' + channel);

// utility functions
const log = { debug: (str) => { console.log(str) } }
const elem = (id) => document.getElementById(id)

const format_python_time = (timestamp) => { 
    options = {
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
    };

    date = new Date(timestamp * 1000)

    return  new Intl.DateTimeFormat("en-US", options).format(date)
}

//socket functions

socket.on('connect', () => {
    //assign ID
    //send chat log up till now
    log.debug('connected!');
});

const create_message_elem = (data) => {
    var newelem = document.createElement('p')
    newelem.className = 'message'

    const timestamp = format_python_time(data.timestamp)

    newelem.innerText = timestamp + ' - ' + data.message

    elem('message_list').append(newelem)
}

const was_scroll_at_end = () => {
    var container = elem("message_container")

    var was_scroll = container.scrollTop + container.clientHeight >= (container.scrollHeight - 100)

    log.debug(container.scrollTop + ' + ' + container.clientHeight + 
    ' >= ' + (container.scrollHeight - 100) + ' => ' + was_scroll)

    return was_scroll
}

const scroll_to_end = () => {
    var container = elem("message_container")
    container.scrollTop = container.scrollHeight
}

socket.on('new_message', (data) => {
    log.debug('received message! ' + JSON.stringify(data));

    const shouldScroll = was_scroll_at_end()

    create_message_elem(data)

    if(shouldScroll) scroll_to_end()
})

socket.on('get_history', (history) => {
    log.debug('received history: ' + JSON.stringify(history));

    elem('message_list').innerText = ''

    history.forEach((data) => {
        create_message_elem(data)
    })

    scroll_to_end()
})

const send_message = () => {
    const message = elem('message_entry')

    if (message.value == '') return

    const data = {
        channel: channel,
        message: message.value
    }

    socket.emit('send_message', data)

    message.value = ''
}

elem('message_entry').onkeypress = (e) => { if (e.key == 'Enter') send_message() }