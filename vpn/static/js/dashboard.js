// dashboard.js
const socket = new WebSocket("ws://localhost:8000/ws/status/");

socket.onmessage = function (event) {
  const data = JSON.parse(event.data);
  document.getElementById("cpu").value = data.cpu_load;
  document.getElementById("ram").value = data.ram_usage;
  document.getElementById("h2cpu").innerText = data.cpu_load + "%";
  document.getElementById("h2ram").innerText = data.ram_usage + "%";
  // console.log("Data received from WebSocket: ");
  // console.log(data.ram_usage);
};
