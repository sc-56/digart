import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

/*

JSX is for Javascript XML and it could combine XML and Javascript well in one file. 

This is main.jsx. There is only one function which is createRoot(). "root" is one division in the index.html. This function creates the root element by the function render(). render() means creating the HTML element. The parameter in render() is "App", which is imported from "App.jsx".   Also the index.css is imported.  

*/