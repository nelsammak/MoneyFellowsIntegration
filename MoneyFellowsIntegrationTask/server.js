const http = require('http');
var Promise = require('promise');
const PORT=3100; 


var body='';
var resp='';
var promise;
function sendToPy(pyData){
	promise= new Promise(function(fulfil,reject){
	body=pyData.toString();
	const req = http.request(
		{
		  hostname: '127.0.0.1',
		  port: 3101,
		  path: '/',
		  method: 'POST',
		  headers: {
		    'Content-Type': 'application/json',
		    'Content-Length': body.length
		  }
		}
		, (res) => {
	  console.log(`statusCode: ${res.statusCode}`)

	  res.on('data', (d) => {
	  	resp=d.toString();
	  	fulfil(resp);
	  })
	})

	req.on('error', (error) => {
		reject(error)
		fulfil(error)
	  	console.error(error)
	})

	req.write(body)
	req.end()
	})
}
http.createServer((request,response)=>{
	//var resp='';
	if (request.method=='POST'){
		request.on('data', (chunk)=>{ sendToPy(chunk)});
		request.on('end', () => {
			promise.then(()=>{
				 console.log(resp);
				 response.end(resp);
			}, function(err) {
					response.end(err);
        			console.log(err);
    		});
			//return new Promise(function(fulfil,reject){})
	    //console.log(Promise.resolve(promise));
	    //response.end(body);
	  });
		}
}).listen(PORT, function(){
    console.log("Server listening on: http://localhost:%s", PORT);
});
