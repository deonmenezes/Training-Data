const verifyBtn = document.getElementById("verifyBtn");
const verifyOut = document.getElementById("verifyOut");

const analyzeBtn = document.getElementById("analyzeBtn");
const analyzeOut = document.getElementById("analyzeOut");

const videoUrlInput = document.getElementById("videoUrl");
const customEventInput = document.getElementById("customEvent");
const customCategoryInput = document.getElementById("customCategory");

function pretty(value) {
  return JSON.stringify(value, null, 2);
}

verifyBtn.addEventListener("click", async () => {
  verifyOut.textContent = "Verifying...";
  try {
    const response = await fetch("/api/verify-auth");
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "Verify failed");
    verifyOut.textContent = pretty(data);
  } catch (error) {
    verifyOut.textContent = String(error);
  }
});

analyzeBtn.addEventListener("click", async () => {
  const video_url = videoUrlInput.value.trim();
  if (!video_url) {
    analyzeOut.textContent = "Video URL is required";
    return;
  }

  analyzeOut.textContent = "Running analysis...";

  try {
    const response = await fetch("/api/analyze-url", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        video_url,
        custom_event: customEventInput.value.trim(),
        custom_category: customCategoryInput.value.trim(),
      }),
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "Analysis failed");
    analyzeOut.textContent = pretty(data);
  } catch (error) {
    analyzeOut.textContent = String(error);
  }
});
