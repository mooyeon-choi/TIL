import React, { Component } from 'react'

export default class Navbar extends Component {
  render() {
    return (
      <div className="navbar">
        <i className="fas fa-leaf navbar-logo"></i>
        <span className="habit-name">Habit Tracker</span>
        <span className="navbar-count">0</span>
      </div>
    )
  }
}
