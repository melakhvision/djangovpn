// dashboard.js
const socket = new WebSocket("ws://localhost:8000/ws/status/");

socket.onmessage = function (event) {
  const data = JSON.parse(event.data);
  document.getElementById("cpu").value = data.cpu_load;
  document.getElementById("ram").value = data.ram_usage;
  console.log(data.ram_usage);
  console.log(data.cpu_load);
};
