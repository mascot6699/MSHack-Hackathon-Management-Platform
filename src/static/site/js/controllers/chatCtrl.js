angular.module('mshack').controller('chatCtrl', function ($scope, dataService){
	$scope.safeApply = function(fn) {
	  let phase = this.$root.$$phase;
	  if(phase == '$apply' || phase == '$digest') {
	    if(fn && (typeof(fn) === 'function')) {
	      fn();
	    }
	  } else {
	    this.$apply(fn);
	  }
	};

	dataService.getGroups().once('value', function(snapshot) {
		$scope.safeApply(function(){
			$scope.allChats = snapshot.val();
		})
	})

	$scope.currentUser = {
		name: $('#user-profile-name').html(),
		id: $('#user-profile-id').html()
	}

	$scope.selectChat = function(index){
		for(let i in $scope.allChats){
			$scope.allChats[i].isActive = false;
		}
		$scope.allChats[index].isActive = true;
		$scope.selectedChat = $scope.allChats[index];
		$scope.groupChat = [];
		console.log($scope.selectedChat);

		getChats($scope.selectedChat.id);
	}

	function getChats(id){
		dataService.getGroupChat(id).on('value', function(snapshot) {
		  let data = snapshot.val();
		  console.log(data.messages);
		  $scope.safeApply(function(){
		  	$scope.groupChat = data.messages;
		  })
		});
	}

	$scope.send = function(message){
		let payload = {
			"sender": $scope.currentUser.name,
            "sender_id": $scope.currentUser.id,
            "message": message,
            "timestamp": (new Date()).toJSON()
		}
		console.log(payload);
		dataService.sendChat($scope.selectedChat.id, payload).then(function(res){
			console.log(res);
		});
	}
});