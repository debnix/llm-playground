import './App.css'
import { ReactTerminal } from "react-terminal";

function App() {
 // Define commands here
 const commands = {
  whoami: "debnix",
  cd: (directory) => `changed path to ${directory}`
};

return (
  <div style={{
    width: '100%',
    height: '50vh'
  }}> 
  <ReactTerminal
  showControlBar={false}
    commands={commands}
    theme='matrix'
    style={{
      width: '100%',
      height: '50vh'
    }}
    width='100vw'
    height='90%'
    defaultHandler={(command) => {
      console.log(command);
    }}
  />
  </div>
);
}

export default App
