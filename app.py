#!/usr/bin/env python3
"""
IvoryOS Main Script
Generated: 2026-06-04T22:51:49.653Z
"""
from ivoryos.config import DemoConfig
from scripts.sim_instruments import SimRoboticArm
from scripts.sim_instruments import SimStirPlate
from ivorysos_colour_match_sdl.sdl import ColourMatcher
from scripts.sim_instruments import SimCappingStation
from scripts.sim_instruments import SimLiquidAdditionStation
from colour_match_web.plugin import colour_match_sdl_bp
import ivoryos
from ivoryos.config import DemoConfig
# Initialize hardware
try:
    robotic_arm = SimRoboticArm()
    stir_plate = SimStirPlate()
    colour_matcher = ColourMatcher()
    capping_station = SimCappingStation()
    liquid_addition_station = SimLiquidAdditionStation()
except Exception as e:
    print(f"Failed to initialize hardware: {e}. Connect them in the web interface or try again.")

# Start IvoryOS web interface
if __name__ == "__main__":
    ivoryos.run(__name__, port=7860, config=DemoConfig(), blueprint_plugins=[colour_match_sdl_bp])
