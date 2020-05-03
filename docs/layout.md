# Objectives
1.  Have a start screen to create your character with naming system and character design.
2.  Using JSON for config
3.  Main Menu, Options, Display, etc.

# Allocation of work

Diarmud:
<br>
Main Menu -> New Game -> Character Selection (Male or Female, Orc or Wolf, Mage or Assassin, etc.)

Fearghal:
<br>
Main Menu -> Load Game (JSON loading and saving, as well as part of the Options menu)
<br>
Main Menu -> New Game (Saving the game settings)

Brian:
<br>
Options -> Resolution (The resolution of the display)

Placeholder name:
<br>
Menu Name -> Sub-Menu Name (Description of the task to do)
# Game Layout:

<pre><code>Game
└── Main Menu
    ├── New Game
    │   └── (Character selection)
    │       ├── Male   ──┐
    │       ├── Female ──┐
    │       │            │
    ╞═══════╬══ Back     │
    │       ║            └── Race
    │       ║                ├── Human  ──┐
    │       ║                ├── Elf    ──┐
    │       ║                ├── Lizard ──┐
    │       ║                ├── Wolf   ──┐
    │       ║                │            │
    │       ╚═══════════════╬══ Back ═    │
    │                        ║            └── Class
    │                        ║                ├── Mage     ──┐
    │                        ║                ├── Archer   ──┐
    │                        ║                ├── Warrior  ──┐
    │                        ║                ├── Assassin ──┐
    │                        ║                │              │
    │                        ╚════════════════╬══ Back       │
    │                                         ║              ├── Start Game
    │                                         ║              │
    │                                         ╚══════════════╧══ Back                         
    │
    │
    ├── Load Game
    │   ├── (Save selection) ──┐
    │   │                      │
    ╞═══╬══ Back               ├── (Confirmation of Save selection)
    │   ║                      │                         
    │   ╚══════════════════════╧══ Back       
    │
    │
    ├── Options
    │   ├── Audio ──────────────────┐
    │   │   ├── Toggle Rain Volume  │
    │   │   │                       └── Volume Control
    │   │   │                           ├── Master
    │   │   │                           ├── Effects
    │   │   │                           ├── Voice
    │   │   │                           ├── Footsteps
    │   │   │                           │
    │   │   ╘═══════════════════════════╧══ Back  
    │   │
    │   │    
    │   ├── Gameplay
    │   │   ├── Difficulty
    │   │   │   ├── Easy
    │   │   │   ├── Normal
    │   │   │   ├── Hard
    │   │   │   └── Hell
    │   │   │
    │   │   ├── Field of View
    │   │   │   └── (60° to 180°)
    │   │   │
    │   ╞═══╧══ Back
    │   │
    │   ├── Display
    │   │   ├── Video Mode
    │   │   │   ├── Fullscreen
    │   │   │   ├── Windowed
    │   │   │   ├── Borderless Windowed
    │   │   │   │
    │   │   ╞═══╧══ Back
    │   │   │
    │   │   ├── Resolution
    │   │   │   ├── (use the module screeninfo for it)
    │   │   │   │
    │   │   ╞═══╧══ Back
    │   │   │
    │   │   ├── Frame Rate Limit
    │   │   │   ├── 60
    │   │   │   ├── 72
    │   │   │   ├── 90
    │   │   │   ├── 120
    │   │   │   ├── 144
    │   │   │   ├── 240
    │   │   │   ├── Unlimited
    │   │   │   │
    │   │   ╞═══╧══ Back   
    │   │   │
    │   │   ├── Vertical Sync
    │   │   │   ├── On
    │   │   │   ├── Of
    │   │   │   │
    │   │   ╞═══╧══ Back
    │   │   │
    │   │   ├── Quality
    │   │   │   ├── Low
    │   │   │   ├── Medium
    │   │   │   ├── High
    │   │   │   ├── Ultra
    │   │   │   │
    │   │   ╘═══╧══ Back
    │   │
    │   ├── Controls
    │   │   ├── Keyboard and Mouse
    │   │   │   ├── Bindings
    │   │   │   │
    │   │   ╞═══╧══ Back
    │   │   │
    │   │   ├── Controller
    │   │   │   ├── Enable controller?
    │   │   │   │   ├── Yes
    │   │   │   │   ├── No
    │   │   │   │   │
    │   │   │   ╞═══╧══ Back
    │   │   │   │
    │   │   │   ├── Bindings
    │   │   ╘═══╧══ Back                
    │   │ 
    ╞═══╩══ Back
    │ 
    │
    ╘══ Exit Game
</code></pre>


Obviously not all of these options have to be implemented, but it just gives you a sense of what we should be 
aiming for.