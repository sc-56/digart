import React from "react"; 
import Greeting from "./components/Greeting"
import Counter from "./components/Counter"

function App() {
    return (
        <div>
            <h1>Welcome to React.</h1>
            <Greeting name="Alice" />
            <Greeting name="Bob" />
            <Counter />
        </div>
    );
}

export default App;