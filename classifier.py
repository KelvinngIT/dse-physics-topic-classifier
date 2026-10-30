from typing import Tuple, Dict

# Official DSE Physics Topics
TOPICS = [
    "Heat and Gases",
    "Force and Motion",
    "Wave Motion",
    "Electricity and Magnetism",
    "Radioactivity and Nuclear Energy",
    "Astronomy and Space Science",
    "Atomic World",
    "Energy and Use of Energy",
    "Medical Physics",
    "Unclassified"
]

TOPIC_KEYWORDS: Dict[str, list] = {
    "Heat and Gases": [
        "specific heat", "latent heat", "heat capacity", "gas law", "ideal gas",
        "kinetic theory", "internal energy", "thermal", "temperature", "heat transfer",
        "conduction", "convection", "radiation", "melting", "boiling"
    ],
    "Force and Motion": [
        "newton", "momentum", "projectile", "circular motion", "centripetal",
        "gravitation", "work done", "kinetic energy", "potential energy",
        "acceleration", "force", "velocity", "displacement", "friction", "impulse"
    ],
    "Wave Motion": [
        "wavelength", "frequency", "interference", "diffraction", "refraction",
        "reflection", "lens", "sound wave", "stationary wave", "v = fλ",
        "fringe", "amplitude", "period", "transverse", "longitudinal"
    ],
    "Electricity and Magnetism": [
        "ohm", "resistance", "current", "voltage", "magnetic field",
        "electromagnetic induction", "faraday", "transformer", "capacitor",
        "electrostatic", "ac", "rms", "solenoid", "coil", "power", "circuit"
    ],
    "Radioactivity and Nuclear Energy": [
        "radioactive", "half-life", "alpha", "beta", "gamma", "nuclear",
        "fission", "fusion", "decay", "isotope", "radiation", "nucleus"
    ],
    "Atomic World": [
        "photoelectric", "photon", "bohr", "energy level", "de broglie",
        "wave-particle", "quantum", "electron diffraction", "threshold frequency"
    ],
    "Medical Physics": [
        "ultrasound", "x-ray", "ct scan", "mri", "radioisotope", "imaging",
        "piezoelectric", "attenuation", "dosimetry"
    ],
    "Astronomy and Space Science": [
        "star", "galaxy", "orbit", "kepler", "parallax", "black hole",
        "universe", "planet", "satellite", "light year", "hr diagram"
    ],
    "Energy and Use of Energy": [
        "efficiency", "renewable", "power station", "energy consumption",
        "insulation", "fossil fuel", "solar", "wind energy"
    ]
}

def classify_question(question: str) -> Tuple[str, int]:
    """
    Classify a question into a DSE Physics topic using keywords.
    Returns (topic_name, score)
    """
    q_lower = question.lower()
    scores = {topic: 0 for topic in TOPIC_KEYWORDS}

    for topic, keywords in TOPIC_KEYWORDS.items():
        for kw in keywords:
            if kw in q_lower:
                scores[topic] += 1

    best_topic = max(scores, key=scores.get)
    best_score = scores[best_topic]

    if best_score == 0:
        return "Unclassified", 0
    return best_topic, best_score
