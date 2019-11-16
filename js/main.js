const BACKEND_IP = "http://10.91.7.152:2528";
const fake_mode = false;

const timeModeButtons = {
    'min': document.querySelector("#modeMin"),
    'hour': document.querySelector("#modeHour"),
    'day': document.querySelector("#modeDay")
}
let currentMode = 'min';    
timeModeButtons[currentMode].disabled = true;

for (let mode in timeModeButtons) {
    console.log(timeModeButtons[mode]);
    timeModeButtons[mode].onclick = () => {
        timeModeButtons[currentMode].disabled = false;
        const oldMode = currentMode;
        currentMode = mode;
        timeModeButtons[currentMode].disabled = true;
        console.log(`Mode changed: from ${oldMode} to ${currentMode}`);
    }
}

async function initIntensivity() {
    const container = $("#intensivity_container");
    container.innerHTML = "";
    let xhr = new XMLHttpRequest();
    
    xhr.open("GET",  "api_placeholders/packet_intensivity.json")
    // xhr.open("GET",  "api_placeholders/packet_intensivity.json")
    
    xhr.onload = () => {
        const dataSet = JSON.parse(xhr.response);
        const timestamps = dataSet.timestamps;
        const labels = []
        timestamps.forEach(element => {
            const dt = new Date(element);
            labels.push(`${dt.getHours()}:${dt.getMinutes()}:${dt.getSeconds()}`);
        });
        const values = dataSet.values;
        // console.log(dataSet);
        const ctx = document.getElementById('intensivity_container').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels,
                datasets: [{
                    data: values,
                    borderColor: "#3e95cd",
                    fill: false
                }]
            },
            options: {
                legend: {
                    display: false,
                },
                title: {
                    display: true,
                    text: 'Интенсивность пакетов'
                }
            }
        });
    };

    xhr.send();
}

async function drawDeviceList() {
    const container = document.querySelector("#device_list");
    container.innerHTML = "";

    let xhr = new XMLHttpRequest();
    console.log(fake)
    xhr.open("GET", fake_mode ? "api_placeholders/devices.json" : BACKEND_IP + "/api/intensivity")
    xhr.onload = () => {
        const dataSet = JSON.parse(xhr.response);
        for (let device of dataSet) {
            container.innerHTML = container.innerHTML + `<tr>
            <th scope="row">${device.panID}</th>
            <td>${device.mac}</td>
            <td>${device.manufacturer}</td>
            <td>${device.type}</td>
            <td>${device.signal}</td>
          </tr>`;
        }
        
    };

    xhr.send();

}

async function drawDeviceCards() {
    const container = document.querySelector("#cards_container");
    container.innerHTML = "";
    let xhr = new XMLHttpRequest();
    xhr.open("GET", BACKEND_IP + "/api/devices");
    xhr.onload = () => {
        console.log(xhr.response)
        const dataSet = JSON.parse(xhr.response);
        console.log(dataSet);
        for (let device of dataSet) {
            console.log(device)
            container.innerHTML = container.innerHTML + `<div class="col-3">
            <div class="card">
                <ul class="list-group list-group-flush">
                    <li class="list-group-item"><b>PanID</b>: ${device.panID}</li>
                    <li class="list-group-item"><b>MAC</b>: ${device.mac}</li>
                    <li class="list-group-item"><b>RSSI</b>: ${device.rssi}</li>
                    <li class="list-group-item"><b>${device.data.sensor}</b>: ${device.data.value}</li>
                </ul>
            </div>
        </div>`
        }
    }
    xhr.send();
}

function reload() {
    console.log("Scanning...");
    Promise.all([
        initIntensivity(), 
        //drawDeviceList(), 
        drawDeviceCards() ]);
}

reload();

document.querySelector("#rescan").onclick = () => {
    reload();
}