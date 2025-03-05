import { useState } from 'react'
import './App.css'
import DateInput from './components/DateInput'

function App() {
  const [count, setCount] = useState(0)
  

  return (
    <>
      <h1>Home Page</h1>
      <DateInput />       
    </>
  )
}

export default App



