import cv2
import argparse
from pathlib import Path
from db import init_db, add_user  # <-- import works

# Initialize database immediately
init_db()

def capture_and_register(name, identifier, num_samples=5, cam_index=0):
    save_dir = Path("faces")
    save_dir.mkdir(exist_ok=True)

    cam = cv2.VideoCapture(cam_index)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    print('Press SPACE to capture an image. Press Q to quit.')

    count = 0
    while count < num_samples:
        ret, frame = cam.read()
        if not ret:
            print("Failed to read from camera")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame, f'Capture {count}/{num_samples}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Register - Press SPACE", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):  # SPACE key
            if len(faces) == 0:
                print("No face detected, try again")
                continue

            (x, y, w, h) = faces[0]
            face_img = frame[y:y+h, x:x+w]

            img_path = save_dir / f"{identifier}_{count}.jpg"
            cv2.imwrite(str(img_path), face_img)

            add_user(name, identifier, str(img_path))
            count += 1
            print(f"Captured sample {count}")

        elif key == ord('q'):  # Quit
            break

    cam.release()
    cv2.destroyAllWindows()
    print("Registration completed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="User name")
    parser.add_argument("--id", required=True, help="Unique identifier")
    parser.add_argument("--samples", type=int, default=5, help="Number of face samples to capture")
    args = parser.parse_args()

    capture_and_register(args.name, args.id, args.samples)
