const path = require('path');
const morgan = require('morgan');
const express = require('express');
const parser = require('body-parser');
const fs = require('fs');
const app = express();

app.use(morgan('dev'));
app.use(parser.json());
app.use(parser.urlencoded({ extended: false }));
app.use(function (req, res, next) {
  res.setHeader('Access-Control-Allow-Headers', 'Accept');
  res.setHeader('Access-Control-Allow-Origin', 'http://localhost:5500');
  res.setHeader('Access-Control-Allow-Methods', 'GET');

  next();
});

const directoryPath = path.join(__dirname, './public/images');

app.get('/images', (req, res) => {
  fs.readdir(directoryPath, (err, filenames) => {
    if (err) {
      return console.log('Unable to scan directory: ' + err);
    }

    const list = [];

    for (let i = 0; i < filenames.length; i++) {
      fs.readFile(directoryPath + '/' + filenames[i], (err, content) => {
        if (err) {
          return console.log(err);
        }

        list.push({
          name: filenames[i]
            .replace(/-/g, ' ')
            .replace('.png', '')
            .toUpperCase(),
          file: content.toString('base64'),
        });

        if (list.length === filenames.length) {
          res.status(200).json(list);
        }
      });
    }
  });
});

app.listen(8080, console.log('Server started.'));
