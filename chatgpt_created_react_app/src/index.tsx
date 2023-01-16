import React from 'react';
import ReactDOM from 'react-dom';
import CandidateTable from './CandidateTable';

const people: Person[] = [
  { name: 'Kevin', age: 30, occupation: 'Great Dental Implant Surgeon', email: 'klgasser@yahoo.com' },
  { name: 'Bob', age: 30, occupation: 'Designer', email: 'glgasser@gmail.com' },
  { name: 'Charlie', age: 35, occupation: 'Project Manager', email: 'mbg29@msn.com' },
];

ReactDOM.render(<CandidateTable people={people} />, document.getElementById('root'));
