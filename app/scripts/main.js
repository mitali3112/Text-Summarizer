var host = 'http://localhost:3000/api/'
angular.module('text-summary')
    .controller('MainCtrl', function($scope, $location, $http, Upload) {
        console.log("main controller");
        $scope.submit_text = function() {
            console.log("submit here for text ", $scope.text);
            var options = {
                url: host + 'text/',
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                data: {
                    text: $scope.text
                }
            }
            $scope.fetchingFlag = true;
            $http(options)
                .then(function(resp) {
                    $scope.fetchingFlag = false;
                    $scope.resp1 = resp.data.response1;
                    $scope.resp2 = resp.data.response2;
                    $scope.resp3 = resp.data.response3;
                    console.log("resp is ", $scope.response1);
                    console.log("resp is ", $scope.response2);
                    console.log("resp is ", $scope.response3);
                })
                .catch(function(err) {
                    console.log("err ", err);
                })
        }
        $scope.upload = function(file) {
            console.log("file is ", file);
            $scope.fetchingFlag = true;
            Upload.upload({
                url: host+'image/',
                file: file,
            }).then(function(data, status, headers, config) {
                // file is uploaded successfully
                $scope.fetchingFlag = false;
                console.log("uploaded", data);
                $scope.resp1 = data.data.response1;
                $scope.resp2 = data.data.response2;
                $scope.resp3 = data.data.response3;
            });
        };
        //
    })
