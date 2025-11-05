document.addEventListener("DOMContentLoaded", () => {
  const ctx = document.getElementById("chartCanvas");
  if (!ctx) return;

  const subjects = ["Math", "Science", "English", "History", "Computer"];
  const marks = [78, 92, 65, 48, 88];

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: subjects,
      datasets: [
        {
          label: "Marks",
          data: marks,
          backgroundColor: "rgba(0, 123, 255, 0.6)",
        },
      ],
    },
    options: {
      scales: {
        y: { beginAtZero: true, max: 100 },
      },
    },
  });
});
