import { useState } from "react"

function Form(){
    const[bookname, setBookName] = useState('')
    const[authorname, setAuthorName] = useState('')
    function handleAddBook(e){
        e.preventDefault()
        const userData = {'name': bookname, 'authorname': authorname}
        fetch('/api/books',{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify(userData)
        })
        .then(r=>{
            if(r.ok==true){
                r.json().then(data=>console.log(data))
            }
            else{
                r.json().then(data=>{
                    console.log(data)
                    
                })
            }
        })
    }
    return(
        <>
        <h1>Add a new Book</h1>
        <form onSubmit={handleAddBook}>
            <label>Book Name</label>
            <input type="text" name="name" onChange={(e)=>setBookName(e.target.value)} />
            <label>Author's Name</label>
            <input type="text" name="authorname" onChange={(e)=>setAuthorName(e.target.value)} />
            <input type="submit" value="Add Book" />
        </form>
        </>
    )
}

export default Form