from dg_ai_platform.dg_platform import ITaskProcess
from PIL import Image, ImageOps

class TaskProcess1to1(ITaskProcess):
    def __init__(self):
        super().__init__()

    def inference(self, input_list, output_list, options=None):
        img1 = Image.open(input_list[0]).convert('RGB')
        img1 = ImageOps.grayscale(img1)
        img1.save(output_list[0])