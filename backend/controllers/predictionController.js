const axios = require("axios");

// 🏠 Home Page
exports.getHome = (req, res) => {
  res.render("index");
};

// 📊 Prediction Logic
exports.postPrediction = async (req, res) => {
  try {
    const data = req.body;

    // 🔄 Call Python ML API
    const response = await axios.post("http://127.0.0.1:8000/predict", {
      temperature: Number(data.temperature),
      humidity: Number(data.humidity),
      footfall: Number(data.footfall),
      staff: Number(data.staff),
      experience: Number(data.experience),
      cold_chain: Number(data.cold_chain),
      is_weekend: Number(data.is_weekend)
    });

    const prediction = response.data.prediction;

    // 🚨 Risk Level Logic
    let risk = "Low Risk ✅";
    if (prediction > 7000) {
      risk = "High Risk 🚨";
    } else if (prediction > 4000) {
      risk = "Medium Risk ⚠️";
    }

    // 💡 Insight Message
    let insight = "";
    if (prediction > 7000) {
      insight = "High loss risk detected! Check temperature, staffing, and cold chain handling.";
    } else if (prediction > 4000) {
      insight = "Moderate risk. Monitor operations closely.";
    } else {
      insight = "Operations look stable. Low risk of loss 👍";
    }

    // 🎯 Send to UI
    res.render("result", {
      result: prediction.toFixed(2),
      risk,
      insight
    });

  } catch (error) {
    console.error("❌ Error:", error.message);

    res.status(500).render("result", {
      result: "Error",
      risk: "N/A",
      insight: "Something went wrong while predicting. Please try again."
    });
  }
};