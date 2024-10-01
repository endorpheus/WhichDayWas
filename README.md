# README.md

<p>
This is a simple app that tells the weekday of any date you type in. I know you could just look it up on a calendar app, ask AI, or whatever, but this was a fun proof of concept using Zeller's Congruence Algorithm.
</p>

<p>
I wrote the original with a Tkinter interface, but this new version looks much better, thanks to PySide6. It's not drastically different in functionality, but hey, it's all about the small improvements!
</p>

### The algorithm used:
```python
h = (q + 13*(m+1)//5 + d + y + (y//4) - (c//4)) % 7

where:
- q is day of the month
- m is the month (3 = March, ..., 12 = December)
- d is the day of the week (0 = Saturday, 1 = Sunday, ..., 6 = Friday)
- y is the year (e.g., 1988)
- c is the century (e.g., 19 for 1988)
```

<p>
It works pretty slick! I don't know how accurate it is, but I haven't seen any errors to date. (See what I did there?) 
</p>

<p>
You can also use this as a class for other projects if needed.
</p>

### Installation Instructions

To get started with this app, follow these steps:

1. **Clone the repository**  
   Run the following command to clone the repository to your local machine:
   ```
   git clone https://github.com/endorpheus/which-day-was.git
   cd which-day-was
   ```

2. **Install the required dependencies**  
   This app relies on PySide6 for the interface. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not present, you can manually install PySide6 with:
   ```
   pip install PySide6
   ```

3. **Run the app**  
   Once everything is set up, you can run the app with:
   ```
   python main.py
   ```

4. **App Icon**  
   The app uses a custom icon, but if for some reason the icon file is missing or not loading, it will generate a cheerful sun symbol instead!

5. **Enjoy!**  
   The app will display a system tray icon, and you can interact with it by right-clicking to show options like "About" or "Quit." Left-clicking the tray icon will show or hide the main window.

<p>
I hope you enjoy using the app as much as I enjoyed building it! Feel free to explore the code and see how <a href="https://en.wikipedia.org/wiki/Zeller%27s_congruence">Zeller's Congruence</a> works behind the scenes. 
</p>

# Thanks

Ryon Shane Hall
ryonshanehall.com