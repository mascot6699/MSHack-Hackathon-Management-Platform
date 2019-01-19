angular.module('mshack').controller('chatCtrl', function ($scope, dataService){
	$scope.allChats = [{
		name: 'Mshack',
		meta: 'This is the last messgae sent',
		icon: 'https://image.flaticon.com/icons/svg/149/149071.svg',
		id: 'guid'
	},
	{
		name: 'Sequia Hack',
		meta: 'This is the last messgae sent',
		icon: 'https://image.flaticon.com/icons/svg/149/149071.svg',
		id: 'guid'
	},{
		name: 'Angel Hack',
		meta: 'This is the last messgae sent',
		icon: 'https://image.flaticon.com/icons/svg/149/149071.svg',
		id: 'guid'
	}]

	$scope.selectChat = function(index){
		for(let i in $scope.allChats){
			$scope.allChats[i].isActive = false;
		}
		$scope.allChats[index].isActive = true;
		$scope.selectedChat = $scope.allChats[index];
		console.log($scope.selectedChat);

		dataService.getOrganisationData($scope.selectedChat.id).on('value', function(snapshot) {
		  console.log(snapshot.val());
		});
	}

	$scope.send = function(){
		console.log($scope.message);
		$scope.message = '';
	}
});