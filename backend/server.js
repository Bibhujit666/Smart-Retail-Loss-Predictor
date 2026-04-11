const express = require("express");
const path = require("path");
require("dotenv").config();

const predictionRoutes = require("./routes/predictionRoutes");

const app = express();

// ✅ Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json()); // ✅ FIXED

// ✅ Static files (CSS, JS)
app.use(express.static(path.join(__dirname, "../public")));

// ✅ View engine setup
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "../views"));

// ✅ Routes
app.use("/", predictionRoutes);

// ✅ 404 handler
app.use((req, res) => {
  res.status(404).send("Page not found");
});

// ✅ Port config
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});