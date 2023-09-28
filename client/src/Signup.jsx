import { useState } from "react"

function Signup(){
    const[userName, setUserName] = useState('')
    const[password, setPassword] = useState('')
    function handleSignUp(e){
        e.preventDefault()
        const userData = {'username':userName, 'password':password}
        fetch('/api/signup',{
          method:"POST",
          headers:{
            "Content-Type":"application/json"
          },
          body: JSON.stringify(userData)
        })
        .then(res=>{
          console.log(res)
          if(res.ok == true){
            res.json().then(data=>console.log(data))
          }
          else{
            res.json().then(data=>{
              console.log(data)
              alert(data.message)
            })
            // console.log(res)
          }
        })
      }
    return(
        <>
        <h1>Sign Up</h1> 
    <form onSubmit={handleSignUp}>
        <label>
          User Name:
          <input type="text" name="username" onChange={(e)=>setUserName(e.target.value)}/>
        </label>
        <label>
          Password:
          <input type="text" name="password" onChange={(e)=>setPassword(e.target.value)}/>
        </label>
        <input type="submit" value="Submit" />
      </form>
        </>
    )
}

export default Signup