const express = require('express');

const app = express();

const redis = require('redis');
const client = redis.createClient({
  host: 'redis-server',
});

client.set('visits', 0);
app.all('', (req, res) => {
  client.get('visits', (err, visits) => {
    res.send(`number of visits: ${visits}`);
    client.set('visits', visits - -1);
    console.log('increament');
  });
});

app.listen(3000, () => {
  console.log(`listening on port 3000`);
});
