import './app.css';
import React, { Component } from 'react';
import Habits from './components/habits';
import Navbar from './components/navbar';

class App extends Component {
  state = {
    total: 0
  }

  changeTotal = (total) => {
    this.setState({ total })
  }

  render() {
    return (
      <React.Fragment>
        <Navbar totalCount={this.total}/>
        <Habits onChangeTotal={this.changeTotal}/>
      </React.Fragment>
    )
  }
}

export default App;
