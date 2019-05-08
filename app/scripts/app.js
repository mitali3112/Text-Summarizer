var app = angular.module("text-summary",[
  'ngRoute',
  'ngCookies',
  'ngMaterial',
  'ngAnimate',
  'ngAria',
  'ngFileUpload'
])

app.config(function($routeProvider){
  $routeProvider
  .when("/",{
    templateUrl : "views/main.html",
    controller: 'MainCtrl'
  })
})
app.run(['$rootScope', '$http', function ($rootScope, $http) {
        toastr.options.showMethod = 'slideDown';
        toastr.options.hideMethod = 'slideUp';
        toastr.options.timeOut = 3000;
        toastr.options.preventDuplicates = true;
      }])
