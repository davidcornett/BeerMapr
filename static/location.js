/* Code modified from:
https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
*/

function findMe() {

    const zip = document.getElementById('zipSection'); //identifies zip code div in form
    zip.style.display = 'none';  // hides div to make room for gps field

    const gpsSection = document.getElementById('gpsSection'); //identifies gps div in form
    gpsSection.style.display = 'block'; // makes div visible 

    const gps = document.getElementById('gps'); //identifies gps field in form
    gps.value = '';
    
  
    function success(position) {
      const latitude  = position.coords.latitude; 
      const longitude = position.coords.longitude;
  
      gps.value = `${latitude},${longitude}`; //auto fill field with gps string
    }
  
    function error() {
      alert('Unable to retrieve your location.  Try again or enter Zip Code instead.');
    }
  
    if(!navigator.geolocation) {
      alert('Geolocation is not supported by your browser');
    } else {
      navigator.geolocation.getCurrentPosition(success, error);
    }
  }
  
  document.querySelector('#autoLocate').addEventListener('click', findMe);
  