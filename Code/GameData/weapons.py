class Weapon:
  int dmg_type
  # Gives Damage Type(0 For Slashing, 1 For Bludgeoning, 2 For Projectile)
  int prestigeLevel = 0
  # Gives Prestige Level(000000 Cannot Be Prestige)
  int id_code
  # Gives ID For Code:
  
  int max_dmg
  # Gives Max Damage
  int min_dmg
  # Gives Min Damage

  int max_combo
  # Gives Max Combo
  int min_combo
  # Gives Min Combo
  int crit_chance
  # Gives Crit Chance(1-100)

  int total_kills = 0
  # Gives Total Kills With Weapon
  int total_dmg = 0
  # Gives Total Damage With Weapon
  
  def Weapon(wpn_type = 1, id=000000 ,max_d=7, min_d=4, max_c=2, min_c=3, crit 90):
    dmg_type = wpn_type
    id_code = id
    max_dmg = max_d
    min_dmg = min_d
    max_combo = max_c
    min_combo = min_c
    crit_chance = crit
