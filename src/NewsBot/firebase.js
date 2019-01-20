let database = function() {
  const firebase = require('firebase-admin');
  	if(!firebase.apps.length){
	    firebase.initializeApp({
	        credential: firebase.credential.cert('./chat-4453f-firebase-adminsdk-l9vhg-551081d47a.json'),
	        databaseURL: "https://chat-4453f.firebaseio.com"
	    });
	}else{
		firebase.app();
	}
    const db = firebase.database();
    return db;
};

exports.database = database;