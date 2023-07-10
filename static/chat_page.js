document.addEventListener('DOMContentLoaded', () => {

    // Make sidebar collapse on click
    document.querySelector('#show-sidebar-button').onclick = () => {
        document.querySelector('#sidebar').classList.toggle('view-sidebar');
    };

    // Make 'enter' key submit message
    let msg = document.getElementById("user_message");
    msg.addEventListener("keyup", function (event) {
        event.preventDefault();
        if (event.keyCode === 13) {
            document.getElementById("send_message").click();
        }
    });

    // chat history
    var history = document.getElementById("chat_history");
    history.addEventListener('click', () => {


        
        //     // var dhist = data_history
        //     // const dhist = document.querySelector('#get-history').innerHTML;
        //     const username = document.querySelector('#get-username').innerHTML;
        //     const sender = document.querySelector('#get-sender').innerHTML;
        //     const message = document.querySelector('#get-message').innerHTML;
        //     const room = document.querySelector('#get-room').innerHTML;

        //     if (message) {
        //         console.log(message)
        //         const p = document.createElement('p');
        //         const span_username = document.createElement('span');
        //         // const span_timestamp = document.createElement('span');
        //         const br = document.createElement('br')
        //         // Display user's own message
        //         if (sender == username) {
        //                 p.setAttribute("class", "my-msg");

        //                 // Username
        //                 span_username.setAttribute("class", "my-username");
        //                 span_username.innerText = sender;

        //                 // Timestamp
        //                 // span_timestamp.setAttribute("class", "timestamp");
        //                 // span_timestamp.innerText = data.time_stamp;

        //                 // HTML to append
        //                 p.innerHTML += span_username.outerHTML + br.outerHTML + message + br.outerHTML  //+ span_timestamp.outerHTML

        //                 //Append
        //                 document.querySelector('#display-message-section').append(p);
        //         }
        //         // Display other users' messages
        //         else if (typeof sender !== 'undefined') {
        //             p.setAttribute("class", "others-msg");

        //             // Username
        //             span_username.setAttribute("class", "other-username");
        //             span_username.innerText = sender;

        //             // Timestamp
        //             // span_timestamp.setAttribute("class", "timestamp");
        //             // span_timestamp.innerText = data.time_stamp;

        //             // HTML to append
        //             p.innerHTML += span_username.outerHTML + br.outerHTML + message + br.outerHTML //+ span_timestamp.outerHTML;

        //             //Append
        //             document.querySelector('#display-message-section').append(p);
        //         }
        //         // Display system message
        //         else {
        //             printSysMsg(message);
        //         }


        //     }
        //     scrollDownChatWindow();
        // })
    });
});

    function scrollDownChatWindow() {
        const chatWindow = document.querySelector("#display-message-section");
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }