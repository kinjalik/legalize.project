async function initIntensivity(arg) {
    const container = $("#intensivity_container");
    console.log("Started")
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
        console.log(dataSet);
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

    xhr.send()
}

function reload() {
    Promise.all([initIntensivity()]);
}

reload();