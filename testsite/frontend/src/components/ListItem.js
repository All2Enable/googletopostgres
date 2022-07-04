import React from 'react'
import { Link } from 'react-router-dom'

const ListItem = ({ table }) => {
  return (
    // <Link to={`/table/${table.id}`}>
      <div className='tables-list-item'>
        <li>ID: {table.id}</li>
        <h3>Номер заказа: {table.zakaz_field}</h3>
        <h3>Стоимость в долларах: {table.stoimostvdol_field}$</h3>
        <h3>Срок поставки: {table.srok_postavki}</h3>
        <h3>Стоимость в рублях: {table.stoimostvrub}</h3>

      </div>
    // </Link>
  )
}

export default ListItem