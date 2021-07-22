from dg_ai_platform.dg_platform import ITaskProcess
from PIL import Image

class TaskProcess2to1(ITaskProcess):
    def __init__(self):
        super().__init__()

    def inference(self, input_list, output_list, options=None):
        img1 = Image.open(input_list[0]).convert('RGB')
        img1 = img1.resize(size=(512, 512))
        img2 = Image.open(input_list[1]).convert('RGB')
        img2 = img2.resize(size=(512, 512))
        output = Image.blend(img1, img2, 0.5)
        output = output.resize((output.width, output.height))
        output.save(output_list[0])