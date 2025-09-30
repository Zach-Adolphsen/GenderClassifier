import './App.css';
import {useEffect, useState} from "react";

function App() {

    const [data, setData] = useState({
        name: '', age: 0
    });

    useEffect(() => {
        fetch('/api/data').then(res => res.json()).then((data) => {
            setData({
                name: data.name,
                age: data.age,
            });
        })
    })

  return (
    <div className="App">
        <h2>Hello User!</h2>
        <form action="">
            <div>Enter Weight: <input type="number"/></div>
            <div>Enter Height: <input type="number"/></div>
            <div>Enter Shoe Size: <input type="float"/></div>
        </form>
        <div>
            <h2>api data</h2>
            <p>{data.name}</p>
            <p>{data.age}</p>
        </div>
    </div>
  );
}

export default App;
