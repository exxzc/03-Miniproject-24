# Light Orchestra — ECE 463 Mini-Project

## Project Overview
Light Orchestra empowers people of all ages to create and share music through playful interactions with light. By transforming everyday light sources into instruments, it makes music-making collaborative, accessible, and fun.  

In this mini-project, we implemented a modular system on the Raspberry Pi Pico 2W. The photoresistor acts as the input (reading light intensity), and the buzzer serves as the output (generating sound). Light intensity is translated into musical notes in the C major scale, enabling the Pico to perform simple melodies interactively.

## Features
- SensorHAL (Reading): Smoothly samples and normalizes light intensity from the photoresistor.  
- NoteMapper (Translation): Maps normalized light values (0–1) to pitches in the C major scale, with hysteresis and minimum note-hold to avoid jitter.  
- BuzzerPlayer (Buzzer): Drives a piezo buzzer with PWM, producing audible notes with dynamic loudness.  
- Main Conductor Loop: Connects all modules together, runs the continuous loop to read light, map it to notes, and play them.

## Repository Structure
src/
├── sensor_hal.py # Sensor reading and normalization
├── note_mapper.py # Mapping normalized values to pitches
├── buzzer_player.py # PWM buzzer driver
└── main.py # Main conductor loop, integrates all modules


## Team Contributions
- Xinyu Wu — Hardware wiring and studying the Pico board pinout.  
- Zitong He — Implemented `SensorHAL` (sensor reading and normalization).  
- Zean Wan — Implemented `NoteMapper` (translation from light intensity to pitch).  
- Jian Dang — Implemented `BuzzerPlayer` (buzzer driver module).  
- Fuyang Chen — Wrote `main.py`, testing and integration, debugging and code modifications.  
- Esther — Documentation (README, wiring diagrams, and project notes).  

## Usage
1. Clone the repository.  
2. Open in Thonny or another MicroPython IDE.  
3. Upload all four `.py` files (`sensor_hal.py`, `note_mapper.py`, `buzzer_player.py`, `main.py`) to the Pico (This device).  
4. Edit `sensor_hal.py` to adjust `VMIN` and `VMAX` based on your measured environment (cover sensor = VMIN, shine flashlight = VMAX).  
5. Run `main.py`.  
6. Use a flashlight or cover/uncover the sensor to play notes.  

## Future Work
- Support multi-octave mapping for richer sound.  
- Add melody playback mode with pre-programmed songs.  
- Expand with Wi-Fi API for conductor-based orchestration across multiple boards.  

