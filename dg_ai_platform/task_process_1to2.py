from dg_ai_platform.dg_platform import ITaskProcess
from PIL import Image, ImageOps

class TaskProcess1to2(ITaskProcess):
    def __init__(self):
        super().__init__()

    def inference(self, input_list, output_list, options=None):
        img1 = Image.open(input_list[0]).convert('RGB')
        output1 = ImageOps.grayscale(img1)
        output2 = ImageOps.posterize(img1, 1)
        output1.save(output_list[0])
        output2.save(output_list[1])