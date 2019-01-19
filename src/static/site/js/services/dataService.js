angular.module('mshack').service('dataService', function (){
	const database = firebase.database();

	function getGroupChat(org){
		return firebase.database().ref(`chat/${org}`);
	}

	function sendChat(groupId, payload){
		return firebase.database().ref(`chat/${groupId}/messages`).push(payload);
	}

	function getGroups(){
		return firebase.database().ref('/groups');
	}

	return {
		getGroupChat: getGroupChat,
		sendChat: sendChat,
		getGroups: getGroups
	}
});