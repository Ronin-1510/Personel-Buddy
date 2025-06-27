// File: src/App.js
import React, { useState } from 'react';

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [chunks, setChunks] = useState([]);
  const [loading, setLoading] = useState(false);

  const askBuddy = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
      });

      const data = await response.json();
      setAnswer(data.answer);
      setChunks(data.chunks);
    } catch (error) {
      setAnswer("❌ Error contacting backend.");
      setChunks([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h2>🧠 Buddy – Internal AI Assistant</h2>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask Buddy something..."
        style={{ width: '80%', padding: '0.5rem', fontSize: '1rem' }}
      />
      <button onClick={askBuddy} style={{ marginLeft: '1rem', padding: '0.5rem 1rem' }}>Ask</button>

      {loading && <p>⏳ Waiting for Buddy to reply...</p>}

      {answer && (
        <div style={{ marginTop: '2rem' }}>
          <h3>🤖 Buddy says:</h3>
          <p>{answer}</p>
        </div>
      )}

      {chunks.length > 0 && (
        <div style={{ marginTop: '2rem' }}>
          <h4>📄 Top Matching Chunks:</h4>
          {chunks.map((chunk, idx) => (
            <div key={idx} style={{ marginBottom: '1rem' }}>
              <strong>From: {chunk[1]}</strong>
              <p>{chunk[0].slice(0, 300)}...</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
