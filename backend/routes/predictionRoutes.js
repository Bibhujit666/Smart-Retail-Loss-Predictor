const express = require("express");
const router = express.Router();
const { getHome, postPrediction } = require("../controllers/predictionController");

router.get("/", getHome);
router.post("/predict", postPrediction);

module.exports = router;