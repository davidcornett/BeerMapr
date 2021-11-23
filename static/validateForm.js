
var zip = document.getElementById('zip');
var gps = document.getElementById('gps');

document.getElementById('submitForm').addEventListener('click', function(event){
    if (zip == '') {
        event.preventDefault();
        alert('You cannot leave location blank.  Please enter a zip code or click the LOCATE ME button.')
    }
});