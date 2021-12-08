const path = require('path');
const morgan = require('morgan');
const express = require('express');
const fs = require('fs');

const app = express();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(morgan('dev'));
app.use(express.static(__dirname + '/public'));

const directoryPath = path.join(__dirname, './public/assets/images');

app.get('/', (req, res) => {
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
          res.render('index', { list: list });
        }
      });
    }
  });
});

app.listen(process.env.PORT || 8080, console.log('Server started.'));
