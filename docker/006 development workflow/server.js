const calculator = require('./calculator');

const express = require('express');

const app = express();

app.all('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const result = calculator.add(id);
  res.send(`${result}`);
});

const port = process.env.PORT || 3000;

app.listen(port, () => console.log(`listening on port2 ${port}`));
