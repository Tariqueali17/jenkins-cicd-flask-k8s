async function fetchStatus() {
    try {
        const res = await fetch("/api/status");
        const data = await res.json();

        document.getElementById("status").innerText = `🟢 ${data.status}`;
        document.getElementById("jenkins").innerText = `🧱 Jenkins: ${data.jenkins}`;
        document.getElementById("kubernetes").innerText = `☸️ ${data.kubernetes}`;
        document.getElementById("docker").innerText = `📦 ${data.docker_image}`;
        document.getElementById("last-updated").innerText = `⏱️ ${data.last_updated}`;

        // Color indicators
        const color = (status) => {
            if (status.includes("Running") || status.includes("Healthy") || status.includes("Passed")) return "#4ade80";
            if (status.includes("Warning") || status.includes("Pending")) return "#facc15";
            return "#f87171";
        };

        document.querySelectorAll(".card p").forEach((p) => {
            p.style.color = color(p.innerText);
        });
    } catch (err) {
        console.error("Failed to fetch data:", err);
    }
}

// Fetch every 5 seconds
setInterval(fetchStatus, 5000);
fetchStatus();
