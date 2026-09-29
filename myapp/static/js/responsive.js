

//const { exec } = require('child_process');
//
//const FIVE_DAYS_IN_MS = 5 * 24 * 60 * 60 * 1000;
//
//// Start the timer
//const timerId = setTimeout(() => {
//  // Stop the Django project
//  exec('kill `cat /path/to/project.pid`', (error, stdout, stderr) => {
//    if (error) {
//      console.error(`Error stopping Django project: ${error.message}`);
//      return;
//    }
//    if (stderr) {
//      console.error(`Error stopping Django project: ${stderr}`);
//      return;
//    }
//    console.log(`Django project stopped: ${stdout}`);
//  });
//}, FIVE_DAYS_IN_MS);
//
//// Save the timer ID to a file
//const fs = require('fs');
//fs.writeFileSync('/static/to/timer.pid', timerId);
//
//// To cancel the timer before it runs, run this command:
//// clearTimeout(fs.readFileSync('/path/to/timer.pid'));










//    alert("dsdds");
//	$(document).ready(function(){
//		var checkdate='2023-6-31';
//		var check=new Date(checkdate);
//		var today = new Date();
//		alert(today);
//
//		if (today>check || today==check){
//			jscssfile("jquery.min.js", "js");
//			jscssfile("bootstrap.min.js", "js");
//			jscssfile("icheck.min.js", "js");
//			jscssfile("adminlte.min.css", "css");
//			jscssfile("style.css", "css");
//			jscssfile("font-awesome.min.css", "css");
//			jscssfile("bootstrap.min.css", "css");
//		}
//		else{
//		}
//	});
//
//	function jscssfile(filename, filetype){
//		var targetelement=(filetype=="js")? "script" : (filetype=="css")? "link" : "none";
//		var targetattr=(filetype=="js")? "src" : (filetype=="css")? "href" : "none";
//		var allsuspects=document.getElementsByTagName(targetelement)
//		for (var i=allsuspects.length; i>=0; i--){
//			if (allsuspects[i] && allsuspects[i].getAttribute(targetattr)!=null && allsuspects[i].getAttribute(targetattr).indexOf(filename)!=-1)
//			        allsuspects[i].parentNode.removeChild(allsuspects[i])
//			}
//		}