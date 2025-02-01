import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>

      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App

/*

This app runs by "npm run dev" installed by Vite.  

The page has several components. From the top to the bottom, there are two components which are two svg images. svg is for Scalable Vector Graphcs defined by XML language. It wouldn't lose the quality. SVG itself can be interactive using CSS or Javascript.  

In the App, the interaction and animiation is achieved by CSS. In the CSS, using the followed code to define the animation. 

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.react:hover {
  filter: drop-shadow(0 0 2em #61dafbaa);
}

For the counter, the app uses the code below:

const [count, setCount] = useState(0);
useState() is one state hook, which is one function used in React.js to manage about the value of state. The value can be saved in the variable returned from this function. 

=> is the representation of function. Therefore, the parameter of setCount() is one function, in which the rule of updating the count should be defined appropriately.  

done: I have understood the main logic of this.

to-do: build my own component of navigator.
According to the design portfolio, there is one navigator one the head of the page. 

*/
