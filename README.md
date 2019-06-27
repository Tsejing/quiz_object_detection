# quiz_object_detection
这是用的tensorflow的objectdetection做的目标检测，主要修改了将数据集打包成tf_record的代码，以及inference.py
自己拍摄了上百张照片进行测试，效果图已上传，如图为ROBOMASTER小车的装甲板检测

# 训练注意事项
mobilenet_v1+sdd检测框架，训练的时候需指定你的tf_record训练集与验证集、下载好的预训练模型、自己制作的label_image.txt路径，同时需要修改config
配置文件。

# 导出inference
这个py文件代码不多，根据你的需求进行修改即可

# 综述与总结
对近年目标检测的主要发展做了总结，比较精炼，希望能对大家有帮助，有任何疑问欢迎邮件交流
