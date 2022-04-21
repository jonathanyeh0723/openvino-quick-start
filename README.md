# openvino-quick-start

Today, everybody talks about Artificial Intelligence (AI). It is growing rapidly and its market is on fire.  OpenVINO is a power toolkit that that you can easily develop and deploy AI solutions with Intel® platforms, on the Cloud or on the Edge.  Following the repository instruction to quickly kick-start your AI journey!

- What is OpenVINO?

  - OpenVINO stands for Open Visual Inferencing and Neural Network Optimization. It is a toolkit that you can develop and deploy computer vision oriented solutions on Intel® platforms, on the Cloud or on the Edge.

## Inference Engine

![inference_enine_flow](./resources/inference_flow.jpg)

### What is the Inference Engine?

- Optimized for Intel® hardware.
  - It provides hardware-based optimizations to get even further improvements from a model.
  
- Running the actual inference at the edge.
  - It only works with the Intermediate Representation (IR) files.
  - They (IR) are come from Intel® Open Model Zoo. Or we can produce them from the Model Optimizer.

- Consists of a high-level API so that we can utilize on the edge application easily.
  - It is built with C++ for faster operations.
  - We can use the built-in Python wrapper to work with the inference engine.

![supported](./resources/support_os_hw.jpg)

### Run

Open the Anaconda Prompt. Activate the environment we just created.<br>
```
conda activate ov_2022_dev
```

After that, clone this repo to your local machine.<br>
```
git clone https://github.com/jonathanyeh0723/openvino-quick-start
```

You should be able to see the following outputs from the console.<br>
```
Cloning into 'openvino-quick-start'...
remote: Enumerating objects: 65, done.
remote: Counting objects: 100% (65/65), done.
remote: Compressing objects: 100% (44/44), done.
Receiving objects: 100% (65/65), 6.72 MiB | 3.74 MiB/sk-reused 0 eceiving objects:  55% (36/65), 5.95 MiB | 3.74 MiB/s
68 MiB/s, done.
Resolving deltas: 100% (22/22), done.
```

Once it's done, change your working directory to the cloned directory.<br>
```
cd openvino-quick-start
```

Now we'll need to install the required dependencies for this project by typing the below commands:<br>
```
pip install -r requirements.txt
```

**Note: If you encounter some error messages in this step, just ignore it. It's about the tensorflow-gpu related compatibility.**

```
(base) C:\Users\Jonathan>conda activate ov_2022_dev

(ov_2022_dev) C:\Users\Jonathan>cd openvino-quick-start

(ov_2022_dev) C:\Users\Jonathan\openvino-quick-start>python quick_start.py
Inference Results:
511, convertible --- 12.158
436, beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon --- 11.670
817, sports car, sport car --- 11.610
717, pickup, pickup truck --- 11.348
479, car wheel --- 10.920
```
