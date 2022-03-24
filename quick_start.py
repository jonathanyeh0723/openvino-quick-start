import cv2
import numpy as np
from openvino.preprocess import PrePostProcessor, ResizeAlgorithm
from openvino.runtime import Core, Layout, Type

core = Core()
model = core.read_model('mobilenet-v2-pytorch/FP16/mobilenet-v2-pytorch.xml')

image = cv2.imread('car.png')

input_tensor = np.expand_dims(image, 0)
ppp = PrePostProcessor(model)

_, h, w, _ = input_tensor.shape

ppp.input().tensor().set_element_type(Type.u8).set_layout(Layout('NHWC')).set_spatial_static_shape(h, w)
ppp.input().preprocess().resize(ResizeAlgorithm.RESIZE_LINEAR)
ppp.input().model().set_layout(Layout('NCHW'))
ppp.output().tensor().set_element_type(Type.f32)

model = ppp.build()
compiled_model = core.compile_model(model, 'CPU')

results = compiled_model.infer_new_request({0: input_tensor})
probs = next(iter(results.values()))
idx = np.argsort(probs[0])[::-1]

for i in range(5):
    print(idx[i], probs[0][idx[i]])
