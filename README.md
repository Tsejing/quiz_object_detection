### 第八周作业

**一、准备数据**

作业提供155张图片，参照/object_detection/dataset_tools/create_pet_tf_record.py编写create_data.py将图片打包成tfrecord格式。

create_data.py主要将图片数据和xml数据对应起来，写成example格式，再写成tfrecord文件。

create_data.py会调用到object_detection目录下的其他代码，所以要添加到搜索模块路径。

```
import sys
sys.path.insert(0, '../quiz_object_detection')
```



**二、下载预训练模型**

作业中使用mobilenet模型ssd检测框架，在链接中ssd_mobilenet_v1_coco预训练模型。

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md



**三、修改配置文件**

num_class: 5

num_examples: 46

PATH_TO_BE_CONFIGURED：/data/weixin-39265957/quiz-w8-data/(替换成tinymind上的数据集路径）

num_steps：0

max_evals：1

eval_input_reader：false

编译proto文件，将object_detection/protos/下的proto文件编译成python文件。

（tinymind上不好调用proto命令，最好本地编译好后上传代码）

```
protoc object_detection/protos/*.proto --python_out=.
```



**四、上传代码到github、上传数据到tinymind**

代码结构：

```
+object_detection
+slim
-inference.py
-run.py
-run.sh
-ssd_mobilenet_v1_pets.config
```

数据结构：

```
-model.ckpt.data-00000-of-00001
-model.ckpt.index
-model.ckpt.meta
-labels_items.txt
-pet_train.record
-pet_val.record
-test.jpg
-ssd_mobilenet_v1_pets.config
```



**五、新建模型**

在tinymind上新建模型，参数只要配置output_dir=/output，其他都写在配置文件里了，挂载点使用run.py

运行结果

https://www.tinymind.com/executions/av5vw5mj

![output](.\output.png)



**六、问题：**

1、生成tfrecord数据时代码报错缺少trainval.txt文件

在/data/annotations/下添加trainval.txt 文件 ， 文件内容是图片的文件名。

```
00000
00001
...
00154
```

2、代码运行报错，没有test.jpg

发现没上传test.jpg到数据集中。在保存模型后，再上传数据，需要在模型设置中勾选新增的数据，否则还是报错。

