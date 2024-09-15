import cv2
import mediapipe as mp
import pyautogui

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get hand landmarks
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    # Draw landmarks and handle gestures
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            # Iterate over the landmarks
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])

                # Draw circles for index finger and thumb
                if id == 8:
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                    index_x = screen_width / frame.shape[1] * x
                    index_y = screen_height / frame.shape[0] * y
                elif id == 4:
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                    thumb_x = screen_width / frame.shape[1] * x
                    thumb_y = screen_height / frame.shape[0] * y

                    # Check for click gesture
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    # Check for move gesture
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)

    # Display the resulting frame
    cv2.imshow('Virtual Mouse', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
