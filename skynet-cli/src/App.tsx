import './App.css'
import { ReactTerminal } from "react-terminal";
import { HeaderCLI } from './HeaderCLI';
import Terminal, { ColorMode, TerminalOutput } from 'react-terminal-ui';
import { useState } from 'react';

const API_URL = 'http://localhost:8000/entity';

function App() {
  const [terminalLineData, setTerminalLineData] = useState([
    <TerminalOutput>Welcome to the React Terminal UI Demo!</TerminalOutput>,
  ]);

  const fetchMessage = async (text: string) => {
    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: text }),
      });
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching message:', error);
      return 'Error fetching message';
    }
  };

  const defaultHandler = async(command: string) => {
    const response = await fetchMessage(command);
    setTerminalLineData([...terminalLineData, <TerminalOutput> {'>>>'}{response}</TerminalOutput>]);
  };

  return (
    <div className='app-container'>

      <div className='title-container'>
        <h2 className='title'>Terminator AI</h2>
      </div>

      <div className='terminal-container'> 
      <Terminal
        name="React Terminal Usage Example"
        colorMode={ColorMode.Light}
        onInput={defaultHandler}
      >
        {terminalLineData}
      </Terminal>
      </div>
    </div>
  );
}

export default App
