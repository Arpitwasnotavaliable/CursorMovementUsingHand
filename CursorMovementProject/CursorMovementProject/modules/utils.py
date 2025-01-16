import pyautogui

def map_to_screen(x, y, frame_shape):
    screen_width, screen_height = pyautogui.size()
    frame_height, frame_width, _ = frame_shape

    # Map camera coordinates to screen coordinates
    screen_x = int((x / frame_width) * screen_width)
    screen_y = int((y / frame_height) * screen_height)
    
    return screen_x, screen_y
