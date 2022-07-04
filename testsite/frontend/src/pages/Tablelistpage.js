import React, {useState, useEffect, Component} from 'react'
import ListItem from '../components/ListItem'
// import { w3cwebsocket as W3CWebSocket } from "websocket";


// class Connection extends Component {

//     client = new W3CWebSocket('ws://127.0.0.1:8000/table/api' + this.state.room + '/');

//     componentDidMount() { 
//         this.client.onopen = () => { 
//             console.log('WebSocket Client Connected')
//         }
//     }
// }



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
        let data = JSON.parse(e.data)
        console.log('CAL:', data)

        if (data.type === 'table') {
            console.log('JOPOSHNIK:', data)
            // useEffect(()=> {
            //     getTables()
            // }, [])
        }
        else {
            console.log(data.type)
        }
        return (getTables)
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