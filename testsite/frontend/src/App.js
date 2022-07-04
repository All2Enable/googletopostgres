import {
  BrowserRouter as Router,
  Route
} from "react-router-dom";
import React from 'react'
import './App.css';
import Header from './components/Header';
import Tablelistpage from './pages/Tablelistpage';
import TablePage from "./pages/TablePage";


function App() {
  return (
    <Router>
      <div className="container dark">
        <div className="app">
          <Header />
          <Route path="/" exact component={Tablelistpage} />
          <Route path="/entry/:id/" component={TablePage} />
        </div>
      </div>
    </Router>
  );
}

export default App;
