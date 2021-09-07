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
console.print(string, anim=False, center=False, 
                animDelay=10, color=color.text.white, 
                newLine=True, msBeforeDelete=None)
```
#### Input text
``` python
console.input(string, anim=False, center=False, 
                animDelay=10, color=color.text.white, 
                newLine=True, whitelist=None, count=None)
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
#### Start app
``` python
console.start(path)
```
#### Console args
``` python
console.args
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
#### Block console
``` python
console.block(move=False, click=False)
```
#### Unblock console
``` python
console.unblock()
```
#### Focus console
``` python
console.focus()
```
#### Unfocus console
``` python
console.unfocus()
```
#### Screenshot console
``` python
console.screenshot(path)
```
## Base64 (base64)
### Encode text
``` python
base64.encode(text)
```
### Decode text
``` python
base64.decode(text)
```
## Thread (thread())
### Create
``` python
thread(func, name=None, daemon=True, group=None)
```
### Start
``` python
thread.start()
```
### Stop
``` python
thread.stop()
```
## Timer (timer())
### Create
``` python
timer(func, interval)
```
### Start
``` python
timer.start()
```
### Stop
``` python
timer.stop()
```
### Is started
``` python
timer.isStarted
```
## Files (files, file)
### Read
``` python
file.read(path)
```
### Write
``` python
file.write(path, text)
```
### Create
``` python
file.create(path)
```
### Remove
``` python
file.remove(path)
```
### Is exists
``` python
file.exists(path)
```
### Local path
``` python
file.local()
```
### Get dir's files
``` python
file.files(path)
```
### Convert files
``` python
file.convert(path, dist)
```
### Create dir
``` python
file.createDir(path)
```
### Remove dir
``` python
file.removeDir(path)
```
### Local file
``` python
file.localFile(path)
```
## Date (date())
### Day
``` python
date.day
```
### Month
``` python
date.month
```
### Year
``` python
date.year
```
### Hour
``` python
date.hour
```
### Minute
``` python
date.minute
```
### Second
``` python
date.second
```
## Sound (sound())
### Create
``` python
sound(path)
```
### Play
``` python
sound.play()
```
### Stop
``` python
sound.stop()
```
### Get volume
``` python
sound.volume
```
### Set volume
``` python
sound.setVolume(volume)
```
### Length
``` python
sound.length
```
## Voice (voice)
### Speak
``` python
voice.speak(text)
```
### Listen
``` python
voice.listen(language="ru-RU")
```
### Save 
``` python
voice.save(text, filename, say=False)
```
## Youtube (youtube, yt)
### Get video
``` python
yt.get(link)
```
### Video's parameters 
``` python
video = yt.get(link)
video.link
video.shortLink
video.id
video.title
video.description
video.author
video.preview
video.views
video.duration
video.createdAt
video.rating
video.author.name
video.author.id
video.author.link
video.author.avatar
```
### Video's methods 
``` python
video = yt.get(link)
video.download(on_progress_callback=lambda x: None,
                     on_complete_callback=None, proxies=None,
                     fps=None, res=None, resolution=None,
                     mime_type=None, type=None, subtype=None,
                     file_extension=None, abr=None, bitrate=None,
                     video_codec=None, audio_codec=None, only_audio=None,
                     only_video=None, progressive=None, adaptive=None,
                     is_dash=None, custom_filter_functions=None,
                     output_path=None, filename=None, filename_prefix=None,
                     skip_existing=True, timeout=None, max_retries=0)
video.author.getLastVideo()
```
### Search video
``` python
yt.search(search, limit=15)
```
## Json file (configJson())
### Create
``` python
configJson(path)
```
### Get
``` python
configJson.get()
```
### Set
``` python
configJson.set(to)
```
## Json encoding (json)
### Encode
``` python
json.encode(var)
```
### Decode
``` python
json.decode(string)
```
## Mega (mega())
### Create
``` python
mega(email=None, password=None)
```
### Used size
``` python
mega.usedSize
```
### Total size
``` python
mega.totalSize
```
### User
``` python
mega.user
```
### Quota
``` python
mega.quota
```
### Files
``` python
mega.files
```
### Rename file
``` python
mega.rename(file, name)
```
### Upload file
``` python
mega.upload(file)
```
### Download file
``` python
mega.download(file, dest_path=None, dest_filename=None)
```
### Get link
``` python
mega.getLink(file)
```
### Delete file
``` python
mega.delete(file)
```
### Remove file
Deleting and clearing trash.
``` python
mega.remove(file)
```
### Move file
``` python
mega.move(file, to)
```
### Create dir
``` python
mega.createDir(path)
```
### Download link
``` python
mega.downloadLink(link, dest_path=None, dest_filename=None)
```
### Clear trash
``` python
mega.clearTrash()
```
### Read file
``` python
mega.read(file)
```
### Write text to file
``` python
mega.write(file, text)
```
### Clear symbols from file
``` python
mega.clearFile(file)
```
### Create file
``` python
mega.create(file)
```
## Window (window())
### Create
Attribute name can be either hwnd or the name of the window.
``` python
window(name)
```
### Close
``` python
window.close()
```
### Focus
``` python
window.focus()
```
### Unfocus
``` python
window.unfocus()
```
### Hide
``` python
window.hide()
```
### Show
``` python
window.show()
```
### Move
``` python
window.move(x, y)
```
### Resize
``` python
window.resize(width, height)
```
### Minimize
``` python
window.minimize()
```
### Maximize
``` python
window.maximize()
```
### Block
``` python
window.block(move=False, click=False)
```
### Unblock
``` python
window.unblock()
```
### Is visible
``` python
window.visible
```
### Get position
``` python
window.position
```
### Get size
``` python
window.size
```
### Get title
``` python
window.name
```
### Get hwnd
``` python
window.hwnd
```
### Get process id
``` python
window.pid
```
### Click mouse
``` python
window.click(x, y, side='left')
```
### Get mouse position
``` python
window.position
```
### Screenshot window
``` python
window.screenshot
```
## Copyboard (cp, copies, copyboard)
### Get copied text
``` python
copyboard.copied()
```
### Copy text
``` python
copyboard.copy(text)
```
## Other funcs
### Remove all characters in the string except numbers
``` python
removeAllExceptNumbers(string)
```
### Remove string prefix
``` python
removePrefix(string, value)
```
### Remove string suffix
``` python
removeSuffix(string, value)
```
### Get the type of a var
This variable gets the name of the class.
```
type(var)
```
### HEX to RGB
``` python
hex2rgb(hex)
```
### RGB to HEX
``` python
rgb2hex(rgb)
```
### Wait in milliseconds
``` python
wait(ms)
```
### Random
Get a random number or get a random item in the list.
``` python
rand(x, y)
rand(list)
```
### Kill program
Stop the program in the usual way.
``` python
kill('default')
```
Stop the program with an error. (Always works :))
``` python
kill('raise')
```
### Translate text
```
translate(text, from, to)
```
### Get all windows
``` python
windows(onlyVisible=True)
```
### Screenshot
``` python
screenshot(path)
```
