# MapET  

>Everything is still in tests  
>Everything in MapET program are still empty

Features
------------
<table>
  <tr>
    <td colspan="2">Map Selection</td>
    <td colspan="2">Level Editor</td>
    <td colspan="2">Tutorial</td>
    <td colspan="2">Settings</td>
    <td colspan="2">Misc</td>
  </tr>
  <tr></tr>
  <tr>
    <td>Map Select</td>
    <td><img src="http://progressed.io/bar/70"></td>
    <td>Map Attributes</td>
    <td><img src="http://progressed.io/bar/5"></td>
    <td>Tutorial System</td>
    <td><img src="http://progressed.io/bar/0"></td>
    <td>Screen Size Feature</td>
    <td><img src="http://progressed.io/bar/40"></td>
    <td>Infinitely large map</td>
    <td><img src="http://progressed.io/bar/0"></td>
  </tr>
  <tr>
    <td>Map Loading</td>
    <td><img src="http://progressed.io/bar/70"></td>
    <td>Player/Npc Movement</td>
    <td><img src="http://progressed.io/bar/0"></td>
    <td></td>
    <td></td>
    <td>Key Binds</td>
    <td><img src="http://progressed.io/bar/70"></td>
    <td>minimap</td>
    <td><img src="http://progressed.io/bar/50"></td>
  </tr>
  <tr>
    <td>GUI Load</td>
    <td><img src="http://progressed.io/bar/10"></td>
    <td>Cell system</td>
    <td><img src="http://progressed.io/bar/50"></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Camera follow</td>
    <td><img src="http://progressed.io/bar/10"></td><td></td>
 </tr>
  <tr>
    <td>User input</td>
    <td><img src="http://progressed.io/bar/50"></td>
    <td>Database</td>
    <td><img src="http://progressed.io/bar/10"></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Color Picker</td>
    <td><img src="http://progressed.io/bar/0"></td>
  </tr>
  
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Zoom in out</td>
    <td><img src="http://progressed.io/bar/0"></td>
   </tr>
   <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Escape backup save</td>
    <td><img src="http://progressed.io/bar/50"></td>
   </tr>
   <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Speed</td>
    <td><img src="http://progressed.io/bar/20"></td>    
  </tr>

</table>


Algorithm
---------

1. Start Program

2. Main Menu
  + Choose
    +  map selection
    +  level editor
    +  tutorial
    +  settings,
    +  exit

3. If Map selection:
  + Select a map
  + Prepare the map
  + Display GUI
  + Display Map
  + User input (zoom, speed of movement, move)
  + Player sprite/object (moving through the map with key binds)

4. If Level Editor:
Choose map to edit/Create new map
Prepare the map
Display GUI
Display Map
Settings
User input (zoom, speed of movement, move)
Player sprite/object (moving through the map with key binds)
Edit properties of cells (objects like walls, doors, keys, traps, moving things)
Program object behaviours, bots' movements, movement speed, camera settings
Cells contain graphics (gif or colour), data, comments, codes
Select a cell and map it into the map by clicking with mouse
Save and name map as text file into a map folder
Exit (if haven’t saved, save as backup)

5. If tutorial:
  + Show controls

  + Guide to using the program

6. If Settings:

  + Change settings (Fullscreen/window, change key binds)

7. If Exit:

  + Exit
