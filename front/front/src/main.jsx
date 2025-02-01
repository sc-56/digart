import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Navigator from './Nav.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Navigator />
  </StrictMode>,
)

/*

JSX is for Javascript XML and it could combine XML and Javascript well in one file. 

This is main.jsx. There is only one function which is createRoot(). "root" is one division in the index.html. This function creates the root element by the function render(). render() means creating the HTML element. The parameter in render() is "App", which is imported from "App.jsx".   Also the index.css is imported. 

It seems that '.jsx' is good format. It could import the HTML, CSS and Javascript in one file. 

After defining the component, the "Hello world" displayed appropriately on the page, but the style is not correct. Therefore, the next step should be defining the "Nav.css" file. 

Everything is within the element of root. Therefore, they are allocated in the middle part. After deleting the setting in the App.css, the centerizing function doesn't exist, but the starting point is not from the left corner. 

This is probability because that the setting in "index.css"; This is becuase of the setting in "index.css" -> body component. There is one setting named "place-items: center;", which could center both "align-items" and "justify-items" at same time. Therefore, the component is at the center of screen. 

done: The navigator has been added as one component using the 


*/