// Function to Fetch Romantic Pickup Lines
function getPickupLine() {
    let name = document.getElementById("nameInput").value || "Crush";

    fetch("/get_pickup_line", {
        method: "POST",
        body: JSON.stringify({ name: name }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("pickupLine").innerText = data.line;
    })
    .catch(error => console.error("Error:", error));
}

// Floating Hearts Effect
function createHeart() {
    const heart = document.createElement("div");
    heart.innerHTML = "❤️";
    heart.classList.add("heart");
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = Math.random() * 3 + 2 + "s";
    document.body.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 5000);
}

setInterval(createHeart, 500);
