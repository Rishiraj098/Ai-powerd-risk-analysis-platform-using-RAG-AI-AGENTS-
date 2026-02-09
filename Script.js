const BACKEND_URL = "https://YOUR-BACKEND.onrender.com";

async function upload() {
  const file = document.getElementById("fileInput").files[0];
  const form = new FormData();
  form.append("file", file);

  await fetch(`${BACKEND_URL}/upload`, {
    method: "POST",
    body: form
  });

  alert("Document uploaded");
}

async function ask() {
  const q = document.getElementById("question").value;
  const res = await fetch(`${BACKEND_URL}/query?question=${q}`, {
    method: "POST"
  });
  const data = await res.json();
  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
}
