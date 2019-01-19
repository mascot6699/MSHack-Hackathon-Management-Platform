angular
.module('mshack', ['ngMaterial', 'ngMessages', 'ui.router'])
.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise('/');
  $stateProvider.state({
  	name: 'chat',
    url: '/',
    controller: 'chatCtrl',
    // templateUrl: '/assets/views/chat.html'
    template: `<div class="chat"> <div class="chat__members-panel"> <div class="chat__member" ng-repeat="chat in allChats" ng-click="selectChat($index)" ng-class="chat.isActive ? 'chat__member--active' : ''"> <img ng-src="{{chat.icon}}" class="chat__member__avatar"> <div> <div class="chat__member__name">{{chat.name}}</div><div class="chat__member__meta">{{chat.meta}}</div></div></div></div><div class="chat__messages-panel"> <div class="chat__container"><!-- <div class="chat__bubble chat__bubble--received chat__bubble--sent" ng-repeat="i in [1,2,3]"> <div class="chat__bubble__name"> Amit Singh </div><div class="chat__bubble__message"> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </div></div>--> <div class="chat__bubble" ng-repeat="message in groupChat" ng-class="message.sender_id===currentUser.id ? 'chat__bubble--sent': 'chat__bubble--received'"> <div class="chat__bubble__name">{{message.sender}}</div><div class="chat__bubble__message">{{message.message}}</div></div></div><form class="chat__message__container" autocomplete="off" ng-submit="send(sendThisMessage)" ng-if="selectedChat"> <input type="text" name="message" class="chat__message" placeholder="Type a message" autocomplete="off" ng-model="sendThisMessage"> </form> </div></div>`
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
