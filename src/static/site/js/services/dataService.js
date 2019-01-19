angular.module('mshack').service('dataService', function (){
	const database = firebase.database();

	function getOrganisationData(org){
		return firebase.database().ref(org);
	}

	return {
		getOrganisationData: getOrganisationData
	}
});