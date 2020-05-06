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

# Tips
1. If you don't specify a return from any function, it returns None. 
This is a problem for our program, as each menu function has to return a valid dictionary to use with the JSON file. 
So if your menu function does not return anything, please return an empty dictionary, by 
writing: <pre><code>return {}</code></pre>
This will return an empty dictionary, which is what we want to do.
<br>

2. In order for the JSON to be correctly stored in the JSON file, we have to have every function return a python "dictionary". 
A dictionary is basically an array, you can google python dictionaries if you want to learn more, but all you need to 
know is that a dictionary has to have a "key" and a "value". If you have a look at my module, fearghal.py, you will see 
that after each option I return a dictionary, which is in the form <code>{"key": "value"}</code> (Also, note the curly brackets, 
the space for the value after the colon, and the double double quotes for a string value.) Strings have to be in double 
quotation marks in JSON, numbers can be without 
quotation marks.
<br>

3. Fearghal has created 4 functions to do four things with the dictionaries and the JSON file (All of which are inside 
the <code>fearghals_functions</code> module).

    - <code>append_settings</code>: This function takes a valid dictionary and appends (Writes to the end of) to the end of the 
    desired file (The default of which is <code>config.json</code>). For the majority of the time, you will be using this function 
    to write to the file
    
    - <code>add_settings_to_start</code>: Does the exact same thing as <code>append_settings</code>, but writes to the start of the file 
    instead.
    
    - <code>load</code>: This function will load the specified filename (The default of which is <code>config.json</code>) You will usually 
    assign this function to a variable (e.g <code>settings = load("config.json")</code> to get and set specific values from the 
    existing keys and values (e.g settings.get("resolution") would be of the value "1080p" or "720p", etc.) already 
    made from using the append_settings function.
    
    - <code>show</code>: This function will print out to you the current JSON data inside the specified filename (The default of 
    which is <code>config.json</code>).

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