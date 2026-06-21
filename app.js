const API = "http://127.0.0.1:5000";

async function loadRecords() {

    const records =
        await fetch(API + "/records");

    const data =
        await records.json();

    const list =
        document.getElementById("records");

    list.innerHTML = "";

    data.forEach(item => {

        const li =
            document.createElement("li");

        li.innerText =
            `${item.description}
             ${item.amount}`;

        list.appendChild(li);

    });

    updateBalance();
}

async function addRecord() {

    const description =
        document.getElementById("description").value;

    const amount =
        parseInt(
        document.getElementById("amount").value
        );

    const type =
        document.getElementById("type").value;

    await fetch(API + "/records",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            description,
            amount,
            type

        })

    });

    loadRecords();
}

async function updateBalance() {

    const response =
        await fetch(API + "/balance");

    const data =
        await response.json();

    document.getElementById("balance")
        .innerText =
        "目前餘額：" + data.balance;
}

loadRecords();

if("serviceWorker" in navigator){

    navigator.serviceWorker
        .register("service-worker.js");
}