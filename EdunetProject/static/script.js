// script.js
function showInfo() {
    var athleteName = document.getElementById('athlete_name').value;

    fetch('/get_info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'athlete_name=' + athleteName
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('infoResult').innerHTML = data.info_text;
        } else {
            document.getElementById('infoResult').innerHTML = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
