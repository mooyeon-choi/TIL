import React, { Component } from 'react';
import Habit from './habit';

class Habits extends Component {
  state = {
    habits: [
      { id: 1, name: 'Reading', count: 0},
      { id: 2, name: 'Running', count: 0},
      { id: 3, name: 'Coding', count: 0},
    ]
  }
  
  handleIncrement = (habit) => {
    const habits = [...this.state.habits]; // this.state.habits를 복사
    const index = habits.indexOf(habit);
    habits[index].count++;
    this.setState({ habits }); // { habits : habits } 와 같이 동일한 이름의 데이터는 한번에 써줄 수 있다.
  }

  handleDecrement = (habit) => {
    const habits = [...this.state.habits];
    const index = habits.indexOf(habit);
    const count = habits[index].count - 1;
    habits[index].count = count < 0 ? 0 : count;
    this.setState({ habits });
  }

  render() {
    return <ul>
      {this.state.habits.map(habit => 
        <Habit 
          key={habit.id} 
          habit={habit} 
          onIncrement={this.handleIncrement} 
          onDecrement={this.handleDecrement}
        />
      )}
    </ul>;
  }
}

export default Habits;