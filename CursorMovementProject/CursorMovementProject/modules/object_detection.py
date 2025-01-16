import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Finger landmarks
INDEX_TIP = mp_hands.HandLandmark.INDEX_FINGER_TIP
MIDDLE_TIP = mp_hands.HandLandmark.MIDDLE_FINGER_TIP
PINKY_TIP = mp_hands.HandLandmark.PINKY_TIP

# Click states to avoid repetitive clicks
left_click_performed = False
right_click_performed = False

def detect_object(frame):
    global left_click_performed, right_click_performed

    # Convert frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            h, w, _ = frame.shape
            
            # Get index finger tip position for cursor movement
            index_tip = hand_landmarks.landmark[INDEX_TIP]
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            
            # Get middle and pinky finger tip positions
            middle_tip = hand_landmarks.landmark[MIDDLE_TIP]
            pinky_tip = hand_landmarks.landmark[PINKY_TIP]
            
            middle_y = int(middle_tip.y * h)
            pinky_y = int(pinky_tip.y * h)
            
            # Perform left click if middle finger is raised
            if middle_tip.y < index_tip.y:  # Middle finger raised
                if not left_click_performed:
                    pyautogui.click(button='left')
                    left_click_performed = True
            else:
                left_click_performed = False

            # Perform right click if pinky finger is raised
            if pinky_tip.y < index_tip.y:  # Pinky finger raised
                if not right_click_performed:
                    pyautogui.click(button='right')
                    right_click_performed = True
            else:
                right_click_performed = False

            # Optionally draw the landmarks on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            return index_x, index_y
    
    return None, None
