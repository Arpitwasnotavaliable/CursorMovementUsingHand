import pyautogui

# Initialize smoothing variables
prev_x, prev_y = None, None
smoothing_factor = 0.2  # Adjust between 0 (no movement) to 1 (instant movement)

def move_cursor(x, y, frame_shape):
    global prev_x, prev_y

    screen_width, screen_height = pyautogui.size()
    frame_height, frame_width, _ = frame_shape

    # Map camera coordinates to screen coordinates
    screen_x = int((x / frame_width) * screen_width)
    screen_y = int((y / frame_height) * screen_height)

    # Apply smoothing
    if prev_x is None or prev_y is None:
        smoothed_x, smoothed_y = screen_x, screen_y
    else:
        smoothed_x = int(prev_x + smoothing_factor * (screen_x - prev_x))
        smoothed_y = int(prev_y + smoothing_factor * (screen_y - prev_y))

    # Move cursor
    pyautogui.moveTo(smoothed_x, smoothed_y, duration=0.05)

    # Update previous coordinates
    prev_x, prev_y = smoothed_x, smoothed_y

movement_threshold = 5  # Minimum pixels to trigger cursor move

def move_cursor(x, y, frame_shape):
    global prev_x, prev_y

    screen_width, screen_height = pyautogui.size()
    frame_height, frame_width, _ = frame_shape

    # Map camera coordinates to screen coordinates
    screen_x = int((x / frame_width) * screen_width)
    screen_y = int((y / frame_height) * screen_height)

    # Apply smoothing and movement threshold
    if prev_x is None or prev_y is None:
        smoothed_x, smoothed_y = screen_x, screen_y
    else:
        smoothed_x = int(prev_x + smoothing_factor * (screen_x - prev_x))
        smoothed_y = int(prev_y + smoothing_factor * (screen_y - prev_y))

        if abs(smoothed_x - prev_x) < movement_threshold and abs(smoothed_y - prev_y) < movement_threshold:
            return  # Skip small movements

    # Move cursor
    pyautogui.moveTo(smoothed_x, smoothed_y, duration=0.05)

    # Update previous coordinates
    prev_x, prev_y = smoothed_x, smoothed_y
