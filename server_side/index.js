var express = require('express');
var bodyParser = require('body-parser');
const pug = require('pug');
const security_key = "f88ee445-ddbe-47a6-b2a1-9134ea7cb1e2"
var app = express();
var fs = require('fs')
var balloons = [[],[],[]]
var last_update = null
app.use(express.static('public'));
app.use(bodyParser.json());
//app.set('views', './views')
//app.set('view engine','pug')
app.post('/', function (req, res) {

  if(req.body.key==security_key){
    if(req.body.image != undefined){
      console.log("working on img");
      var recimage = new Buffer(req.body.image,'base64');
      fs.unlinkSync('public/img.jpg');
      fs.writeFileSync('public/img.jpg',recimage);
    }
    balloons[req.body.id] = parseInt(req.body.pressure);

    last_update = Date().toString()
  }
  else console.log("security fail");
  res.send('');
});

app.get('/', function (req, res) {
/*  var outstr = "";
  for(var i=0;i<balloons.length;i++){
    outstr+="Pressure for balloon " + i + " " + balloons[i][balloons[i].length-1] + "\n";
  }
  res.send(outstr);*/
  balloon_array = [];
  for(x=0;x<balloons.length;x++){
    balloon_array.push([x,balloons[x]])
  }
  res.render('index.pug', { last_update_time : last_update, balloons:balloon_array});

});


app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
