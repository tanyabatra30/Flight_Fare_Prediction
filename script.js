// document.querySelector("form").addEventListener("submit", function(event) {
//     event.preventDefault();
//     const formData = new FormData(this);
//     fetch("/predict", {
//         method: "POST",
//         body: formData
//     })
//   .then(response => response.json())
//   .then(data => {
//         document.getElementById("prediction").innerText = `Predicted Fare: $${data.predictedFare}`;
//     })
//   .catch(error => console.error("Error:", error));
// });
function updateTimeDisplay() {
    const currentTime = new Date();
    const hours = currentTime.getHours();
    const minutes = currentTime.getMinutes();
    const ampm = hours >= 12? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours? hours : 12; // the hour '0' should be '12'
    const strTime = hours + ':' + minutes + ' ' + ampm;
    document.getElementById('current-time').innerText = strTime;
}

setInterval(updateTimeDisplay, 1000); // Update every second
