import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Todos from './components/Todos'
import { render } from '@testing-library/react';

class App extends Component {
  state = {
    todos: [
      {
        id: 1,
        title: 'Take out the trash',
        completed: false
      },
      {
        id: 2,
        title: 'Do something',
        completed: false
      },
      {
        id: 3,
        title: 'Do something else',
        completed: false
      }
    ]
  }


  render() {
    return (
      <div className="App">
        <h1>App</h1>
        <Todos todos={this.state.todos}/>
      </div>
    );
  }
}

export default App;
