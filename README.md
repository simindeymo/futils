# FUtils
#### Just some funcs and utils.
#### The same on [the HackMD](https://hackmd.io/@themixray/futils)

## Keyboard (keyboard, keys)
### Keys
All existing keys
``` python
keyboard.keys
```
### Press key
``` python
keyboard.press(key)
```
### Release key
``` python
keyboard.release(key)
```
### Click key
For some programs delay must be changed to 150.
``` python
keyboard.click(key, delay=0)
```
### Write text
``` python
keyboard.write(text, delay=0)
```
### Is key pressed
Checks if a key is pressed.
``` python
keyboard.isPressed(key)
```
### Wait key 
Wait for a key press
``` python
keyboard.wait(key=None)
```
### Block keys
``` python
keyboard.block(timeout=None)
```
### Unblock keys
``` python
keyboard.unblock()
```
## Mouse (mouse)
### Click button
``` python
mouse.click(side)
```
### Move cursor
``` python
mouse.move(x, y, absolute=True, delay=100)
```
### Cursor position
``` python
mouse.position
```
### Is button pressed
``` python
mouse.isPressed(button)
```
### Wait button 
Wait for a button press
``` python
mouse.wait(key=None)
```
### Block mouse
``` python
mouse.block(timeout=None)
```
### Unblock mouse
``` python
mouse.unblock()
```
## Colors (colors)
### Text (text)
``` python
colors.text.black
colors.text.red
colors.text.green
colors.text.yellow
colors.text.blue
colors.text.magenta
colors.text.cyan
colors.text.white
```
### Background (bg)
``` python
colors.bg.black
colors.bg.red
colors.bg.green
colors.bg.yellow
colors.bg.blue
colors.bg.magenta
colors.bg.cyan
colors.bg.white
```
### Style (style)
``` python
colors.style.dim
colors.style.normal
colors.style.bright
```
## Console (cmd, console, cnsl)
### Interaction with the console
#### Print text
``` python
console.print(string, anim=False, center=False, animDelay=10, color=color.text.white, newLine=True, msBeforeDelete=None)
```
#### Input text
``` python
console.input(string, anim=False, center=False, animDelay=10, color=color.text.white, newLine=True)
```
#### Clear console
``` python
console.clear(lines=0)
```
#### Run command
``` python
console.run(cmd, show=False)
```
#### Printed text
``` python
console.printed
```
### Interaction with the console window
#### Window size
``` python
console.size
```
#### Window position
``` python
console.position
```
#### Is window visible
``` python
console.visible
```
#### Set window title
``` python
console.setName(name)
```
#### Get window title
``` python
console.getName()
```
#### Fullscreen window
``` python
console.maximize()
```
#### Minimize window
``` python
console.minimize()
```
#### Resize window
``` python
console.resize(width, height)
```
#### Move window
``` python
console.move(x, y)
```
#### Hide console
``` python
console.hide()
```
#### Show console
``` python
console.show()
```
#### Focus console
``` python
console.focus()
```
#### Unfocus console
``` python
console.unfocus()
```
## Base64 (base64)
#### In progress...
## Thread (thread())
#### In progress...
## Timer (timer())
#### In progress...
## Files (files, file)
#### In progress...
## Date (date())
#### In progress...
## Sound (sound())
#### In progress...
## Voice (voice)
#### In progress...
## Youtube (youtube, yt)
#### In progress...
## Json (json())
#### In progress...
## Mega (mega())
#### In progress...
## Window (window())
#### In progress...
