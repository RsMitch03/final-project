# final-project
https://github.com/RsMitch03/final-project
https://pythonprogramming.net/adding-sounds-music-pygame/
https://www.pygame.org/docs/ref/mixer.html


This project is called The Rogue Trains!

The final project for 2305 PFDA Spring 2025 is a rogue fight, featuring me in foam swords I bought on Amazon for Halloween a couple of years ago. These images are stored in a folder under the src folder called OGFight_scene, containing the raw images that I took on my phone. From there, I implemented my first function, resize_fight(). This would resize the photos from their original size to a tenth of their size. I had to make special arrangements for the 14th photo as it shrunk down too much, but I made it proportionate to the other images, and saved them all to a new folder named Resized_scene. I took the resized folder and called my next function reformat_image(). This changed the images from JPGs to PNGs. I saved those to the Final_fight_scene folder so I can display these images. 

From there, I worked on sound. I took a sound effect to replicate a sword slice, hence the name swordSlice(). This would initialize pygame's mixer area, where I would play the effect only once at 90% volume. I proceeded to do the same with the music() function. The main difference was that I was playing it back indefinitely. After this, I gave my main() function. I initialize pygame, call the resize, reformat, and music functions so they start working before everything else. Then I would blit the current image, the hit count, and the music would play at 50% volume. With specific event types, either the hit count would go up and the sword slice would play, or the next image would be displayed.
