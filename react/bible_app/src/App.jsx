import { useState } from 'react'
import './App.css'
import DateInput from './components/DateInput'
import Proverb from './components/Proverb'

function App() {
  const [count, setCount] = useState(0)
  

  return (
    <>
      <h2>Join us in reading the Bible through this year!</h2>
      <DateInput />    
      <Proverb />    
         
    </>
  )
}

export default App



