exports.fbDB = function(){
	const admin = require('firebase-admin');
    admin.initializeApp({
        credential: admin.credential.cert('./chat-4453f-firebase-adminsdk-l9vhg-551081d47a.json'),
        databaseURL: "https://chat-4453f.firebaseio.com"
    });
    const database = admin.database();
    return database;
}