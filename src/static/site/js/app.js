angular
.module('mshack', ['ngMaterial', 'ngMessages', 'ui.router'])
.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise('/');
  $stateProvider.state({
  	name: 'chat',
    url: '/',
    controller: 'chatCtrl',
    templateUrl: '/assets/views/chat.html'
  });
})
.run(function(){
	const config = {
	    apiKey: "AIzaSyBWSPc_qZEH6wNd6I1dv8dm5ErkqodnqI8",
	    authDomain: "chat-4453f.firebaseapp.com",
	    databaseURL: "https://chat-4453f.firebaseio.com",
	    projectId: "chat-4453f",
	    storageBucket: "chat-4453f.appspot.com",
	    messagingSenderId: "266885685983"
	};
	firebase.initializeApp(config);

});
