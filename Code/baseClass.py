class Fighter:
  int max_health
  # Max Health Value
  int health
  # Curent Health
  
  int max_spell
  # Max Spell Value
  int spell
  # Curent Spell

  int current_weapon = 000000
  # Curent Weapon(Uses Weapon 6-digit code)
  spell_list = [000000, 000000, 000000, 000000, 000000, 000000]
  # Curent Spells(Uses Spell 6-digit code)

  boolean is_guarding = False
  # Sets Guarding Value To False
  boolean is_burnt = False
  # Sets Burning Value To False
  boolean is_choking = False
  # Sets Choking Value To False

  # Creating Class:
  def Fighter(hp=5, sp=5):
    # Sets Data:
    
    max_health = hp
    health = max_health
    # Sets Health Stats
    
    max_spell = sp
    spell = max_spell
    # Sets Spell Stats

    # THE NEXT LINES ARE TEMPORARY AND ARE FOR TESTING COMBAT ONLY:
    spell_list[0]=000001
