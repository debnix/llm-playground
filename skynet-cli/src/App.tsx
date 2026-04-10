import './App.css'
import { HeaderCLI } from './HeaderCLI';
import Terminal, { ColorMode, TerminalOutput } from 'react-terminal-ui';
import { useState } from 'react';

const API_URL = 'http://localhost:8000/entity';

function App() {
  const [prompt, setPrompt] = useState('$');
  const [isLoading, setIsLoading] = useState(false);
  const [terminalLineData, setTerminalLineData] = useState([
    <TerminalOutput></TerminalOutput>,
  ]);

  const fetchMessage = async (text: string) => {
    setIsLoading(true);
    try {

      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: text }),
      });
      const data = await response.json();
      setIsLoading(false);
      return data;

    } catch (error) {
      console.error('Error fetching message:', error);
      setIsLoading(false);
      return 'Error fetching message';
    }
  };

  const defaultHandler = async(command: string) => {
    if(isLoading){
      return;
    }
    setTerminalLineData((prevState) => {
      return [
        ...prevState,
        <TerminalOutput> 
          {<span className='prompt-custom'>$</span>} {command} {<br/>}
        </TerminalOutput>
      ]
    });

    setPrompt(() => '...');

    const response = await fetchMessage(command);

    setTerminalLineData((prevState) => {
      return [
        ...prevState,
        <TerminalOutput> 
          <div className='container-response-message'>
            <p className='response-message'>
            <span className='prompt-custom'>{'>> '}</span>
              {response}
            </p>
          </div>
        </TerminalOutput>
      ]
    });

    setPrompt(() => '$');
  };

  return (
    <div className='app-container'>

      <div className='title-container'>
        <h2 className='title'>Terminator AI</h2>
      </div>

      <div className='terminal-container'> 
      <Terminal
        name="Skynet"
        colorMode={ColorMode.Dark}
        onInput={defaultHandler}
        prompt={prompt}
      >
        <>
          <HeaderCLI />
          {terminalLineData}
        </>
      </Terminal>
      </div>
    </div>
  );
}

export default App
