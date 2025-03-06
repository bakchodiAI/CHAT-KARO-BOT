document.addEventListener("DOMContentLoaded", function () {
    const inputBox = document.getElementById("user-input");
    const sendButton = document.getElementById("send-btn");
    const chatLog = document.getElementById("chat-log");

    function sendMessage() {
        let userMessage = inputBox.value.trim();
        if (userMessage === "") return;

        inputBox.value = "";

        // User ka message display karein
        chatLog.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;

        // Backend ko request bhejein (localhost hata diya)
        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            if (data.reply) {
                chatLog.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;
            } else {
                chatLog.innerHTML += `<p><strong>Bot:</strong> Error: ${data.error}</p>`;
            }
            chatLog.scrollTop = chatLog.scrollHeight;  // Auto-scroll to latest message
        })
        .catch(error => {
            console.error("Error:", error);
            chatLog.innerHTML += `<p><strong>Bot:</strong> Failed to fetch response.</p>`;
        });
    }

    sendButton.addEventListener("click", sendMessage);
    inputBox.addEventListener("keypress", function (event) {
        if (event.key === "Enter") sendMessage();
    });
});

