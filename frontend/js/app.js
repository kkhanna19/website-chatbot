async function ingest() {
  const url = document.getElementById("url").value;
  await fetch(`http://127.0.0.1:8000/ingest/?url=${url}`, { method: "POST" });
  alert("Website indexed");
}

async function ask() {
  const q = document.getElementById("question").value;
  const res = await fetch(`http://127.0.0.1:8000/chat/?question=${q}`, {
    method: "POST"
  });
  const data = await res.json();
  document.getElementById("response").innerText = data.answer;
}
