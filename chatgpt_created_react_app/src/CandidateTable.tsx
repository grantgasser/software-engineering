import React, { useState } from 'react';

import { makeStyles, createStyles, Theme } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';

interface Person {
  name: string;
  age: number;
  occupation: string;
  decision?: 'Yes' | 'No';
  email: string;
}

interface Props {
  people: Person[];
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    table: {
      minWidth: 450,
      fontFamily: 'Karla, Arial, sans-serif'
    },
    tableRow: {
      '&:nth-of-type(odd)': {
        backgroundColor: '#8ED4F7',
      },
      '&:nth-of-type(even)': {
        backgroundColor: '#A5AFFA',
      },
    },
    tableCell: {
      color: '#2346B9',
    },
    decisionCell: {
      color: '#D26491',
    },
    blueBackground: {
      backgroundColor: '#2346B9',
    },
    text: {
      color: '#FFFFFF'
    },
  })
);

const CandidateTable: React.FC<Props> = ({ people }) => {
  const classes = useStyles();

  // Add state to the component using the useState hook
  const [state, setState] = useState<Person[]>(people);

  function updateDecision(person: Person, decision: string) {
    const updatedPerson = { ...person, decision };
    setState(state.map((p) => (p === person ? updatedPerson : p)));
  }

  return (
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="candidate table">
        <TableHead className={classes.blueBackground}>
          <TableRow>
            <TableCell className={classes.text}>Name</TableCell>
            <TableCell className={classes.text}>Age</TableCell>
            <TableCell className={classes.text}>Occupation</TableCell>
            <TableCell className={classes.text}>Email</TableCell>
            <TableCell className={classes.text}>Decision</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {people.map(person => (
            <TableRow key={person.name} className={classes.tableRow}>
              <TableCell>{person.name}</TableCell>
              <TableCell>{person.age}</TableCell>
              <TableCell>{person.occupation}</TableCell>
              <TableCell>{person.email}</TableCell>
              <TableCell className={classes.decisionCell}>
                <Select
                  value={person.decision}
                  onChange={e => updateDecision(person, e.target.value)}
                >
                  <MenuItem value="">
                    <em>None</em>
                  </MenuItem>
                  <MenuItem value="Yes">Yes</MenuItem>
                  <MenuItem className={classes.decisionCell} value="No">No</MenuItem>
                </Select>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default CandidateTable;
