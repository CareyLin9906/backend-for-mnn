const express = require('express')
const spawn = require('child_process').spawn;
const app = express();
const port = 4200
const bodyParser = require('body-parser');
app.use(bodyParser.json());

app.post('/', (req, res)=>{
  data = (req.body.data)
  console.log(req.body)
  groupingCoeff = (req.body.groupingCoeff)
  sendback = {}
  
    // spawn new child process to call the python script
  const python = spawn('py', ['./script.py', data, groupingCoeff], {shell:true});
  console.log(python.connected)
  python.on('error', (error) => {
      console.error(`Failed to spawn Python process: ${error}`);
    });
  
    // collect data from script
  python.stdout.on('data', (output) => {
      console.log('Pipe data from python script ...');
      temp = output.toString().split('/ ')
      console.log(`this is from js:${output.toString()}`);
      sendback = {
        Budsuper_group_list: JSON.parse(temp[0]),
        number_of_groups:JSON.parse(temp[1])
      }
  });
  
  python.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });
    // in close event we are sure that stream from child process is closed
  python.stderr.pipe(process.stderr);
  
  python.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`);
        // send data to browser
      res.json(sendback)
  });
})
app.listen(port, () => console.log(`Example app listening on port ${port}!`))





