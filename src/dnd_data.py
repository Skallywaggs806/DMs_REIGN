races = [
    "Dragonborn",
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling",
    "Half-Orc",
    "Human",
    "Tiefling"
]#d9

classes = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]#d12

backgrounds = [
    "Acolyte",
    "Charlatan",
    "Criminal",
    "Entertainer",
    "Folk Hero",
    "Guild Artisan",
    "Hermit",
    "Noble",
    "Outlander",
    "Sage",
    "Soldier",
    "Urchin"
]#d12

monsters = [
    {
        "name": "Goblin",
        "hit_dice": "2d6",
        "armor_class": 15,
        "description": "A small, sneaky humanoid that attacks in groups and prefers ambushes.",
        "attacks": [
            {"action": "Scimitar", "damage_dice": "1d6+2", "description": "A slashing strike with a curved blade."},
            {"action": "Shortbow", "damage_dice": "1d6+2", "description": "A quick shot from a small bow."}
        ]
    },
    {
        "name": "Skeleton",
        "hit_dice": "2d8",
        "armor_class": 13,
        "description": "An animated humanoid skeleton wielding rusty weapons, vulnerable to bludgeoning.",
        "attacks": [
            {"action": "Shortsword", "damage_dice": "1d6+2", "description": "A rusty blade swung with eerie precision."},
            {"action": "Shortbow", "damage_dice": "1d6+2", "description": "A poorly aimed shot from a creaky bow."}
        ]
    },
    {
        "name": "Orc",
        "hit_dice": "2d8+6",
        "armor_class": 13,
        "description": "A brutish, aggressive humanoid with a love for battle and chaos.",
        "attacks": [
            {"action": "Greataxe", "damage_dice": "1d12+3", "description": "A powerful chop with a massive axe."},
            {"action": "Javelin", "damage_dice": "1d6+3", "description": "A thrown spear with brute force."}
        ]
    },
    {
        "name": "Giant Rat",
        "hit_dice": "2d6",
        "armor_class": 12,
        "description": "A large, aggressive rodent often found in sewers or ruins.",
        "attacks": [
            {"action": "Bite", "damage_dice": "1d4+2", "description": "A vicious bite that may carry disease."}
        ]
    },
    {
        "name": "Kobold",
        "hit_dice": "2d6-4",
        "armor_class": 12,
        "description": "A small, cowardly reptilian creature that sets traps and fights in packs.",
        "attacks": [
            {"action": "Dagger", "damage_dice": "1d4+2", "description": "A quick stab with a small blade."},
            {"action": "Sling", "damage_dice": "1d4+2", "description": "A stone hurled from a simple sling."}
        ]
    },
    {
        "name": "Zombie",
        "hit_dice": "3d8+3",
        "armor_class": 8,
        "description": "A slow, undead creature that relentlessly pursues the living.",
        "attacks": [
            {"action": "Slam", "damage_dice": "1d6+1", "description": "A heavy, clumsy strike with rotting limbs."}
        ]
    },
    {
        "name": "Dire Wolf",
        "hit_dice": "5d10+10",
        "armor_class": 14,
        "description": "A large, ferocious wolf with powerful jaws and pack tactics.",
        "attacks": [
            {"action": "Bite", "damage_dice": "2d6+3", "description": "A crushing bite that can knock foes prone."}
        ]
    },
    {
        "name": "Giant Spider",
        "hit_dice": "4d10+4",
        "armor_class": 14,
        "description": "A huge arachnid that spins webs and delivers venomous bites.",
        "attacks": [
            {"action": "Bite", "damage_dice": "1d8+3", "description": "A venomous bite that may poison its target."},
            {"action": "Web", "damage_dice": "0", "description": "A sticky web that can restrain foes (no damage)."}
        ]
    }
]#1d8