import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Navigator from './components/navigator/Nav.jsx'

const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <Navigator />
  </StrictMode>,
)