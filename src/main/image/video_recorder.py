import cv2 as cv


class VideoRecorder:
    def __init__(self,
                 webcam: cv.VideoCapture,
                 video_codec: cv.VideoWriter_fourcc,
                 video_file_recorder: cv.VideoWriter):
        self.webcam = webcam
        self.video_codec = video_codec
        self.video_recorder = video_file_recorder

    @staticmethod
    def create_from_defaults():
        webcam = cv.VideoCapture(0)
        video_codec = cv.VideoWriter_fourcc(*"XVID")
        video_file_recorder = cv.VideoWriter("output.avi", video_codec, 30, (640, 480))
        video_recorder = VideoRecorder(webcam, video_codec, video_file_recorder)
        return video_recorder


    def record(self):
        while True:
            has_next, img = self.webcam.read()
            if has_next:
                self.video_recorder.write(img)
                cv.imshow("Input", img)
                is_space_bar_buffered = cv.waitKey(1) & 0xFF
                if is_space_bar_buffered == 32:
                    break
            else:
                break
        self.webcam.release()
        self.video_recorder.release()
        cv.destroyAllWindows()
        pass

