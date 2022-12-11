const message = document.querySelector('#message');

// check if the Geolocation API is supported
if (!navigator.geolocation) {
    message.textContent = `Your browser doesn't support Geolocation`;
    message.classList.add('error');
}

// handle click event
const btn = document.querySelector('#show');
// btn.addEventListener('click', function () {
// get the current position
navigator.geolocation.getCurrentPosition(onSuccess, onError);
// });

var latitude = 45.9432;
var longitude = 24.9668;

function onSuccess(position) {
    console.log("succes");
    const { latitude1, longitude1 } = position.coords;
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
}

function onError() {
    message.classList.add('error');
    console.log("error");
    latitude = 45.9432
    longitude = 24.9668
}

const myArr1 = [latitude, longitude];
console.log(myArr1)

///////////////////////////

let map = L.map('mymap').setView([latitude, longitude], 7);
let ourData = [];

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors',
    maxZoom: 20,
    minZoom: 2,
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);

let iconOption = {
    iconUrl: './assets/location-marker.svg',
    iconSize: [30, 30]
};
let ourCustomIcon = L.icon(iconOption);

fetch("http://172.29.0.3:5000/api/locations/")
    .then(response => response.json())
    .then(data => {
        ourData = data;
        for (let i = 0; i < data.length; i++) {
            let option = document.createElement("option");
            option.value = i + 1;
            option.text = data[i].title;
            document.querySelector(".select-dropdown").appendChild(option);

            let marker = L.marker([data[i].latitude, data[i].longitude], { icon: ourCustomIcon }).bindPopup(`<h3> ${data[i].title} </h3> <p> ${data[i].description} </p>`).on('click', () => {
                map.flyTo([data[i].latitude, data[i].longitude], data[i].zoomLevel);
            }).addTo(map);
        }
    })
    .catch(error => alert(error))


document.querySelector(".map-zoom-out-btn").addEventListener('click', () => {
    map.flyTo([latitude, longitude], 14);
});

document.querySelector(".search-btn").addEventListener('click', () => {
    let select = document.querySelector(".select-dropdown");
    let value = select.options[select.selectedIndex].value;
    map.flyTo([ourData[value - 1].latitude, ourData[value - 1].longitude], ourData[value - 1].zoomLevel);
});
