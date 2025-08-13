let currentParams = {};

function generateDH() {
    const p = document.getElementById("prime").value;
    const g = document.getElementById("generator").value;

    fetch(`/generate?p=${p}&g=${g}`)
        .then(res => res.json())
        .then(data => {
            currentParams = data;
            document.getElementById("output").innerText =
                `p = ${data.p}\ng = ${data.g}\nA = ${data.A}\n(a for demo = ${data.a})`;
        });
}

function bruteforce() {
    fetch("/bruteforce", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(currentParams)
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            document.getElementById("attackOutput").innerText =
                `Error: ${data.error} (Time: ${data.time.toFixed(4)}s)`;
        } else {
            document.getElementById("attackOutput").innerText =
                `Recovered a = ${data.a} in ${data.time.toFixed(4)}s`;
        }
    });
}
