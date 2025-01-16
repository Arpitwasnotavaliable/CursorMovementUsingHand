import cv2
from modules.object_detection import detect_object
from modules.cursor_control import move_cursor

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect object position
        x, y = detect_object(frame)
        
        # Move cursor based on the detected position
        if x is not None and y is not None:
            move_cursor(x, y, frame.shape)
        
        # Display the frame
        cv2.imshow('Object Tracking', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
