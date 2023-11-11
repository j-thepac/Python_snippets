"""
Cheesy Cheeseman just got a new monitor! He is happy with it, but he just discovered that his old desktop wallpaper no longer fits. He wants to find a new wallpaper, but does not know which size wallpaper he should be looking for, and alas, he just threw out the new monitor's box. Luckily he remembers the width and the aspect ratio of the monitor from when Bob Mortimer sold it to him. Can you help Cheesy out?

The Challenge
Given an integer width and a string ratio written as WIDTH:HEIGHT, output the screen dimensions as a string written as WIDTHxHEIGHT.

Note: The calculated height should be represented as an integer. If the height is fractional, truncate it.

"""

def find_screen_height(width, ratio): 
    num,den=ratio.split(":")
    height=width*int(den)/int(num)
    return (f"{width}x{int(height)}")
    


assert(find_screen_height(1024, "4:3")== "1024x768")
assert(find_screen_height(1280, "16:9")== "1280x720")
assert(find_screen_height(3840, "32:9")== "3840x1080")
assert(find_screen_height(1600, "4:3")== "1600x1200")
assert(find_screen_height(1280, "5:4")== "1280x1024")
assert(find_screen_height(2160, "3:2")== "2160x1440")
assert(find_screen_height(1920, "16:9")== "1920x1080")
assert(find_screen_height(5120, "32:9")== "5120x1440")
print("DOne")