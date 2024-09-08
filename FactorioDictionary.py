import math
from fractions import Fraction
recipes = {
 "wooden_chest": {
  "input": [("wood", 2)],
  "output": [("wooden_chest", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "iron_chest": {
  "input": [("iron_plate", 8)],
  "output": [("iron_chest", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "steel_chest": {
  "input": [("steel_plate", 8)],
  "output": [("steel_chest", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "storage_tank": {
  "input": [("iron_plate", 20), ("steel_plate", 5)],
  "output": [("storage_tank", 1)],
  "time": 3,
  "type": "crafting"
 },
 "transport_belt": {
  "input": [("iron_plate", 1), ("iron_gear_wheel", 1)],
  "output": [("transport_belt", 2)],
  "time": 0.5,
  "type": "crafting"
 },
 "fast_transport_belt": {
  "input": [("transport_belt", 1), ("iron_gear_wheel", 5)],
  "output": [("fast_transport_belt", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "express_transport_belt": {
  "input": [("fast_transport_belt", 1), ("lubricant", 20), ("iron_gear_wheel", 10)],
  "output": [("express_transport_belt", 1)],
  "time": 0.5,
  "type": "liquid_crafting"
 },
 "underground_belt": {
  "input": [("transport_belt", 5), ("iron_plate", 10)],
  "output": [("underground_belt", 2)],
  "time": 1,
  "type": "crafting"
 },
 "fast_underground_belt": {
  "input": [("underground_belt", 2), ("iron_gear_wheel", 40)],
  "output": [("fast_underground_belt", 2)],
  "time": 2,
  "type": "crafting"
 },
 "express_underground_belt": {
  "input": [("fast_underground_belt", 2), ("lubricant", 40), ("iron_gear_wheel", 80)],
  "output": [("express_underground_belt", 2)],
  "time": 2,
  "type": "liquid_crafting"
 },
 "splitter": {
  "input": [("transport_belt", 4), ("iron_plate", 5), ("electronic_circuit", 5)],
  "output": [("", 1)],
  "time": 1,
  "type": "crafting"
 },
 "fast_splitter": {
  "input": [("splitter", 1), ("iron_gear_wheel", 10), ("electronic_circuit", 10)],
  "output": [("fast_splitter", 1)],
  "time": 2,
  "type": "crafting"
 },
 "express_splitter": {
  "input": [("fast_splitter", 1), ("lubricant", 80), ("iron_gear_wheel", 10), ("advanced_circuit", 10)],
  "output": [("express_splitter", 1)],
  "time": 2,
  "type": "liquid_crafting"
 },
 "burner_inserter": {
  "input": [("iron_plate", 1), ("iron_gear_wheel", 1)],
  "output": [("burner_inserter", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "inserter": {
  "input": [("iron_plate", 1), ("iron_gear_wheel", 1), ("electronic_circuit", 1)],
  "output": [("inserter", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "fast_inserter": {
  "input": [("inserter", 1), ("iron_plate", 2), ("electronic_circuit", 2)],
  "output": [("fast_inserter", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "long-handed_inserter": {
  "input": [("inserter", 1), ("iron_plate", 1), ("iron_gear_wheel", 1)],
  "output": 1,
  "time": 0.5,
  "type": "crafting"
 },
 "filter_inserter": {
  "input": [("fast_inserter", 1), ("electronic_circuit", 4)],
  "output": [("filter_inserter", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "stack_inserter": {
  "input": [("fast_splitter", 1), ("iron_gear_wheel", 15), ("electronic_circuit", 15), ("advanced_circuit", 1)],
  "output": [("stack_inserter", 1)],
  "time": 0.5,
   "type": "crafting"
 },
 "stack_filter_inserter": {
  "input": [("stack_inserter", 1), ("electronic_circuit", 5)],
  "output": [("stack_filter_inserter", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "small_electric_pole": {
  "input": [("wood", 1), ("copper_cable", 2)],
  "output": [("small_electric_pole", 2)],
  "time": 0.5,
  "type": "crafting"
 },
 "medium_electric_pole": {
  "input": [("copper_plate", 2), ("steel_plate", 2), ("iron_stick", 4)],
  "output": [("medium_electric_pole", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "big_electric_pole": {
  "input": [("copper_plate", 5), ("steel_plate", 5), ("iron_stick", 8)],
  "output": [("big_electric_pole", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "substation": {
  "input": [("copper_plate", 5), ("steel_plate", 10), ("advanced_circuit", 5)],
  "output": [("substation", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "pipe": {
  "input": [("iron_plate", 1)],
  "output": [("pipe", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "pipe_to_ground": {
  "input": [("pipe", 10), ("iron_plate", 5)],
  "output": [("pipe_to_ground", 2)],
  "time": 0.5,
  "type": "crafting"
 },
 "pump": {
  "input": [("pipe", 1), ("steel_plate", 1), ("engine_unit", 1)],
  "output": [("pump", 1)],
  "time": 2,
    "type": "crafting"
 },
 "rail": {
  "input": [("stone", 1), ("steel_plate", 1), ("iron_stick", 1)],
  "output": [("rail", 2)],
  "time": 0.5,
  "type": "crafting"
 },
 "train_station": {
  "input": [("iron_plate", 6), ("steel_plate", 3), ("iron_stick", 6), ("electronic_circuit", 5)],
  "output": [("train_station", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "rail_signal": {
  "input": [("iron_plate", 5), ("electronic_circuit", 1)],
  "output": [("rail_signal", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "rail_chain_signal": {
  "input": [("iron_plate", 5), ("electronic_circuit", 1)],
  "output": [("rail_chain_signal", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "locomotive": {
  "input": [("steel_plate", 30), ("electronic_circuit", 10), ("engine_unit", 20)],
  "output": [("locomotive", 1)],
  "time": 4,
  "type": "crafting"
 },
 "cargo_wagon": {
  "input": [("iron_plate", 20), ("steel_plate", 20), ("iron_gear_wheel", 10)],
  "output": [("cargo_wagon", 1)],
  "time": 1,
  "type": "crafting"
 },
 "fluid_wagon": {
  "input": [("storage_tank", 1), ("pipe", 8), ("steel_plate", 16), ("iron_gear_wheel", 10)],
  "output": [("fluid_wagon", 1)],
  "time": 1.5,
  "type": "crafting"
 },
 "artillery_wagon": {
  "input": [("pipe", 16), ("steel_plate", 40), ("iron_gear_wheel", 10), ("advanced_circuit", 20), ("engine_unit", 64)],
  "output": [("artillery_wagon", 1)],
  "time": 4,
   "type": "crafting"
 },
 "car": {
  "input": [("iron_plate", 20), ("steel_plate", 5), ("engine_unit", 8)],
  "output": [("car", 1)],
  "time": 2,
  "type": "crafting"
 },
 "tank": {
  "input": [("steel_plate", 50), ("iron_gear_wheel", 15), ("advanced_circuit", 10), ("engine_unit", 32)],
  "output": [("tank", 1)],
  "time": 5,
  "type": "crafting"
 },
 "spidertron": {
  "input": [("efficiency_module_3", 2), ("rocket_control_unit", 16), ("low_density_structure", 150), ("rocket_launcher", 4), ("portable_fusion_reactor", 2), ("exoskeleton", 4), ("radar", 2), ("raw_fish", 1)],
  "output": [("spidertron", 1)],
  "time": 10,
  "type": "crafting"
 },
 "spidertron_remote": {
  "input": [("rocket_control_unit", 1), ("radar", 1)],
  "output": [("spidertron_remote", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "logistic_robot": {
  "input": [("advanced_circuit", 2), ("flying_robot_frame", 1)],
  "output": [("logistic_robot", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "construction_robot": {
  "input": [("electronic_circuit", 2), ("flying_robot_frame", 1)],
  "output": [("construction_robot", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "active_provider_chest": {
  "input": [("steel_chest", 1), ("electronic_circuit", 3), ("advanced_circuit", 1)],
  "output": [("active_provider_chest", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "passive_provider_chest": {
  "input": [("steel_chest", 1), ("electronic_circuit", 3), ("advanced_circuit", 1)],
  "output": [("passive_provider_chest", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "storage_chest": {
  "input": [("steel_chest", 1), ("electronic_circuit", 3), ("advanced_circuit", 1)],
  "output": [("storage_chest", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "buffer_chest": {
  "input": [("steel_chest", 1), ("electronic_circuit", 3), ("advanced_circuit", 1)],
  "output": [("buffer_chest", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "requester_chest": {
  "input": [("steel_chest", 1), ("electronic_circuit", 3), ("advanced_circuit", 1)],
  "output": [("requester_chest", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "roboport": {
  "input": [("steel_plate", 45), ("iron_gear_wheel", 45), ("advanced_circuit", 45)],
  "output": [("roboport", 1)],
  "time": 5,
  "type": "crafting"
 },
 "lamp": {
  "input": [("iron_plate", 1), ("copper_cable", 3), ("electronic_circuit", 1)],
  "output": [("lamp", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "red_wire": {
  "input": [("copper_cable", 1), ("electronic_circuit", 1)],
  "output": [("red_wire", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "green_wire": {
  "input": [("copper_cable", 1), ("electronic_circuit", 1)],
  "output": [("green_wire", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "arithmetic_combinator": {
  "input": [("copper_cable", 5), ("electronic_circuit", 5)],
  "output": [("arithmetic_combinator", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "decider_combinator": {
  "input": [("copper_cable", 5), ("electronic_circuit", 5)],
  "output": [("decider_combinator", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "constant_combinator": {
  "input": [("copper_cable", 5), ("electronic_circuit", 2)],
  "output": [("constant_combinator", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "power_switch": {
  "input": [("iron_plate", 5), ("copper_cable", 5), ("electronic_circuit", 2)],
  "output": [("power_switch", 1)],
  "time": 2,
   "type": "crafting"
 },
 "programmable_speaker": {
  "input": [("iron_plate", 3), ("copper_cable", 5), ("iron_stick", 4), ("electronic_circuit", 4)],
  "output": [("programmable_speaker", 1)],
  "time": 2,
  "type": "crafting"
 },
 "stone_brick": {
  "input": [("stone", 2)],
  "output": [("stone_brick", 1)],
  "time": 3.2,
  "type": "smelting"
 },
 "concrete": {
  "input": [("water", 100), ("iron_ore", 1), ("stone_brick", 5)],
  "output": [("concrete", 10)],
  "time": 10,
  "type": "liquid_crafting"
 },
 "hazard_concrete": {
  "input": [("concrete", 10)],
  "output": [("hazard_concrete", 10)],
  "time": 0.25,
  "type": "crafting"
 },
 "refined_concrete": {
  "input": [("water", 100), ("concrete", 20), ("steel_plate", 1), ("iron_stick", 8)],
  "output": [("refined_concrete", 10)],
  "time": 15,
  "type": "liquid_crafting"
 },
 "refined_hazed_concrete": {
  "input": [("refined_concrete", 10)],
  "output": [("refined_hazed_concrete", 10)],
  "time": 0.25,
  "type": "crafting"
 },
 "landfill": {
  "input": [("stone", 20)],
  "output": [("landfill", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "cliff_explosives": {
  "input": [("explosives", 10), ("empty_barrel", 1), ("grenade", 1)],
  "output": [("cliff_explosives", 1)],
  "time": 8,
  "type": "crafting"
 },
 "repair_pack": {
  "input": [("iron_gear_wheel", 2), ("electronic_circuit", 2)],
  "output": [("repair_pack", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "boiler": {
  "input": [("pipe", 4), ("stone_furnace", 1)],
  "output": [("boiler", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "steam_engine": {
  "input": [("pipe", 5), ("iron_plate", 10), ("iron_gear_wheel", 8)],
  "output": [("steam_engine", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "solar_panel": {
  "input": [("copper_plate", 5), ("steel_plate", 5), ("electronic_circuit", 15)],
  "output": [("solar_panel", 1)],
  "time": 10,
  "type": "crafting"
 },
 "accumulator": {
  "input": [("iron_plate", 2), ("battery", 5)],
  "output": [("accumulator", 1)],
  "time": 10
 },
 "nuclear_reactor": {
  "input": [("concrete", 500), ("copper_plate", 500), ("steel_plate", 500), ("advanced_circuit", 500)],
  "output": [("nuclear_reactor", 1)],
  "time": 8,
  "type": "crafting"
 },
 "heat_pipe": {
  "input": [("copper_plate", 20), ("steel_plate", 10)],
  "output": [("heat_pipe", 1)],
  "time": 1,
  "type": "crafting"
 },
 "heat_exchanger": {
  "input": [("pipe", 10), ("copper_plate", 100), ("steel_plate", 10)],
  "output": [("heat_exchanger", 1)],
  "time": 3,
  "type": "crafting"
 },
 "steam_turbine": {
  "input": [("pipe", 20), ("copper_plate", 50), ("iron_gear_wheel", 50)],
  "output": [("steam_turbine", 1)],
  "time": 3,
  "type": "crafting"
 },
 "burner_mining_drill": {
  "input": [("stone_furnace", 1), ("iron_plate", 3), ("iron_gear_wheel", 3)],
  "output": [("burner_mining_drill", 1)],
  "time": 2,
  "type": "crafting"
 },
 "electric_mining_drill": {
  "input": [("iron_plate", 10), ("iron_gear_wheel", 5), ("electronic_circuit", 3)],
  "output": [("electric_mining_drill", 1)],
  "time": 2,
   "type": "crafting"
 },
 "offshore_pump": {
  "input": [("pipe", 1), ("iron_gear_wheel", 1), ("electronic_circuit", 2)],
  "output": [("offshore_pump", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "pumpjack": {
  "input": [("pipe", 10), ("steel_plate", 5), ("iron_gear_wheel", 10), ("electronic_circuit", 5)],
  "output": [("pumpjack", 1)],
  "time": 5,
  "type": "crafting"
 },
 "stone_furnace": {
  "input": [("stone", 5)],
  "output": [("stone_furnace", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "steel_furnace": {
  "input": [("stone_brick", 10), ("steel_plate", 6)],
  "output": [("steel_furnace", 1)],
  "time": 3,
  "type": "crafting"
 },
 "electric_furnace": {
  "input": [("stone_brick", 10), ("steel_plate", 10), ("advanced_circuit", 5)],
  "output": [("electric_furnace", 1)],
  "time": 5,
  "type": "crafting"
 },
 "assembling_machine_1": {
  "input": [("iron_plate", 9), ("iron_gear_wheel", 5), ("electronic_circuit", 3)],
  "output": [("assembling_machine_1", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "assembling_machine_2": {
  "input": [("assembling_machine_1", 1), ("steel_plate", 2), ("iron_gear_wheel", 5), ("electronic_circuit", 3)],
  "output": [("assembling_machine_2", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "assembling_machine_3": {
  "input": [("assembling_machine_2", 2), ("speed_module", 4)],
  "output": [("assembling_machine_3", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "oil_refinery": {
  "input": [("pipe", 10), ("stone_brick", 10), ("steel_plate", 15), ("iron_gear_wheel", 10), ("electronic_circuit", 10)],
  "output": [("oil_refinery", 1)],
  "time": 8,
  "type": "crafting"
 },
 "chemical_plant": {
  "input": [("pipe", 5), ("steel_plate", 5), ("iron_gear_wheel", 5), ("electronic_circuit", 5)],
  "output": [("chemical_plant", 1)],
  "time": 5,
  "type": "crafting"
 },
 "centrifuge": {
  "input": [("concrete", 100), ("steel_plate", 50), ("iron_gear_wheel", 100), ("advanced_circuit", 100)],
  "output": [("centrifuge", 1)],
  "time": 4,
  "type": "crafting"
 },
 "lab": {
  "input": [("transport_belt", 4), ("iron_gear_wheel", 10), ("electronic_circuit", 10)],
  "output": [("lab", 1)],
  "time": 2,
  "type": "crafting"
 },
 "beacon": {
  "input": [("steel_plate", 10), ("copper_cable", 10), ("electronic_circuit", 20), ("advanced_circuit", 20)],
  "output": [("beacon", 1)],
  "time": 15,
  "type": "crafting"
 },
 "speed_module": {
  "input": [("electronic_circuit", 5), ("advanced_circuit", 5)],
  "output": [("speed_module", 1)],
  "time": 15,
   "type": "crafting"
 },
 "speed_module_2": {
  "input": [("speed_module", 4), ("advanced_circuit", 5), ("processing_unit", 5)],
  "output": [("speed_module_2", 1)],
  "time": 30,
  "type": "crafting"
 },
 "speed_module_3": {
  "input": [("speed_module_2", 5), ("advanced_circuit", 5), ("processing_unit", 5)],
  "output": [("speed_module_3", 1)],
  "time": 60,
  "type": "crafting"
 },
 "efficiency_module": {
  "input": [("electronic_circuit", 5), ("advanced_circuit", 5)],
  "output": [("efficiency_module", 1)],
  "time": 15,
  "type": "crafting"
 },
 "efficiency_module_2": {
  "input": [("efficiency_module", 4), ("advanced_circuit", 5), ("processing_unit", 5)],
  "output": [("efficiency_module_2", 1)],
  "time": 30,
  "type": "crafting"
 },
 "efficiency_module_3": {
  "input": [("efficiency_module_2", 5), ("advanced_circuit", 5), ("processing_unit", 5)],
  "output": [("efficiency_module_3", 1)],
  "time": 60,
  "type": "crafting"
 },
 "productivity_module": {
  "input": [("electronic_circuit", 5), ("advanced_circuit", 5)],
  "output": [("productivity_module", 1)],
  "time": 15,
  "type": "crafting"
 },
 "productivity_module_2": {
  "input": [("productivity_module", 4), ("advanced_circuit", 5), ("processing_unit", 5)],
  "output": [("productivity_module_2", 1)],
  "time": 30,
  "type": "crafting"
 },
 "productivity_module_3": {
  "input": [("productivity_module_2", 5), ("advanced_circuit", 5), ("processing_unit", 5)],
  "output": [("productivity_module_3", 1)],
  "time": 60,
  "type": "crafting"
 },
 "rocket_silo": {
  "input": [("pipe", 100), ("concrete", 1000), ("steel_plate", 1000), ("processing_unit", 200), ("electric_engine_unit", 200)],
  "output": [("rocket_silo", 1)],
  "time": 30,
  "type": "crafting"
 },
 "satellite": {
  "input": [("solar_panel", 100), ("accumulator", 100), ("processing_unit", 100), ("low_density_structure", 100), ("rocket_fuel", 50), ("radar", 5)],
  "output": [("satellite", 1)],
  "time": 5,
  "type": "crafting"
 },
 "heavy_oil": {
  "input": [("crude_oil", 100), ("water", 50)],
  "output": [("heavy_oil", 25)],
  "time": 5,
  "productivity_allowed": 1,
  "type": "refining"
 },
 "light_oil": {
  "input": [("crude_oil", 100), ("water", 50)],
  "output": [("light_oil", 45)],
  "time": 5,
  "productivity_allowed": 1,
  "type": "refining"
 },
 "lubricant": {
  "input": [("heavy_oil", 10)],
  "output": [("lubricant", 10)],
  "time": 1,
  "productivity_allowed": 1,
  "type": "chemical"
 },
 "petroleum_gas": {
  "input": [("crude_oil", 100), ("water", 50)],
  "output": [("petroleum_gas", 55)],
  "time": 5,
  "productivity_allowed": 1,
  "type": "refining"
 },
 "sulfuric_acid": {
  "input": [("water", 100), ("iron_plate", 1), ("sulfur", 5)],
  "output": [("sulfuric_acid", 50)],
  "time": 1,
  "productivity_allowed": 1,
  "type": "chemical"
 },
 "iron_plate": {
  "input": [("iron_ore", 1)],
  "output": [("iron_plate", 1)],
  "time": 3.2,
  "productivity_allowed": 1,
  "type": "smelting"
 },
 "copper_plate": {
  "input": [("copper_ore", 1)],
  "output": [("copper_plate", 1)],
  "time": 3.2,
  "productivity_allowed": 1,
  "type": "smelting"
 },
 "solid_fuel": {
  "input": [("light_oil", 10)],
  "output": [("solid_fuel", 1)],
  "time": 2,
  "productivity_allowed": 1,
  "type": "chemical"
 },
 "steel_plate": {
  "input": [("iron_plate", 5)],
  "output": [("steel_plate", 1)],
  "time": 16,
  "productivity_allowed": 1,
  "type": "smelting"
 },
 "plastic_bar": {
  "input": [("coal", 1), ("petroleum_gas", 20)],
  "output": [("plastic_bar", 2)],
  "time": 1,
  "productivity_allowed": 1,
  "type": "chemical"
 },
 "sulfur": {
  "input": [("water", 30), ("petroleum_gas", 30)],
  "output": [("sulfur", 2)],
  "time": 1,
  "productivity_allowed": 1,
  "type": "chemical"
 },
 "battery": {
  "input": [("sulfuric_acid", 20), ("iron_plate", 1), ("copper_plate", 1)],
  "output": [("battery", 1)],
  "time": 4,
  "productivity_allowed": 1,
  "type": "chemical"
 },
 "explosives": {
  "input": [("water", 10), ("coal", 1), ("sulfur", 1)],
  "output": [("explosives", 2)],
  "time": 4,
  "productivity_allowed": 1,
  "type": "chemical"
 },
 "uranium-235": {
  "input": [("uranium-238", 3)],
  "output": 1,
  "time": 60,
  "productivity_allowed": 1,
  "type": "nuclear"
 },
 "uranium-238": {
  "input": [("uranium_ore", 10)],
  "output": 1,
  "time": 12,
  "productivity_allowed": 1,
  "type": "nuclear"
 },
 "copper_cable": {
  "input": [("copper_plate", 1)],
  "output": [("copper_cable", 2)],
  "time": 0.5,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "iron_stick": {
  "input": [("iron_plate", 1)],
  "output": [("iron_stick", 2)],
  "time": 0.5,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "iron_gear_wheel": {
  "input": [("iron_plate", 2)],
  "output": [("iron_gear_wheel", 1)],
  "time": 0.5,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "empty_barrel": {
  "input": [("steel_plate", 1)],
  "output": [("empty_barrel", 1)],
  "time": 1,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "electronic_circuit": {
  "input": [("iron_plate", 1), ("copper_cable", 3)],
  "output": [("electronic_circuit", 1)],
  "time": 0.5,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "advanced_circuit": {
  "input": [("plastic_bar", 2), ("copper_cable", 4), ("electronic_circuit", 2)],
  "output": [("advanced_circuit", 1)],
  "time": 6,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "processing_unit": {
  "input": [("sulfuric_acid", 5), ("electronic_circuit", 20), ("advanced_circuit", 2)],
  "output": [("processing_unit", 1)],
  "time": 10,
  "productivity_allowed": 1,
  "type": "liquid_crafting"
 },
 "engine_unit": {
  "input": [("pipe", 2), ("steel_plate", 1), ("iron_gear_wheel", 1)],
  "output": [("engine_unit", 1)],
  "time": 10,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "electric_engine_unit": {
  "input": [("lubricant", 15), ("electronic_circuit", 2), ("engine_unit", 1)],
  "output": [("electric_engine_unit", 1)],
  "time": 10,
  "productivity_allowed": 1,
  "type": "liquid_crafting"
 },
 "flying_robot_frame": {
  "input": [("steel_plate", 1), ("battery", 2), ("electronic_circuit", 3), ("electric_engine_unit", 1)],
  "output": [("flying_robot_frame", 1)],
  "time": 20,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "rocket_part": {
  "input": [("rocket_control_unit", 10), ("low_density_structure", 10), ("rocket_fuel", 10)],
  "output": [("rocket_part", 1)],
  "time": 3,
  "productivity_allowed": 1,
  "type": "rockets"
 },
 "rocket_control_unit": {
  "input": [("speed_module", 1), ("processing_unit", 1)],
  "output": [("rocket_control_unit", 1)],
  "time": 30,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "low_density_structure": {
  "input": [("copper_plate", 20), ("plastic_bar", 5), ("steel_plate", 2)],
  "output": [("low_density_structure", 1)],
  "time": 20,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "rocket_fuel": {
  "input": [("light_oil", 10), ("solid_fuel", 10)],
  "output": [("rocket_fuel", 1)],
  "time": 30,
  "productivity_allowed": 1,
  "type": "liquid_crafting"
 },
 "nuclear_fuel": {
  "input": [("uranium-235", 1), ("rocket_fuel", 1)],
  "output": [("nuclear_fuel", 1)],
  "time": 90,
  "productivity_allowed": 1,
  "type": "nuclear"
 },
 "uranium_fuel_cell": {
  "input": [("iron_plate", 10), ("uranium-235", 1), ("uranium-238", 19)],
  "output": [("uranium_fuel_cell", 10)],
  "time": 10,
  "productivity_allowed": 1,
  "type": "nuclear"
 },
 "automation_science_pack": {
  "input": [("copper_plate", 1), ("iron_gear_wheel", 1)],
  "output": [("automation_science_pack", 1)],
  "time": 5,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "logistic_science_pack": {
  "input": [("transport_belt", 1), ("inserter", 1)],
  "output": [("logistic_science_pack", 1)],
  "time": 6,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "military_science_pack": {
  "input": [("piercing_rounds_magazine", 1), ("grenade", 1), ("wall", 2)],
  "output": [("military_science_pack", 2)],
  "time": 10,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "chemical_science_pack": {
  "input": [("sulfur", 1), ("advanced_circuit", 3), ("engine_unit", 2)],
  "output": [("chemical_science_pack", 2)],
  "time": 24,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "production_science_pack": {
  "input": [("rail", 30), ("electric_furnace", 1), ("productivity_module", 1)],
  "output": [("production_science_pack", 3)],
  "time": 21,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "utility_science_pack": {
  "input": [("processing_unit", 2), ("flying_robot_frame", 1), ("low_density_structure", 3)],
  "output": [("utility_science_pack", 3)],
  "time": 21,
  "productivity_allowed": 1,
  "type": "crafting"
 },
 "pistol": {
  "input": [("iron_plate", 5), ("copper_plate", 5)],
  "output": [("pistol", 1)],
  "time": 5,
  "type": "crafting"
 },
 "submachine_gun": {
  "input": [("iron_plate", 10), ("copper_plate", 5), ("iron_gear_wheel", 10)],
  "output": [("submachine_gun", 1)],
  "time": 10,
  "type": "crafting"
 },
 "shotgun": {
  "input": [("wood", 5), ("iron_plate", 15), ("copper_plate", 10), ("iron_gear_wheel", 5)],
  "output": [("shotgun", 1)],
  "time": 10,
  "type": "crafting"
 },
 "combat_shotgun": {
  "input": [("wood", 10), ("copper_plate", 10), ("steel_plate", 15), ("iron_gear_wheel", 5)],
  "output": [("combat_shotgun", 1)],
  "time": 10,
  "type": "crafting"
 },
 "rocket_launcher": {
  "input": [("iron_plate", 5), ("iron_gear_wheel", 5), ("electronic_circuit", 5)],
  "output": [("rocket_launcher", 1)],
  "time": 10,
  "type": "crafting"
 },
 "flamethrower": {
  "input": [("steel_plate", 5), ("iron_gear_wheel", 10)],
  "output": [("flamethrower", 1)],
  "time": 10,
  "type": "crafting"
 },
 "land_mine": {
  "input": [("steel_plate", 1), ("explosives", 2)],
  "output": [("land_mine", 4)],
  "time": 5,
  "type": "crafting"
 },
 "firearm_magazine": {
  "input": [("iron_plate", 4)],
  "output": [("firearm_magazine", 1)],
  "time": 1,
  "type": "crafting"
 },
 "piercing_rounds_magazine": {
  "input": [("copper_plate", 5), ("steel_plate", 1), ("firearm_magazine", 1)],
  "output": [("piercing_rounds_magazine", 1)],
  "time": 3,
  "type": "crafting"
 },
 "uranium_rounds_magazine": {
  "input": [("uranium-238", 1), ("piercing_rounds_magazine", 1)],
  "output": [("uranium_rounds_magazine", 1)],
  "time": 10,
  "type": "crafting"
 },
 "shotgun_shells": {
  "input": [("iron_plate", 2), ("copper_plate", 2)],
  "output": [("shotgun_shells", 1)],
  "time": 3,
  "type": "crafting"
 },
 "piercing_shotgun_shells": {
  "input": [("copper_plate", 5), ("steel_plate", 2), ("shotgun_shells", 2)],
  "output": [("piercing_shotgun_shells", 1)],
  "time": 8,
  "type": "crafting"
 },
 "cannon_shell": {
  "input": [("steel_plate", 2), ("plastic_bar", 2), ("explosives", 1)],
  "output": [("cannon_shell", 1)],
  "time": 8,
  "type": "crafting"
 },
 "explosive_cannon_shell": {
  "input": [("steel_plate", 2), ("plastic_bar", 2), ("explosives", 2)],
  "output": [("explosive_cannon_shell", 1)],
  "time": 8,
  "type": "crafting"
 },
 "uranium_cannon_shell": {
  "input": [("uranium-238", 1), ("cannon_shell", 1)],
  "output": [("uranium_cannon_shell", 1)],
  "time": 12,
  "type": "crafting"
 },
 "explosive_uranium_cannon_shell": {
  "input": [("uranium-238", 1), ("explosive_cannon_shell", 1)],
  "output": [("explosive_uranium_cannon_shell", 1)],
  "time": 12,
  "type": "crafting"
 },
 "artillery_shell": {
  "input": [("explosives", 8), ("explosive_cannon_shell", 4), ("radar", 1)],
  "output": [("artillery_shell", 1)],
  "time": 15,
  "type": "crafting"
 },
 "rocket": {
  "input": [("iron_plate", 2), ("explosives", 1), ("electronic_circuit", 1)],
  "output": [("rocket", 1)],
  "time": 8,
  "type": "crafting"
 },
 "explosive_rocket": {
  "input": [("explosives", 2), ("rocket", 1)],
  "output": [("explosive_rocket", 1)],
  "time": 8,
  "type": "crafting"
 },
 "atomic_bomb": {
  "input": [("explosives", 10), ("uranium-235", 30), ("rocket_control_unit", 10)],
  "output": [("atomic_bomb", 1)],
  "time": 50,
  "type": "crafting"
 },
 "flamethrower_ammo": {
  "input": [("crude_oil", 100), ("steel_plate", 5)],
  "output": [("flamethrower_ammo", 1)],
  "time": 6,
  "type": "chemical"
 },
 "grenade": {
  "input": [("coal", 10), ("iron_plate", 5)],
  "output": [("grenade", 1)],
  "time": 8,
  "type": "crafting"
 },
 "cluster_grenade": {
  "input": [("steel_plate", 5), ("explosives", 5), ("grenade", 7)],
  "output": [("cluster_grenade", 1)],
  "time": 8,
  "type": "crafting"
 },
 "poison_capsule": {
  "input": [("coal", 10), ("steel_plate", 3), ("electronic_circuit", 3)],
  "output": [("poison_capsule", 1)],
  "time": 8,
  "type": "crafting"
 },
 "slowdown_capsule": {
  "input": [("coal", 5), ("steel_plate", 2), ("electronic_circuit", 2)],
  "output": [("slowdown_capsule", 1)],
  "time": 8,
   "type": "crafting"
 },
 "defender_capsule": {
  "input": [("iron_gear_wheel", 3), ("electronic_circuit", 3), ("piercing_rounds_magazine", 3)],
  "output": [("defender_capsule", 1)],
  "time": 8,
  "type": "crafting"
 },
 "distractor_capsule": {
  "input": [("advanced_circuit", 3), ("defender_capsule", 1)],
  "output": [("distractor_capsule", 1)],
  "time": 15,
  "type": "crafting"
 },
 "destroyer_capsule": {
  "input": [("speed_module", 1), ("distractor_capsule", 4)],
  "output": [("destroyer_capsule", 1)],
  "time": 15,
  "type": "crafting"
 },
 "light_armor": {
  "input": [("iron_plate", 40)],
  "output": [("light_armor", 1)],
  "time": 3,
  "type": "crafting"
 },
 "heavy_armor": {
  "input": [("copper_plate", 100), ("steel_plate", 50)],
  "output": [("heavy_armor", 1)],
  "time": 8,
  "type": "crafting"
 },
 "modular_armor": {
  "input": [("steel_plate", 50), ("advanced_circuit", 30)],
  "output": [("modular_armor", 1)],
  "time": 15,
  "type": "crafting"
 },
 "power_armor": {
  "input": [("steel_plate", 40), ("processing_unit", 40), ("electric_engine_unit", 20)],
  "output": [("power_armor", 1)],
  "time": 20,
  "type": "crafting"
 },
 "power_armor_mk2": {
  "input": [("speed_module_2", 25), ("efficiency_module_2", 25), ("engine_unit", 60), ("electric_engine_unit", 40), ("low_density_structure", 30)],
  "output": [("power_armor_mk2", 1)],
  "time": 25,
  "type": "crafting"
 },
 "portable_solar_panel": {
  "input": [("solar_panel", 1), ("steel_plate", 5), ("advanced_circuit", 2)],
  "output": [("portable_solar_panel", 1)],
  "time": 10,
  "type": "crafting"
 },
 "portable_fusion_reactor": {
  "input": [("processing_unit", 200), ("low_density_structure", 50)],
  "output": [("portable_fusion_reactor", 1)],
  "time": 10,
  "type": "crafting"
 },
 "personal_battery": {
  "input": [("steel_plate", 10), ("battery", 5)],
  "output": [("personal_battery", 1)],
  "time": 10,
  "type": "crafting"
 },
 "personal_battery_mk2": {
  "input": [("processing_unit", 15), ("low_density_structure", 5), ("personal_battery", 10)],
  "output": [("personal_battery_mk2", 1)],
  "time": 10,
  "type": "crafting"
 },
 "belt_immunity_equipment": {
  "input": [("steel_plate", 10), ("advanced_circuit", 5)],
  "output": [("belt_immunity_equipment", 1)],
  "time": 10,
  "type": "crafting"
 },
 "exoskeleton": {
  "input": [("steel_plate", 20), ("processing_unit", 10), ("electric_engine_unit", 30)],
  "output": [("exoskeleton", 1)],
  "time": 10,
  "type": "crafting"
 },
 "personal_roboport": {
  "input": [("steel_plate", 20), ("battery", 45), ("iron_gear_wheel", 40), ("advanced_circuit", 10)],
  "output": [("personal_roboport", 1)],
  "time": 10,
  "type": "crafting"
 },
 "personal_roboport_mk2": {
  "input": [("processing_unit", 100), ("low_density_structure", 20), ("personal_roboport", 5)],
  "output": [("personal_roboport_mk2", 1)],
  "time": 20,
  "type": "crafting"
 },
 "nightvision": {
  "input": [("steel_plate", 10), ("advanced_circuit", 5)],
  "output": [("nightvision", 1)],
  "time": 10,
  "type": "crafting"
 },
 "energy_shield": {
  "input": [("steel_plate", 10), ("advanced_circuit", 5)],
  "output": [("energy_shield", 1)],
  "time": 10,
  "type": "crafting"
 },
 "energy_shield_mk2": {
  "input": [("processing_unit", 5), ("low_density_structure", 5), ("energy_shield", 10)],
  "output": [("energy_shield_mk2", 1)],
  "time": 10,
  "type": "crafting"
 },
 "personal_laser_defense": {
  "input": [("processing_unit", 20), ("low_density_structure", 5), ("laser_turret", 5)],
  "output": [("personal_laser_defense", 1)],
  "time": 10,
  "type": "crafting"
 },
 "discharge_defense": {
  "input": [("steel_plate", 20), ("processing_unit", 5), ("laser_turret", 10)],
  "output": [("discharge_defense", 1)],
  "time": 10,
  "type": "crafting"
 },
 "discharge_defense_remote": {
  "input": [("electronic_circuit", 1)],
  "output": [("discharge_defense_remote", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "wall": {
  "input": [("stone_brick", 5)],
  "output": [("wall", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "gate": {
  "input": [("steel_plate", 2), ("electronic_circuit", 2), ("wall", 1)],
  "output": [("gate", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "gun_turret": {
  "input": [("iron_plate", 20), ("copper_plate", 10), ("iron_gear_wheel", 10)],
  "output": [("gun_turret", 1)],
  "time": 8,
  "type": "crafting"
 },
 "laser_turret": {
  "input": [("steel_plate", 20), ("battery", 12), ("electronic_circuit", 20)],
  "output": [("laser_turret", 1)],
  "time": 20,
  "type": "crafting"
 },
 "flamethrower_turret": {
  "input": [("pipe", 10), ("steel_plate", 30), ("iron_gear_wheel", 15), ("engine_unit", 5)],
  "output": [("flamethrower_turret", 1)],
  "time": 20,
  "type": "crafting"
 },
 "artillery_turret": {
  "input": [("concrete", 60), ("steel_plate", 60), ("iron_gear_wheel", 40), ("advanced_circuit", 20)],
  "output": [("artillery_turret", 1)],
  "time": 40,
  "type": "crafting"
 },
 "artillery_targeting_remote": {
  "input": [("processing_unit", 1), ("radar", 1)],
  "output": [("artillery_targeting_remote", 1)],
  "time": 0.5,
  "type": "crafting"
 },
 "radar": {
  "input": [("iron_plate", 10), ("iron_gear_wheel", 5), ("electronic_circuit", 5)],
  "output": [("radar", 1)],
  "time": 0.5,
  "type": "crafting"
 }
}

machines = {
    "assembling_machine_1": {
        "module_slots": 0,
        "crafting_speed": 0.5,
        "energy_consumption": 75000,
        "drain": 2500,
        "energy_type": "electric",
        "beacons": 12
    },
    "assembling_machine_2": {
        "module_slots": 2,
        "crafting_speed": 0.75,
        "energy_consumption": 150000,
        "drain": 5000,
        "energy_type": "electric",
        "beacons": 12
    },
    "assembling_machine_3": {
        "module_slots": 4,
        "crafting_speed": 1.25,
        "energy_consumption": 375000,
        "drain": 12500,
        "energy_type": "electric",
        "beacons": 12
    },
    "stone_furnace": {
        "module_slots": 0,
        "crafting_speed": 1,
        "energy_consumption": 90000,
        "energy_type": "burner",
        "beacons": 0
    },
    "steel_furnace": {
        "module_slots": 0,
        "crafting_speed": 2,
        "energy_consumption": 90000,
        "energy_type": "burner",
        "beacons": 0
    },
    "electric_furnace": {
        "module_slots": 2,
        "crafting_speed": 2,
        "energy_consumption": 180000,
        "drain": 6000,
        "energy_type": "electric",
        "beacons": 12
    },
    "chemical_plant": {
        "module_slots": 3,
        "crafting_speed": 1,
        "energy_consumption": 210000,
        "drain": 7000,
        "energy_type": "electric",
        "beacons": 12
    },
    "oil_refinery": {
        "module_slots": 3,
        "crafting_speed": 1,
        "energy_consumption": 420000,
        "drain": 14000,
        "energy_type": "electric",
        "beacons": 16
    },
    "rocket_silo": {
        "module_slots": 4,
        "crafting_speed": 1,
        "energy_consumption": 4000000,
        "drain": 0,
        "energy_type": "electric",
        "beacons": 20
    },
    "centrifuge": {
        "module_slots": 2,
        "crafting_speed": 1,
        "energy_consumption": 350000,
        "drain": 11600,
        "energy_type": "electric",
        "beacons": 12
    }
}

machinesP = {
    1: {
        "assembling_machine": {
            "name": "assembling_machine_1",
            "crafting_speed": 0.5,
            "crafting_type": ["crafting"],
            "max_inserters": 12
        },
        "furnace": {
            "name": "stone_furnace",
            "crafting_speed": 1,
            "crafting_type": ["smelting"],
            "max_inserters": 8
        },
        "chemical_plant": {
            "name": "chemical_plant",
            "crafting_speed": 1,
            "crafting_type": ["chemical"],
            "max_inserters": 12
        },
        "oil_refinery": {
            "name": "oil_refinery",
            "crafting_speed": 1,
            "crafting_type": ["refining"],
            "max_inserters": 20
        },
        "centrifuge": {
            "name": "centrifuge",
            "crafting_speed": 1,
            "crafting_type": ["nuclear"],
            "max_inserters": 12
        },
        "rocket_silo": {
            "name": "rocket_silo",
            "crafting_speed": 1,
            "crafting_type": ["rockets"],
            "max_inserters": 36
        }
    },
    2: {
        "assembling_machine": {
            "name": "assembling_machine_2",
            "crafting_speed": 0.75,
            "crafting_type": ["crafting", "liquid_crafting"],
            "max_inserters": 12
        },
        "furnace": {
            "name": "steel_furnace",
            "crafting_speed": 2,
            "crafting_type": ["smelting"],
            "max_inserters": 8
        },
        "chemical_plant": {
            "name": "chemical_plant",
            "crafting_speed": 1,
            "crafting_type": ["chemical"],
            "max_inserters": 12
        },
        "oil_refinery": {
            "name": "oil_refinery",
            "crafting_speed": 1,
            "crafting_type": ["refining"],
            "max_inserters": 20
        },
        "centrifuge": {
            "name": "centrifuge",
            "crafting_speed": 1,
            "crafting_type": ["nuclear"],
            "max_inserters": 12
        },
        "rocket_silo": {
            "name": "rocket_silo",
            "crafting_speed": 1,
            "crafting_type": ["rockets"],
            "max_inserters": 36
        }
    },
    3: {
        "assembling_machine": {
            "name": "assembling_machine_3",
            "crafting_speed": 1.25,
            "crafting_type": ["crafting", "liquid_crafting"],
            "max_inserters": 12
        },
        "furnace": {
            "name": "electric_furnace",
            "crafting_speed": 2,
            "crafting_type": ["smelting"],
            "max_inserters": 8
        },
        "chemical_plant": {
            "name": "chemical_plant",
            "crafting_speed": 1,
            "crafting_type": ["chemical"],
            "max_inserters": 12
        },
        "oil_refinery": {
            "name": "oil_refinery",
            "crafting_speed": 1,
            "crafting_type": ["refining"],
            "max_inserters": 20
        },
        "centrifuge": {
            "name": "centrifuge",
            "crafting_speed": 1,
            "crafting_type": ["nuclear"],
            "max_inserters": 12
        },
        "rocket_silo": {
            "name": "rocket_silo",
            "crafting_speed": 1,
            "crafting_type": ["rockets"],
            "max_inserters": 36
        }
    }
}

fuel = {
    "wood": 2000000,
    "coal": 4000000,
    "solid_fuel": 12000000,
    "rocket_fuel": 100000000,
    "nuclear_fuel": 1200000000,
    "uranium_fuel_cell": 8000000000,
}

inserterSpeeds = [0.83, 2.31, 4.29]
beltSpeeds = [15, 30, 45]



def formatT(text):
    return text.replace("_"," ").title()

def p(text):
    return print(text)

def printRecipe(recipeName):
    if recipeName not in recipes:
        return p(f"Error: Invalid Item, try:\n{recipes.keys()}")

    i = recipes[recipeName]["input"]
    o = recipes[recipeName]["output"]
    t = recipes[recipeName]["time"]
    Y = recipes[recipeName]["type"]
    p("Recipe for " + formatT(recipeName) + ":\n" + "  Ingredients:")

    for ingredient, amount in i:
        p(formatT(f"    {amount}x {ingredient}"))

    p("  Products:")

    for ingredient, amount in o:
        p(formatT(f"    {amount}x {ingredient}"))

    p(f"  Recipe Time: {t} seconds")

    p("Crafted by: ")

    for tier, type in machinesP.items():
        for type, info in type.items():
            if Y in info["crafting_type"]:
                p(formatT(f"  Tier {tier}: " + info["name"] + " (Speed:" + str(info["crafting_speed"]) + ")"))

def balancedBlueprint(recipeName, blueprintTier):
    
    if recipeName not in recipes:
        return p(f"Error: Invalid Item, try:\n{recipes.keys()}")

    items = recipes[recipeName]["input"] + recipes[recipeName]["output"]
    recipeTime = recipes[recipeName]["time"]
    recipeCraftingType = recipes[recipeName]["type"]
    beltSpeed = beltSpeeds[blueprintTier-1]
    inserterSpeed = inserterSpeeds[blueprintTier-1]

    machineFound = False
    for machineType, machineInfo in machinesP[blueprintTier].items():
        if recipeCraftingType in machineInfo["crafting_type"]:
            machine = machineInfo["name"]
            craftingSpeed = machineInfo["crafting_speed"]
            maxInserters = machineInfo["max_inserters"]
            machineFound = True
    if machineFound == False:
        return f"Error: Incompatible Item and Tier"
    

    itemNames = []
    itemAmounts = []
    for ingredient, amount in items:
        itemNames.append(ingredient)
        itemAmounts.append(amount)


    c = craftingSpeed
    n = itemAmounts
    t = recipeTime
    b = beltSpeed
    i = inserterSpeed

    # Per second rates of each item
    r = []
    for n_j in n:
        r.append(c*n_j/t)

    # Inserters per each item
    I = []
    for r_j in r:
        I.append(math.ceil(r_j/i))

    # Number of Machines
    M = 1
    unitBelts = []
    for r_j in r:
        unitBelts.append(Fraction(r_j/b).limit_denominator().denominator)
        for element in unitBelts:
            M = math.lcm(M, element)

    B = []
    for r_j in r:
        B.append(M*r_j/b)

    R = []
    for r_j in r:
        R.append(M*r_j)

    p("-"*80)
    p(formatT(f"Balanced Blueprint for {recipeName} with Tier {blueprintTier} machines/belts/inserters"))
    p("-"*80)
    p(formatT(f"  Requires {M} {machine}"))
    p("-"*30+"In"+"-"*30)
    for j in range(len(items)):
        p(formatT(f"    {R[j]}x {items[j][0]} / sec"))
        p(f"      Belts: " + format(B[j],".0f"))
        p(formatT(f"      Inserters: {I[j]}"))
        outputIndex = len(items) - len(recipes[recipeName]["output"]) - 1
        if(j==outputIndex):
            p("-"*30+"Out"+"-"*30)
        else: p("-"*40)




balancedBlueprint("satellite", 3)

