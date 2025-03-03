import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Navigator from './components/navigator/Nav.jsx'
import Contentor from './components/contentor/Con.jsx'
import Sky from './components/nightsky/Sky.jsx'

const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <Navigator />

    <div id="container-1">
      <div class="column" id="sky">Sky</div>
      <div class="column" id="contentor">Content</div>
    </div>

  </StrictMode>,
)