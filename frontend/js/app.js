(function ($) {
    var brewshop = angular.module('brewshop', ['angular-loading-bar'])
        .config(['cfpLoadingBarProvider', function (cfpLoadingBarProvider) {
            cfpLoadingBarProvider.includeSpinner = false;
            cfpLoadingBarProvider.parentSelector = '#loading-bar-container';
        }]);

    brewshop.controller('TitleListController', function TitleListController($scope, $http) {
        $http.get('https://brewshop.github.io/BrewShopCTR/list0.json').then(function (response) {
            $scope.titles = response.data.sort(function (a, b) {
                if (a.name.toUpperCase() < b.name.toUpperCase()) return -1;
                if (a.name.toUpperCase() > b.name.toUpperCase()) return 1;
                return 0;
            });
        });
        console.log(titles);
    });

    //Filesize filter, credit to https://gist.github.com/yrezgui/5653591
    brewshop.filter('filesize', function () {
        var units = [
            'bytes',
            'KB',
            'MB',
            'GB',
            'TB',
            'PB'
        ];

        return function (bytes, precision) {
            if (isNaN(parseFloat(bytes)) || !isFinite(bytes)) {
                return '?';
            }

            var unit = 0;

            while (bytes >= 1024) {
                bytes /= 1024;
                unit++;
            }

            return bytes.toFixed(+ precision) + ' ' + units[unit];
        };
    });
})();

/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}