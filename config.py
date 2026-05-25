"""
config.py
=========
Central configuration for the Olkaria GEOS-Chem dissertation project.
ALL other scripts import from here. Change a value once, applies everywhere.

Project: Numerical Simulation of CO2 and CH4 Emissions from Olkaria
         Geothermal Field using GEOS-Chem and Satellite Comparison
Author : [Your Name]
"""

# =============================================================================
#  STUDY SITE
# =============================================================================
TARGET_LAT = -0.933210     # Center of study polygon
TARGET_LON =  36.331589    # Center of study polygon
SITE_NAME  = "Olkaria_Kenya"
SITE_LABEL = "Olkaria Geothermal Field"

# Exact polygon corners (decimal degrees, converted from DMS)
POLYGON = {
    "C1": {"lat": -0.842803, "lon": 36.241878},  # NW corner
    "C2": {"lat": -0.842803, "lon": 36.421436},  # NE corner
    "C3": {"lat": -1.023542, "lon": 36.241736},  # SW corner
    "C4": {"lat": -1.023692, "lon": 36.421306},  # SE corner
}

# Polygon bounding box
POLY_LAT_MIN = -1.023692
POLY_LAT_MAX = -0.842803
POLY_LON_MIN =  36.241736
POLY_LON_MAX =  36.421436

# =============================================================================
#  STUDY PERIOD
# =============================================================================
START_DATE = "2023-01-01"
END_DATE   = "2023-12-31"

START_DT = "2023-01-01T00:00:00Z"
END_DT   = "2023-12-31T23:59:59Z"

# =============================================================================
#  REGIONAL DOMAIN  (±5 degrees around site for GEOS-Chem and satellite data)
# =============================================================================
DOMAIN = {
    "lat_min": -5.0,
    "lat_max":  5.0,
    "lon_min": 32.0,
    "lon_max": 42.0,
}

# Bounding box string for NASA CMR API queries
BBOX = (
    f"{DOMAIN['lon_min']},"
    f"{DOMAIN['lat_min']},"
    f"{DOMAIN['lon_max']},"
    f"{DOMAIN['lat_max']}"
)

# WKT polygon for Copernicus CDSE API
BBOX_WKT = (
    f"POLYGON(("
    f"{DOMAIN['lon_min']} {DOMAIN['lat_min']},"
    f"{DOMAIN['lon_max']} {DOMAIN['lat_min']},"
    f"{DOMAIN['lon_max']} {DOMAIN['lat_max']},"
    f"{DOMAIN['lon_min']} {DOMAIN['lat_max']},"
    f"{DOMAIN['lon_min']} {DOMAIN['lat_min']}"
    f"))"
)

# =============================================================================
#  LOCAL DATA DIRECTORIES
# =============================================================================
DATA_ROOT    = "./data"
DIR_MERRA2   = f"{DATA_ROOT}/MERRA2"
DIR_OCO2     = f"{DATA_ROOT}/OCO2"
DIR_TROPOMI  = f"{DATA_ROOT}/TROPOMI"
DIR_GROUND   = f"{DATA_ROOT}/ground_measurements"
DIR_OUTPUTS  = f"{DATA_ROOT}/outputs"
DIR_FIGURES  = f"{DATA_ROOT}/figures"

# =============================================================================
#  CREDENTIALS
# =============================================================================

# NASA Earthdata — register at: https://urs.earthdata.nasa.gov/users/new
# After registering, approve GES DISC at:
# https://urs.earthdata.nasa.gov/approve_app?client_id=ijpRZvb9qeKCK5ctsn75Tg
EARTHDATA_USER = "John_KIMKE"
EARTHDATA_PASS = "225322532253J_k"

# Copernicus Data Space — register at: https://dataspace.copernicus.eu
# NOTE: Old s5phub.copernicus.eu is SHUT DOWN — use the link above
COPERNICUS_USER = "johnnduati600@gmail.com"
COPERNICUS_PASS = "D_#rWwXRj4DGA/*"

# =============================================================================
#  GEOS-CHEM SETTINGS
# =============================================================================
GC_MET        = "MERRA2"
GC_RESOLUTION = "4x5"

# Olkaria emission estimates (replace with your ground measurement values)
EMISSION_CO2_KG_S = 3.274    # ~283 tCO2/day
EMISSION_CH4_KG_S = 0.012    # Estimated thermogenic CH4

# =============================================================================
#  PLOTTING DEFAULTS
# =============================================================================
FIG_DPI      = 150
FIG_FORMAT   = "png"
COLORMAP_CO2 = "RdYlBu_r"
COLORMAP_CH4 = "YlOrRd"
