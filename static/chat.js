document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('chat-form');
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    if (!form) {
        console.error("Form not found!");
        return;
    }

    form.addEventListener('submit', async (event) => {
        // THIS LINE IS THE MOST IMPORTANT:
        event.preventDefault(); 
        
        const text = input.value.trim();
        if (!text) return;

        // Add user bubble
        appendBubble('user', text);
        input.value = '';

        // Add placeholder for AI
        const aiBubble = appendBubble('assistant', '<i>Typing...</i>');

        try {
            const formData = new FormData();
            formData.append('prompt', text);

            const response = await fetch('/ask', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            
            // Render Markdown and Highlight Code
            aiBubble.innerHTML = marked.parse(data.output);
            aiBubble.querySelectorAll('pre code').forEach((el) => {
                hljs.highlightElement(el);
            });

        } catch (err) {
            aiBubble.innerText = "Error: " + err.message;
        } finally {
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    });

    function appendBubble(role, content) {
        const div = document.createElement('div');
        div.className = `message ${role}`;
        const inner = document.createElement('div');
        inner.className = 'bubble';
        inner.innerHTML = content;
        div.appendChild(inner);
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
        return inner;
    }

    // Enter key logic
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            form.requestSubmit(); // Modern way to trigger submit
        }
    });
});