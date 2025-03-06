document.addEventListener("DOMContentLoaded", function () {
    const inputBox = document.getElementById("user-input");
    const chatLog = document.getElementById("chat-log");

    inputBox.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            let userMessage = inputBox.value;
            inputBox.value = "";

            // Display user message
            chatLog.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;

            // Send request to Flask backend
            fetch("http://127.0.0.1:5000/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                chatLog.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;
                chatLog.scrollTop = chatLog.scrollHeight;  // Auto-scroll to latest message
            })
            .catch(error => console.error("Error:", error));
        }
    });
});
