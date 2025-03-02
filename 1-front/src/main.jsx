import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Navigator from './components/navigator/Nav.jsx'
import Contentor from './components/contentor/Con.jsx'

const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <Navigator />
    <div id="container">
      <Contentor />
    </div>
  </StrictMode>,
)