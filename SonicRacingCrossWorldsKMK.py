from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class SRCArchipelagoOptions:
    pass

class SRCGame(Game):
    name = "Sonic Racing: CrossWorlds"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.SW2,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = SRCArchipelagoOptions
    
    def characters_base(self) -> List[str]:
        return [
            "Sonic",
            "Tails",
            "Knuckles",
            "Amy",
            "Cream & Cheese",
            "Big",
            "Silver",
            "Blaze",
            "Shadow",
            "Rouge",
            "Omega",
            "Vector",
            "Espio",
            "Charmy",
            "Zavok",
            "Zazz",
            "Dr. Eggman",
            "Metal Sonic",
            "Egg Pawn",
            "Sage",
            "Jet",
            "Wave",
            "Storm",
        ]
    
    def characters(self) -> List[str]:
        characters: List[str] = self.characters_base()[:]
        characters.extend([
            "NiGHTS",
            "Joker",
            "Ichiban",
            "Miku",
        ])
        return sorted(characters)
    
    def vehicles(self) -> List[str]:
        return sorted(self.speed_vehicles[:] + self.acceleration_vehicles[:] + self.handling_vehicles[:] + self.power_vehicles[:] + self.boost_vehicles[:])

    @functools.cached_property
    def speed_vehicles(self) -> List[str]:
        return [
            "Speedster Lightning",
            "Dark Reaper",
            "Mirage Blade",
            "Super Shining",
            "Royal Chariot",
            "Stealth Chaser",
            "Retro Future",
            "Wild GT",
            "Buster M",
            "Arsène Wing",
        ]
    
    @functools.cached_property
    def acceleration_vehicles(self) -> List[str]:
        return [
            "Whirlwind Sport",
            "Jumble Rage",
            "Hyper Scorpion",
            "Cyber Spear",
            "Pawn Calibur",
            "Long Stinger",
            "Radical Fours",
            "Racing Buggy",
            "Giganto Liner",
        ]

    @functools.cached_property
    def handling_vehicles(self) -> List[str]:
        return [
            "Pink Cabriolet",
            "Lip Spyder",
            "Victoria Carriage",
            "Moto Beetle",
            "Ancient Throne",
            "Little Lady",
            "Hot Hatch",
            "Fossil Rock",
            "Neo Lightron",
        ]

    @functools.cached_property
    def power_vehicles(self) -> List[str]:
        return [
            "Land Smasher",
            "Road Dragoon",
            "Knight Tank",
            "Fang Loader",
            "Beat Gator",
            "Frog Cruiser",
            "Cross Dozer",
            "Trail Runner",
            "Egg Drillster Mk. II",
            "Dragon Brave",
        ]

    @functools.cached_property
    def boost_vehicles(self) -> List[str]:
        return [
            "TYPE-J Iota",
            "TYPE-S Stream",
            "Sakura Board",
            "Triple Fan",
            "Pop Float",
            "TYPE-W Windy",
            "Wispon Booster",
            "Quad Copter",
            "Jaws Rocket",
            "Diva Macchina",
            "Dream Sleeper",
        ]

    @staticmethod
    def grand_prixs() -> List[str]:
        return [
            "Donpa",
            "Wisp",
            "Boom Boo",
            "Pumpkin",
            "Coral",
            "Crystal",
            "Eggman",
            "Secret",
        ]

    def courses(self) -> List[str]:
        return [
            "E-Stadium",
            "Rainbow Garden",
            "Water Palace",
            "Metal Harbor",
            "Sand Road",
            "Colorful Mall",
            "Mystic Jungle",
            "Apotos",
            "Wonder Museum",
            "Crystal Mine",
            "Ocean View",
            "Pumpkin Mansion",
            "Urban Canyon",
            "Market Street",
            "Coral Town",
            "Blizzard Valley",
            "Radical Highway",
            "Chao Park",
            "Donpa Factory",
            "Aqua Forest",
            "Eggman Expo",
            "Kronos Island",
            "Northstar Islands",
            "White Space",
        ]

    def crossworlds(self) -> List[str]:
        return [
            "Sky Road",
            "Roulette Road",
            "Kraken Bay",
            "Golden Temple",
            "Magma Planet",
            "Hidden World",
            "Steampunk City",
            "Dragon Road",
            "Holoska",
            "Galactic Parade",
            "Dinosaur Jungle",
            "Sweet Mountain",
            "White Cave",
            "Cyber Space",
            "Digital Circuit",
        ]

    def time_trial_courses(self) -> List[str]:
        return self.courses()[:] + self.crossworlds()[:]
   
    @staticmethod
    def race_park_rules() -> List[str]:
        return [
            "Triple Team Ring Grab",
            "Triple Team Tap Boost",
            "Double Team Shoot-out",
            "Double Team Dash",
            "Quick Match",
            "Extreme Match",
        ]

    @staticmethod
    def speeds() -> List[str]:
        return [
            "Normal",
            "High",
            "Sonic",
            "Mirror Sonic",
            "Super Sonic",
        ]

    @staticmethod
    def items() -> List[str]:
        return [
            "Boost"
            "Double Boost",
            "Triple Boost",
            "Laser",
            "Drill",
            "Warp Ring",
            "Monster Truck",
            "Omochao",
            "100 Rings"
            "Homing Punch",
            "Triple Homing Punch",
            "Rocket Punch",
            "Triple Rocket Punch",
            "Slicer",
            "Bomb",
            "King Boom Boo",
            "Slime",
            "Weights",
            "Dark Chao",
            "Void",
            "Shield",
            "Tornado",
            "Spiked Iron Ball",
            "Magnet",
        ]

    @staticmethod
    def gadgets() -> List[str]:
        return [
           "Starting Boost Bounty",
           "Air Trick Bounty",
           "Item Attack Bounty",
           "Runoff Bounty",
           "Slipstream Bounty",
           "Travel Ring Bounty",
           "Morph Action Bounty",
           "Perfect Charge Bounty",
           "Dash Panel Bounty",
           "Dash Panel Mini Bounty",
           "Dash Panel Combo Bounty",
           "130 Ring Limit",
           "200 Ring Limit",
           "Mini Ring Thief",
           "Ring Thief",
           "Ring Gain Mini Boost",
           "Ring Gain Boost",
           "Ring Range UP",
           "Extended Slipstream",
           "Air Drift Mobility",
           "Charge Jump Mobility",
           "Air Trick Adept",
           "Air Trick Expert",
           "Collision Boost",
           "Spin Drift",
           "Lv1 Quick Charge",
           "Lv2 Quick Charge",
           "Lv3 Quick Charge",
           "Ultimate Charge",
           "Perfect Charge Boost",
           "Technical Drift",
           "Friction Drift",
           "Counter Quick Charge",
           "Quick Starter",
           "Super Quick Starter",
           "Slow Starter",
           "Super Slow Starter",
           "Speed Tuner 1",
           "Speed Tuner 2",
           "Acceleration Tuner 1",
           "Acceleration Tuner 2",
           "Handling Tuner 1",
           "Handling Tuner 2",
           "Power Tuner 1",
           "Power Tuner 2",
           "Boost Tuner 1",
           "Boost Tuner 2",
           "Ring Mercy",
           "Damage Mercy",
           "Item Mercy",
           "Maximum Traction",
           "Second Wind",
           "Invincible Start",
           "Strong Finish",
           "Item Keeper",
           "Quick Recovery",
           "Crash Pads",
           "Lucky Pair",
           "Double Down",
           "Inventory Swap",
           "Inventory Plus",
           "Hazard Item Chance UP",
           "Attack Item Chance UP",
           "Defense Item Chance UP",
           "Speed Item Chance UP",
           "Wisp Chance UP",
           "Boost Starter",
           "Double Boost Specialist",
           "Dark Chao Starter",
           "Warp Ring Specialist",
           "Giant Rocket Punch",
           "Giant Spiked Iron Ball",
           "Short Fuse",
           "Monster Truck Starter",
           "Drift Charge Kit",
           "Item Hoarder Kit",
           "Damage Support Kit",
           "Speed Machine Kit",
           "Acceleration Machine Kit",
           "Handling Machine Kit",
           "Power Machine Kit",
           "Boost Machine Kit",
        ]
    
    @staticmethod
    def positions() -> List[str]:
        return [
            "1st",
            "2nd or better",
            "3rd or better",
        ]

    @staticmethod
    def easy_rival_levels() -> range:
        return range(3,7)

    @staticmethod
    def hard_rival_levels() -> range:
        return range(7,11)

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return []

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Finish 1st on COURSE as CHARACTER on SPEED Speed",
                data={
                    "COURSE": (self.courses, 1),
                    "CHARACTER": (self.characters, 1),
                    "SPEED": (self.speeds, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            GameObjectiveTemplate(
                label="Finish POSITION on COURSES as CHARACTER on SPEED Speed",
                data={
                    "POSITION": (self.positions, 1),
                    "COURSES": (self.courses, 3),
                    "CHARACTER": (self.characters, 1),
                    "SPEED": (self.speeds, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Finish POSITION in the GP Grand Prix as CHARACTER on SPEED Speed against a level LEVEL rival",
                data={
                    "POSITION": (self.positions, 1),
                    "GP": (self.grand_prixs, 1),
                    "CHARACTER": (self.characters, 1),
                    "SPEED": (self.speeds, 1),
                    "LEVEL": (self.easy_rival_levels, 1),
                },
                is_time_consuming=False,
                is_difficult= False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Finish POSITION in the GP Grand Prix as CHARACTER on SPEED Speed against a level LEVEL rival",
                data={
                    "POSITION": (self.positions, 1),
                    "GP": (self.grand_prixs, 1),
                    "CHARACTER": (self.characters, 1),
                    "SPEED": (self.speeds, 1),
                    "LEVEL": (self.hard_rival_levels, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a RULESET on COURSE on SPEED Speed against a level LEVEL rival team",
                data={
                    "RULESET": (self.race_park_rules, 1),
                    "COURSE": (self.courses, 1),
                    "SPEED": (self.speeds, 1),
                    "LEVEL": (self.easy_rival_levels, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            GameObjectiveTemplate(
                label="Win a RULESET on COURSE on SPEED Speed against a level LEVEL rival team",
                data={
                    "RULESET": (self.race_park_rules, 1),
                    "COURSE": (self.courses, 1),
                    "SPEED": (self.speeds, 1),
                    "LEVEL": (self.hard_rival_levels, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get an A rank on the Sonic Speed time trial for COURSE",
                data={
                    "COURSE": (self.time_trial_courses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
            GameObjectiveTemplate(
                label="Complete a race (other than a Custom Match) in which Lap 2 takes place in CROSSWORLD",
                data={
                    "CROSSWORLD": (self.crossworlds, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1
            ),
            GameObjectiveTemplate(
                label="Hit CHARACTER with an item",
                data={
                    "CHARACTER": (self.characters_base, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
            GameObjectiveTemplate(
                label="Finish 1st while holding ITEM",
                data={
                    "ITEM": (self.items, 1),        
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2
            ),
            GameObjectiveTemplate(
                label="Win a race with the GADGET gadget equipped",
                data={
                    "GADGET": (self.gadgets, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3
            ),
        ]