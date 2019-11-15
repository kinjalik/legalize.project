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
    xhr.open("GET", "api_placeholders/packet_intensivity.json")
    
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
    xhr.open("GET", "api_placeholders/devices.json")
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
    xhr.open("GET", "api_placeholders/full-device-list.json");
    xhr.onload = () => {
        const dataSet = JSON.parse(xhr.response);
        console.log(dataSet);
        for (let device of dataSet) {
            let props = "";
            for (let prop of device.data) {
                props += `<li class="list-group-item"><b>${prop.key}</b>: ${prop.value}</li>`
            }
            container.innerHTML = container.innerHTML + `<div class="col-3">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${device.type} by ${device.manufacturer}</h5>
                </div>
                <ul class="list-group list-group-flush">
                        <li class="list-group-item"><b>PanID</b>: ${device.panID}</li>
                        <li class="list-group-item"><b>MAC</b>: ${device.mac}</li>
                        ${props}
                </ul>
            </div>
        </div>`
        }
    }
    xhr.send();
}

function reload() {
    console.log("Scanning...");
    Promise.all([initIntensivity(), drawDeviceList(), drawDeviceCards() ]);
}

reload();

document.querySelector("#rescan").onclick = () => {
    reload();
}