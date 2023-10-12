function click_icon() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }

  function initMap() {
    const myLatLng = {
      lat: 37.06764602661133,
      lng: -4.326528072357178
    };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 18,
      center: myLatLng,
      fullscreenControl: false,
      zoomControl: true,
      streetViewControl: false
    });
    new google.maps.Marker({
      position: myLatLng,
      map,
      title: "My location"
    });
  }