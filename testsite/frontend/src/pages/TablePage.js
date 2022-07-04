import React, { useState, useEffect } from 'react'

const TablePage = ({ match }) => {
    
  let entryId = match.params.id
  let [entry, setEntry] = useState(null)

  useEffect(()=> {
    getEntry()
  }, [entryId])

  let getEntry = async ()=> {

      let response = await fetch(`/api/table/${entryId}`)
      let data = await response.json()
      console.log('DATA:', data)
      setEntry(data)
  }

  return (
    <div>
      <p>{entry}</p>
    </div>
  )
}

export default TablePage