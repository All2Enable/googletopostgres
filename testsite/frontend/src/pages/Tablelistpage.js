import React, {useState, useEffect, Component} from 'react'
import ListItem from '../components/ListItem'


const Tablelistpage = () => {

    let url = `wss://${window.location.host}/ws/socket-server/`
    const chatSocket = new WebSocket(url)
    
    let [Tables, setTables] = useState([])

    useEffect(()=> {
        getTables()
    }, [])


    let getTables = async () => {

        let response = await fetch('/api/table/')
        let data = await response.json()
        setTables(data)
        
    }
    
    chatSocket.onmessage = function(e){
        let mess = JSON.parse(e.data)

        if (mess.type === 'table') {
            getTables.call()          
        }
    }

  return (
    <div className='tables'>
        <div className='tables-header'>
            <h2 className='tables-title'>&#9782; Заказы</h2>
            <p className='tables-count'>{Tables.length}</p>
        </div>
        <div>
            <div className='tables-list'>
                {Tables.map((table, index) => (
                    <ListItem key={index} table={table} />
                ))}
            </div>
        </div>
    </div>
  )
}

export default Tablelistpage