# python-fl-runner



接口文档
=================

&nbsp;




通信
-----------------

### 通信组件 fl_component.communication.Communication
1. 通信组件实例化
```python
communication = Communication(src_role='GUEST', dest_role='HOST')
```
| 参数 		| 类型  		 | 介绍  |
|:----------|:---------- |:----------|
| src_role 	| str       | sender 的角色 |
| dest_role | str       | reciever 的角色 |

1. 通信实例接口

| attribute | 参数  		                      | 介绍|
|:----------|:----------                     |:---------- |
| put 	    | data, tag: tuple, stream=False | data 是要发送的数据，必须为可以被pickle的数据;tag 是发送数据批次的一个特殊表示;与 get 的 tag 对应; stream 是否以流发送，当为 True 时，data必须为可迭代对象 |
| get       | tag: tuple                     | 返回值是一个 src_role 角色的参与方列表（src_role 的每一个参与方都需要向本方发送），列表内是与之对应参与方的数据(当对应 put 为流的时候，收到的是一个迭代器) |

&nbsp;

&nbsp;

&nbsp;

&nbsp;


计算
-----------------

### 流计算组件 fl_component.computing.stream_computing.engine.AbstractDataSet
1. todo

### 矩阵计算组件 fl_component.computing.tensor_computing.DataFrame
1. todo

&nbsp;

&nbsp;

&nbsp;

&nbsp;




分布式多进程
-----------------

### 分布式多进程组件 fl_component.process.Process
1. todo


&nbsp;

&nbsp;

&nbsp;

&nbsp;





算法组件
-----------------

### 算法组件接口
1. 算法组件继承基类 fl_component.algorithm.BaseAlgorithm.BaseAlgorithm 提供参数解析；输入数据获取、数据数据接口。
2. fl_component.algorithm.BaseAlgorithm.BaseAlgorithm 接口介绍

	2.1. 输入 BaseAlgorithm.fl_input
	
	| attribute 		| 类型  		 | 介绍  |
	|:----------		|:---------- |:----------|
	| fl_input.data    	| list    	 | 输入流数据，支持map reduce 计算, 参考计算组件 fl_component.computing.stream_computing.engine.AbstractDataSet   |
	| fl_input.model   	| list       | 输入模型，依据算法决定类型    |
	| fl_input.tensor  	| List[fl_component.computing.tensor_computing.DataFrame]       | 输入矩阵，参考计算组件  |
	| fl_input.role    	| str        | 角色，枚举类型，Guest; Host; Arbiter    |
	| fl_input.output_lenght | int        | dag 中输出长度   |


	2.2. 输出 BaseAlgorithm
	
	| attribute 			| 类型  		 | 介绍  |
	|:----------			|:---------- |:----------|
	| output_data    		| List[fl_component.computing.stream_computing.engine.AbstractDataSet]        | 输出流数据|
	| output_model   		| list        | 输出模型，每一项必须为可以被 pickle    |
	| output_tensor  		| List[fl_component.computing.tensor_computing.DataFrame]        | 输出矩阵  |
	| summary    			| dict        | 输出一些小数据    |
	| output_data_ret    	| List[rfc1738_url]        | 替代 output_data 可减少读写,优先级高于 output_data   |
	| output_model_ret    	| List[rfc1738_url]        | 替代 output_model 可减少读写,优先级高于 output_model    |
	| output_tensor_ret    	| List[{'id': rfc1738_url, 'label': rfc1738_url, 'feature': rfc1738_url, 'meta': rfc1738_url, }]]        | 角色，枚举类型，Guest; Host; Arbiter    |


	
3. 算法参数类继承 fl_component.algorithm.BaseAlgorithmParameter; 参数类的属性对应入参的json key
4. demo



```python
from fl_component.communication import Communication
from fl_component.algorithm import BaseAlgorithm, BaseAlgorithmParameter


class SubParameter():
	sub_a = 1
	sub_b = 'a'

class Parameter(BaseAlgorithmParameter):
    arg_a = None
	sub_arg = SubParameter()

class Demo(BaseAlgorithm):
    parameter = Parameter()
    C = Communication(src_role='GUEST', dest_role='HOST')

    def __init__(self):
        self.urls = None

    def run(self):
        if self.fl_input.role == 'GUEST':
            self.C.put(data=[0,2,5,4], tag=(1, 5, 6, 7, 8, 9), stream=True)
            # from time import sleep
            # sleep(4)
        elif self.fl_input.role == 'HOST':
            for i in list(self.C.get(tag=(1, 5, 6, 7, 8, 9))):
                print(list(i), 'zzzzzz')
            for i in self.fl_input.data:
                print(i)

            for i in self.fl_input.tensor:
                print(i)
                print(i.has_id, '(has_id)')
                print(i.has_label, '(has_label)')
                print(i.feature_names, '(feature_names)')
                print(i.id.to_numpy(), '(id tensor)')
                print(i.label.to_numpy(), '(label tensor)')
                print(i.feature.to_numpy(), '(feature tensor)')

```
	


