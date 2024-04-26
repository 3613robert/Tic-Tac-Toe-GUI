from PIL import Image, ImageTk

class PlaceMarker:
    def __init__(self, board_instance, label_instance):
        self.board_instance = board_instance
        self.label_instance = label_instance
        self.x_marker = None
        self.o_marker = None

    def resize_marker(self):
        original_image_x = Image.open('transparantX.png')
        # Resize the image
        resized_image_x = original_image_x.resize((120, 115))
        # Convert resized image to PhotoImage object
        self.x_marker = ImageTk.PhotoImage(resized_image_x)

        original_image_o = Image.open('transparantO.png')
        # Resize the image
        resized_image_o = original_image_o.resize((120, 115))
        # Convert resized image to PhotoImage object
        self.o_marker = ImageTk.PhotoImage(resized_image_o)

    def get_markers(self):
        if self.x_marker is None or self.o_marker is None:
            self.resize_marker()
        return self.x_marker, self.o_marker
