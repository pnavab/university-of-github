import { useState } from 'react';
import './App.css';

async function flipCoin() {
  try {
    const response = await fetch('http://localhost:8000/flip-coin');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error; // Rethrow the error for the caller to handle
  }
}

function App() {
  const [result, setResult] = useState("Click below!");

  async function handleFlipCoin() {
    const head_tail = await flipCoin();
    console.log("Result of our api call: ", head_tail);
    setResult(head_tail.value);
  }
  return (
    <div className="App">
      {result && (
      <p>{result}</p>
      )}
      <button onClick={handleFlipCoin}>Flip a Coin</button>
    </div>
  );
}

export default App;
