import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Books from './Books'
import Form from './Form'
import Signup from './Signup'

function App() {
  const [count, setCount] = useState(0)
  const[salamu, setSalamu] = useState('')

  useEffect(()=>{
    fetch('/api').then(r=>r.json()).then(data=>setSalamu(data.hello))
  },[])


  return (
    <>
      <Signup/>
      <h1>Lib App</h1>
      <h1>{salamu}</h1>
      <Books/>
      <Form/>
      
    </>
  )
}

export default App
